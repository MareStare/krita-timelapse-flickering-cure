import dataclasses
import os
from pathlib import Path
from shutil import copy2
from time import monotonic
from xml.etree import ElementTree

from krita import (
    Krita,
)
from PyQt5.QtCore import (
    QDir,
    QSize,
    Qt,
    QTimer,
    qCritical,
    qDebug,
    qInfo,
    qWarning,
)
from PyQt5.QtGui import QImage, QImageReader
from PyQt5.QtWidgets import (
    QCheckBox,
    QLabel,
    QLayout,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QProgressDialog,
    QPushButton,
)

PLUGIN_LABEL = "[Timelapse Flickering Cure]"

krita = Krita.instance()


def export_without_flickering(recordings_dir: str):
    try:
        try_export_without_flickering(recordings_dir)
    except Exception as exception:  # noqa: BLE001
        QMessageBox.critical(
            None,
            f"{PLUGIN_LABEL} Oops",
            f"Error exporting timelapse without flickering: {exception}",
            QMessageBox.StandardButton.Ok,
        )


def try_export_without_flickering(recordings_dir: str):
    recording_id = get_recording_id()
    timelapse_dir = Path(recordings_dir) / recording_id

    qInfo(f"Scanning timeplapse frames at: {timelapse_dir}")

    files = [
        Path(path)
        for path in sorted(
            entry.path for entry in os.scandir(timelapse_dir) if entry.is_file()
        )
    ]

    scan_start = monotonic()
    result = scan(files)
    scan_took = monotonic() - scan_start

    delete_white_frames_dialogue(
        timelapse_dir,
        recording_id,
        result,
        scan_took,
    )

    krita.action("recorder_export").trigger()


def delete_white_frames_dialogue(
    timelapse_dir: Path,
    recording_id: str,
    scan_result: "ScanResult | None",
    scan_took: float,
):
    if scan_result is None:
        qInfo("Scan was cancelled by user")
        return

    if len(scan_result.white_frames) == 0:
        QMessageBox.information(
            None,
            f"{PLUGIN_LABEL} Success",
            f"No white frames were detected (scan took {scan_took:.2f} seconds). Happy rendering!",
        )
        return

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.NoIcon)
    msg.setWindowTitle(f"{PLUGIN_LABEL} White frames deletion")
    msg.setMinimumWidth(900)

    msg.setText(
        f"Detected {len(scan_result.white_frames)} white frames "
        f"(scan took {scan_took:.2f} seconds). Delete them?"
    )

    backup_dir = (
        Path(QDir.tempPath()) / "krita_timelapses_backup" / recording_id
    )

    delete_button = msg.addButton("Confirm", QMessageBox.ButtonRole.YesRole)
    msg.addButton("Cancel", QMessageBox.ButtonRole.NoRole)
    msg.setDefaultButton(delete_button)

    backup_checkbox = QCheckBox("Backup timelapse data")

    msg.setCheckBox(backup_checkbox)

    msg.setInformativeText(
        f"Note: a backup will copy {len(scan_result.files)} image files ({scan_result.files_size / (10**9):.2f}GB in total)\n"
        f"from: {timelapse_dir}\n"
        f"to: {backup_dir}"
    )

    for label in msg.findChildren(QLabel):
        label.setWordWrap(False)

    msg.exec()

    if msg.clickedButton() != delete_button:
        qInfo("User chose not to delete white frames")
        return

    qInfo(f"User chose to delete white frames, backing up to {backup_dir}")

    if backup_checkbox.isChecked():
        create_backup(backup_dir, scan_result.files)

    delete_white_frames(scan_result.files, scan_result.white_frames)


def delete_white_frames(
    files: list[Path],
    delete_indices: list[int],
):
    if not delete_indices or not files:
        return

    delete_stack = delete_indices[::-1]
    padding = len(files[0].stem)
    deleted = 0
    first_deleted = delete_stack[-1]

    progress = ProgressBar(
        "Deleting white frames",
        "Deleting/renaming files... %p% (%v/%m files)",
        len(files) - first_deleted,
    )

    for i, file in enumerate(files[first_deleted:], start=first_deleted):
        if delete_stack and i == delete_stack[-1]:
            # qWarning(f"Deleting the white frame file: {file.name}")

            os.remove(file)

            deleted += 1
            delete_stack.pop()
        else:
            new_index = i - deleted
            new_name = f"{new_index:0{padding}d}{file.suffix}"

            # qInfo(f"Renaming {file.name} to {new_name}")

            file.rename(file.with_name(new_name))

        progress.increment()


def is_fully_white(img: QImage) -> bool:
    if img.isNull():
        return False

    fmt = img.format()

    ptr = unwrap(img.constBits())
    ptr.setsize(img.sizeInBytes())
    data = memoryview(ptr)  # ty:ignore[invalid-argument-type]

    if fmt in (
        QImage.Format_RGB32,
        QImage.Format_ARGB32,
        QImage.Format_ARGB32_Premultiplied,
    ):
        for i in range(0, len(data), 4):
            # RGB32 is typically 0xFFRRGGBB in memory (little endian)
            if (
                data[i] != 255
                or data[i + 1] != 255
                or data[i + 2] != 255
                or data[i + 3] != 255
            ):
                return False
        return True

    # Grayscale fast path
    if fmt in (QImage.Format_Grayscale8, QImage.Format_Alpha8):
        # grayscale white = 255
        for b in data:
            if b != 255:
                return False
        return True

    # Generic fallback: no conversion, interpret per pixel via pixelFormat
    w = img.width()
    h = img.height()

    for y in range(h):
        for x in range(w):
            c = img.pixelColor(x, y)
            if (
                c.red() != 255
                or c.green() != 255
                or c.blue() != 255
                or c.alpha() != 255
            ):
                return False

    return True


def get_recording_id() -> str:
    document = krita.activeDocument()

    if document is None:
        raise Exception("No active document found")  # noqa: TRY002

    xml = Krita.instance().activeDocument().documentInfo()
    date_node = ElementTree.fromstring(xml).find(".//{*}about/{*}creation-date")
    date_str = unwrap(unwrap(date_node).text)
    return "".join(char for char in date_str if char.isdigit())


@dataclasses.dataclass
class ScanResult:
    files: list[Path]
    files_size: int
    white_frames: list[int]


def scan(files: list[Path]) -> ScanResult | None:
    progress = ProgressBar(
        "Scanning for white frames",
        "Scanning files... %p% (%v/%m files)",
        len(files),
        cancellable=True,
    )

    files_size = 0

    white_frames: list[int] = []

    # A cache with (width, height) as the key and the file size of a fully white image as the value.
    # This way we can skip nonwhite images instantly if we detect the image size doesn't match the
    # one in the cache.
    cache: dict[tuple[int, int], int] = {}
    img = QImage()

    for i, file in enumerate(files):
        if progress.dialogue.wasCanceled():
            return None

        progress.increment()

        reader = QImageReader(str(file))

        byte_size = file.stat().st_size
        files_size += byte_size

        dims = reader.size()
        key = (dims.width(), dims.height())

        # For some reason, Krita UI starts unbearably lagging when we load
        # many large images in a loop, even though if we don't keep them
        # all in memory at once (we load one by one). Looks like there is
        # some issue in the internal C++ code that makes this loop extremely
        # slow even after the QImage is no longer needed.
        # This scaling helps a bunch to counter that problem
        reader.setScaledSize(QSize(dims.width() // 10, dims.height() // 10))

        cached = cache.get(key)

        if cached in (None, byte_size):
            if not reader.read(img):
                raise Exception(  # noqa: TRY002
                    f"Failed to read image {file.name}: {reader.errorString()}"
                )

            if is_fully_white(img):
                cache[key] = byte_size
                white_frames.append(i)

    return ScanResult(files, files_size, white_frames)


def delete_backup(backup_dir: Path):
    entries = list(os.scandir(backup_dir))

    progress = ProgressBar(
        "Deleting the old backup",
        "Deleting files... %p% (%v/%m files)",
        len(entries),
        # Make this destructive operation cancellable for extra safety
        cancellable=True,
    )

    for entry in entries:
        if progress.dialogue.wasCanceled():
            raise Exception("Backup deletion cancelled by user")  # noqa: TRY002

        os.remove(entry.path)


def create_backup(
    backup_dir: Path,
    files: list[Path],
):
    backup_dir.mkdir(parents=True, exist_ok=False)

    progress = ProgressBar(
        "Creating a backup",
        "Copying timelapse files... %p% (%v/%m files)",
        len(files),
    )

    for file in files:
        progress.increment()
        copy2(file, backup_dir / file.name)


class ProgressBar:
    def __init__(
        self,
        title: str,
        format: str,
        total: int,
        cancellable: bool = False,
    ):
        self.current = 0
        self.refresh_interval = 0.015
        self.last_update = monotonic()

        self.dialogue = QProgressDialog()

        bar = QProgressBar(self.dialogue)
        bar.setFormat(format)
        bar.setMaximum(total)

        self.dialogue.setBar(bar)
        self.dialogue.setWindowTitle(f"{PLUGIN_LABEL} {title}")
        self.dialogue.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.dialogue.setMinimumDuration(0)
        self.dialogue.setMinimumWidth(500)

        if cancellable:
            self.dialogue.setCancelButtonText("Cancel")

    def increment(self, label: str | None = None):
        self.current += 1

        now = monotonic()

        if (
            now - self.last_update < self.refresh_interval
            and self.current < self.dialogue.maximum()
        ):
            return

        if label is not None:
            self.dialogue.setLabelText(label)

        # setValue() calls QApplication.processEvents() internally for a modal QProgressDialog
        self.dialogue.setValue(self.current)
        self.last_update = now


def _init():
    recorder = next(
        (
            docker
            for docker in krita.dockers()
            if docker.objectName() == "RecorderDocker"
        ),
        None,
    )
    if recorder is None:
        # Retry again after a short delay because the recorder docker is not
        # available during plugin initialization. Unfortunately, there is no
        # official API to wait for it to load, so we have to poll for it.
        qDebug("Waiting for recorder export button to initialize")
        QTimer.singleShot(1000, _init)
        return

    recordings = unwrap(recorder.findChild(QLineEdit, "editDirectory")).text()
    export = unwrap(recorder.findChild(QPushButton, "buttonExport"))
    parent = unwrap(export.parentWidget())
    parent_layout = unwrap(parent.layout())
    buttons_layout = unwrap(parent_layout.findChild(QLayout, "layoutButtons"))
    export.hide()

    new_export = QPushButton(
        export.icon(), "Export (without flickering)", parent
    )
    new_export.clicked.connect(lambda: export_without_flickering(recordings))
    buttons_layout.addWidget(new_export)


def unwrap[T](value: T | None) -> T:
    if value is None:
        raise ValueError("Expected a non-None value")
    return value


try:
    _init()
except Exception as exception:  # noqa: BLE001
    qCritical(f"Timelapse Flickering Plugin Initialization Error: {exception}")
