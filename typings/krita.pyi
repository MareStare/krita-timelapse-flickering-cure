from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from typing import List, Dict, Union
KisPresetChooser = QObject
KoDockFactoryBase = QObject
class Window(QObject):
	"""* Window represents one Krita mainwindow. A window can have any number of views open on any number of documents. """

	def qwindow(self) -> QMainWindow:
		# type: () -> QMainWindow:
		"""@access public Q_SLOTS
 Return a handle to the QMainWindow widget. This is useful to e.g. parent dialog boxes and message box. """

	def dockers(self) -> List[QDockWidget]:
		# type: () -> List[QDockWidget]:
		"""@access public Q_SLOTS
 @brief dockers
@return a list of all the dockers belonging to this window """

	def views(self) -> List['View']:
		# type: () -> List[View]:
		"""@access public Q_SLOTS
 @return a list of open views in this window """

	def addView(self, document: 'Document') -> 'View':
		# type: (document) -> View:
		"""@access public Q_SLOTS
 Open a new view on the given document in this window """

	def showView(self, v: 'View') -> None:
		# type: (v) -> None:
		"""@access public Q_SLOTS
 Make the given view active in this window. If the view does not belong to this window, nothing happens. """

	def activeView(self) -> 'View':
		# type: () -> View:
		"""@access public Q_SLOTS
 @return the currently active view or 0 if no view is active """

	def activate(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief activate activates this Window. """

	def close(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief close the active window and all its Views. If there are no Views left for a given Document, that Document will also be closed. """

	def createAction(self, id: str, text: str = str(), menuLocation: str = str("tools/scripts")) -> QAction:
		# type: (id, text, menuLocation) -> QAction:
		"""@access public Q_SLOTS
 @brief createAction creates a QAction object and adds it to the action manager for this Window.
@param id The unique id for the action. This will be used to     propertize the action if any .action file is present
@param text The user-visible text of the action. If empty, the text from the    .action file is used.
@param menuLocation a /-separated string that describes which menu the action should     be places in. Default is "tools/scripts"
@return the new action. """

	def windowClosed(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
Emitted when the window is closed. """

	def themeChanged(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
Emitted when we change the color theme """

	def activeViewChanged(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
Emitted when the active view changes """

class View(QObject):
	"""* View represents one view on a document. A document can be shown in more than one view at a time. """

	def window(self) -> 'Window':
		# type: () -> Window:
		"""@access public Q_SLOTS
 @return the window this view is shown in. """

	def document(self) -> 'Document':
		# type: () -> Document:
		"""@access public Q_SLOTS
 @return the document this view is showing. """

	def setDocument(self, document: 'Document') -> None:
		# type: (document) -> None:
		"""@access public Q_SLOTS
 Reset the view to show @p document. """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @return True if the current view is visible, False if not. """

	def setVisible(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Make the current view visible. """

	def canvas(self) -> 'Canvas':
		# type: () -> Canvas:
		"""@access public Q_SLOTS
 @return the canvas this view is showing. The canvas controls things like zoom and rotation. """

	def activateResource(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 @brief activateResource activates the given resource.
@param resource: a pattern, gradient or paintop preset """

	def foregroundColor(self) -> 'ManagedColor':
		# type: () -> ManagedColor:
		"""@access public Q_SLOTS
 @brief foregroundColor allows access to the currently active foreground color. This is nominally per canvas/view, but in practice per mainwindow.
@code
color = Application.activeWindow().activeView().foregroundColor()
components = color.components()
components[0] = 1.0
components[1] = 0.6
components[2] = 0.7
color.setComponents(components)
Application.activeWindow().activeView().setForeGroundColor(color)
@endcode
@return The current foreground color """

	def backgroundColor(self) -> 'ManagedColor':
		# type: () -> ManagedColor:
		"""@access public Q_SLOTS
 @brief backgroundColor allows access to the currently active background color. This is nominally per canvas/view, but in practice per mainwindow.
@return The current background color """

	def currentBrushPreset(self) -> 'Resource':
		# type: () -> Resource:
		"""@access public Q_SLOTS
 @brief return the current selected preset
@return the current preset (Resource type = 'preset') """

	def setCurrentBrushPreset(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 @brief set the current selected preset
@param resource the current preset to set (Resource type = 'preset') """

	def currentPattern(self) -> 'Resource':
		# type: () -> Resource:
		"""@access public Q_SLOTS
 @brief return the current selected pattern
@return the current pattern (Resource type = 'pattern') """

	def setCurrentPattern(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 @brief set the current selected pattern
@param resource the current pattern to set (Resource type = 'pattern') """

	def currentGradient(self) -> 'Resource':
		# type: () -> Resource:
		"""@access public Q_SLOTS
 @brief return the current selected gradient
@return the current gradient (Resource type = 'gradient') """

	def setCurrentGradient(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 @brief set the current selected gradient
@param resource the current gradient to set (Resource type = 'gradient') """

	def currentBlendingMode(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief return the current blending mode for brush
@return the current blending mode identifier """

	def setCurrentBlendingMode(self, blendingMode: str) -> None:
		# type: (blendingMode) -> None:
		"""@access public Q_SLOTS
 @brief set the current blending mode for brush
@param blendingMode the current belding mode identifier """

	def HDRExposure(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return the current HDR Exposure value """

	def setHDRExposure(self, exposure: float) -> None:
		# type: (exposure) -> None:
		"""@access public Q_SLOTS
 @brief set the current HDR Exposure value
@param exposure the HDR Exposure to set """

	def HDRGamma(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return the current HDR Gamma value """

	def setHDRGamma(self, gamma: float) -> None:
		# type: (gamma) -> None:
		"""@access public Q_SLOTS
 @brief set the current HDR Gamma value
@param exposure the HDR Gamma to set """

	def paintingOpacity(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current opacity for brush
@return the brush opacity value (0.00=fully transparent - 1.00=fully opaque) """

	def setPaintingOpacity(self, opacity: float) -> None:
		# type: (opacity) -> None:
		"""@access public Q_SLOTS
 @brief set the current opacity for brush
@param opacity the opacity value (0.00=fully transparent - 1.00=fully opaque) """

	def brushSize(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current size for brush
@return the brush size value (in pixels) """

	def setBrushSize(self, brushSize: float) -> None:
		# type: (brushSize) -> None:
		"""@access public Q_SLOTS
 @brief set the current size for brush
@param brushSize the brush size (in pixels) """

	def brushFade(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current fade for brush
@return the brush fade value (0.00 - 1.00) """

	def setBrushFade(self, brushFade: float) -> None:
		# type: (brushFade) -> None:
		"""@access public Q_SLOTS
 @brief set the current fade for brush
@param brushFade the brush fade (0.00 - 1.00) """

	def brushRotation(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current rotation for brush tip
@return the brush tip rotation value (in degrees) """

	def setBrushRotation(self, brushRotation: float) -> None:
		# type: (brushRotation) -> None:
		"""@access public Q_SLOTS
 @brief set the current rotation for brush tip
@param brushRotation the brush tip rotation (in degrees) """

	def paintingFlow(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current flow for brush
@return the brush flow value """

	def setPaintingFlow(self, flow: float) -> None:
		# type: (flow) -> None:
		"""@access public Q_SLOTS
 @brief set the current flow value for brush
@param flow the brush flow """

	def patternSize(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return the current pattern size for brush
@return the brush pattern size value """

	def setPatternSize(self, size: float) -> None:
		# type: (size) -> None:
		"""@access public Q_SLOTS
 @brief set the current pattern size value for brush
@param flow the brush pattern size """

	def eraserMode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief return current eraser mode status (active/inactive)
@return True if eraser mode is active, otherwise False """

	def setEraserMode(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief set current eraser active/inactive
@param value Set to True to activate eraser mode, False to deactivate """

	def globalAlphaLock(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief return current global alpha lock mode (active/inactive)
@return True if is active, otherwise False """

	def setGlobalAlphaLock(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief set current global alpha lock mode active/inactive
@param value Set to True to lock global alpha mode, False to unlock """

	def disablePressure(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief return current disabled pressure status
@return True if is pressure is disabled, otherwise False """

	def setDisablePressure(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief set current disabled pressure status
@param value Set to True to disable pressure, False to enabled pressure """

	def showFloatingMessage(self, message: str, icon: QIcon, timeout: int, priority: int) -> None:
		# type: (message, icon, timeout, priority) -> None:
		"""@access public Q_SLOTS
 @brief showFloatingMessage displays a floating message box on the top-left corner of the canvas
@param message: Message to be displayed inside the floating message box
@param icon: Icon to be displayed inside the message box next to the message string
@param timeout: Milliseconds until the message box disappears
@param priority: 0 = High, 1 = Medium, 2 = Low. Higher priority messages will be displayed in place of lower priority messages """

	def selectedNodes(self) -> List['Node']:
		# type: () -> List[Node]:
		"""@access public Q_SLOTS
 @brief selectedNodes returns a list of Nodes that are selected in this view.
@code
from krita import *
w = Krita.instance().activeWindow()
v = w.activeView()
selected_nodes = v.selectedNodes()
print(selected_nodes)
@endcode
@return a list of Node objects which may be empty. """

	def flakeToDocumentTransform(self) -> QTransform:
		# type: () -> QTransform:
		"""@access public Q_SLOTS
 @brief flakeToDocumentTransform The transformation of the document relative to the view without rotation and mirroring
@return QTransform """

	def flakeToCanvasTransform(self) -> QTransform:
		# type: () -> QTransform:
		"""@access public Q_SLOTS
 @brief flakeToCanvasTransform The transformation of the canvas relative to the view without rotation and mirroring
@return QTransform """

	def flakeToImageTransform(self) -> QTransform:
		# type: () -> QTransform:
		"""@access public Q_SLOTS
 @brief flakeToImageTransform The transformation of the image relative to the view without rotation and mirroring
@return QTransform """

class Swatch(QObject):
	"""* @brief The Swatch class is a thin wrapper around the KisSwatch class. A Swatch is a single color that is part of a palette, that has a name and an id. A Swatch color can be a spot color. """

class Shape(QObject):
	"""* @brief The Shape class The shape class is a wrapper around Krita's vector objects. Some example code to parse through interesting information in a given vector layer with shapes.
@code
import sys
from krita import *

doc = Application.activeDocument()

root = doc.rootNode()

for layer in root.childNodes():
    print (str(layer.type())+" "+str(layer.name()))
    if (str(layer.type())=="vectorlayer"):
        for shape in layer.shapes():
            print(shape.name())
            print(shape.toSvg())
@endcode """

	def name(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief name
@return the name of the shape """

	def setName(self, name: str) -> None:
		# type: (name) -> None:
		"""@access public Q_SLOTS
 @brief setName
@param name which name the shape should have. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type
@return the type of shape. """

	def zIndex(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief zIndex
@return the zindex of the shape. """

	def setZIndex(self, zindex: int) -> None:
		# type: (zindex) -> None:
		"""@access public Q_SLOTS
 @brief setZIndex
@param zindex set the shape zindex value. """

	def selectable(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief selectable
@return whether the shape is user selectable. """

	def setSelectable(self, selectable: bool) -> None:
		# type: (selectable) -> None:
		"""@access public Q_SLOTS
 @brief setSelectable
@param selectable whether the shape should be user selectable. """

	def geometryProtected(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief geometryProtected
@return whether the shape is protected from user changing the shape geometry. """

	def setGeometryProtected(self, protect: bool) -> None:
		# type: (protect) -> None:
		"""@access public Q_SLOTS
 @brief setGeometryProtected
@param protect whether the shape should be geometry protected from the user. """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief visible
@return whether the shape is visible. """

	def setVisible(self, visible: bool) -> None:
		# type: (visible) -> None:
		"""@access public Q_SLOTS
 @brief setVisible
@param visible whether the shape should be visible. """

	def boundingBox(self) -> QRectF:
		# type: () -> QRectF:
		"""@access public Q_SLOTS
 @brief boundingBox the bounding box of the shape in points
@return RectF containing the bounding box. """

	def position(self) -> QPointF:
		# type: () -> QPointF:
		"""@access public Q_SLOTS
 @brief position the position of the shape in points.
@return the position of the shape in points. """

	def setPosition(self, point: QPointF) -> None:
		# type: (point) -> None:
		"""@access public Q_SLOTS
 @brief setPosition set the position of the shape.
@param point the new position in points """

	def transformation(self) -> QTransform:
		# type: () -> QTransform:
		"""@access public Q_SLOTS
 @brief transformation the 2D transformation matrix of the shape.
@return the 2D transformation matrix. """

	def setTransformation(self, matrix: QTransform) -> None:
		# type: (matrix) -> None:
		"""@access public Q_SLOTS
 @brief setTransformation set the 2D transformation matrix of the shape.
@param matrix the new 2D transformation matrix. """

	def absoluteTransformation(self) -> QTransform:
		# type: () -> QTransform:
		"""@access public Q_SLOTS
 @brief transformation the 2D transformation matrix of the shape including all grandparent transforms.
@return the 2D transformation matrix. """

	def remove(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief remove delete the shape. """

	def update(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief update queue the shape update. """

	def updateAbsolute(self, box: QRectF) -> None:
		# type: (box) -> None:
		"""@access public Q_SLOTS
 @brief updateAbsolute queue the shape update in the specified rectangle.
@param box the RectF rectangle to update. """

	def toSvg(self, prependStyles: bool = False, stripTextMode: bool = True) -> str:
		# type: (prependStyles, stripTextMode) -> str:
		"""@access public Q_SLOTS
 @brief toSvg convert the shape to svg, will not include style definitions.
@param prependStyles prepend the style data. Default: false
@param stripTextMode enable strip text mode. Default: true
@return the svg in a string. """

	def select(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief select selects the shape. """

	def deselect(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief deselect deselects the shape. """

	def isSelected(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief isSelected
@return whether the shape is selected. """

	def parentShape(self) -> 'Shape':
		# type: () -> Shape:
		"""@access public Q_SLOTS
 @brief parentShape
@return the parent GroupShape of the current shape. """

class Selection(QObject):
	"""* Selection represents a selection on Krita. A selection is not necessarily associated with a particular Node or Image.
@code
from krita import *
d = Application.activeDocument()
n = d.activeNode()
r = n.bounds()
s = Selection()
s.select(r.width() / 3, r.height() / 3, r.width() / 3, r.height() / 3, 255)
s.cut(n)
@endcode """

	def __init__(self) -> 'Shape':
		""" @brief parentShape
@return the parent GroupShape of the current shape. """

	def duplicate(self) -> 'Selection':
		# type: () -> Selection:
		"""@access public Q_SLOTS
 @return a duplicate of the selection """

	def width(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the width of the selection """

	def height(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the height of the selection """

	def x(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the left-hand position of the selection. """

	def y(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the top position of the selection. """

	def move(self, x: int, y: int) -> None:
		# type: (x, y) -> None:
		"""@access public Q_SLOTS
 Move the selection's top-left corner to the given coordinates. """

	def clear(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Make the selection entirely unselected. """

	def contract(self, value: int) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 Make the selection's width and height smaller by the given value. This will not move the selection's top-left position. """

	def copy(self, node: 'Node') -> None:
		# type: (node) -> None:
		"""@access public Q_SLOTS
 @brief copy copies the area defined by the selection from the node to the clipboard.
@param node the node from where the pixels will be copied. """

	def cut(self, node: 'Node') -> None:
		# type: (node) -> None:
		"""@access public Q_SLOTS
 @brief cut erases the area defined by the selection from the node and puts a copy on the clipboard.
@param node the node from which the selection will be cut. """

	def paste(self, destination: 'Node', x: int, y: int) -> None:
		# type: (destination, x, y) -> None:
		"""@access public Q_SLOTS
 @brief paste pastes the content of the clipboard to the given node, limited by the area of the current selection.
@param destination the node where the pixels will be written
@param x: the x position at which the clip will be written
@param y: the y position at which the clip will be written """

	def erode(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Erode the selection with a radius of 1 pixel. """

	def dilate(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Dilate the selection with a radius of 1 pixel. """

	def border(self, xRadius: int, yRadius: int) -> None:
		# type: (xRadius, yRadius) -> None:
		"""@access public Q_SLOTS
 Border the selection with the given radius. """

	def feather(self, radius: int) -> None:
		# type: (radius) -> None:
		"""@access public Q_SLOTS
 Feather the selection with the given radius. """

	def grow(self, xradius: int, yradius: int) -> None:
		# type: (xradius, yradius) -> None:
		"""@access public Q_SLOTS
 Grow the selection with the given radius. """

	def shrink(self, xRadius: int, yRadius: int, edgeLock: bool) -> None:
		# type: (xRadius, yRadius, edgeLock) -> None:
		"""@access public Q_SLOTS
 Shrink the selection with the given radius. """

	def smooth(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Smooth the selection. """

	def invert(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Invert the selection. """

	def resize(self, w: int, h: int) -> None:
		# type: (w, h) -> None:
		"""@access public Q_SLOTS
 Resize the selection to the given width and height. The top-left position will not be moved. """

	def select(self, x: int, y: int, w: int, h: int, value: int) -> None:
		# type: (x, y, w, h, value) -> None:
		"""@access public Q_SLOTS
 Select the given area. The value can be between 0 and 255; 0 is  totally unselected, 255 is totally selected. """

	def selectAll(self, node: 'Node', value: int) -> None:
		# type: (node, value) -> None:
		"""@access public Q_SLOTS
 Select all pixels in the given node. The value can be between 0 and 255; 0 is  totally unselected, 255 is totally selected. """

	def replace(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 Replace the current selection's selection with the one of the given selection. """

	def add(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 Add the given selection's selected pixels to the current selection. """

	def subtract(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 Subtract the given selection's selected pixels from the current selection. """

	def intersect(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 Intersect the given selection with this selection. """

	def symmetricdifference(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 Intersect with the inverse of the given selection with this selection. """

	def pixelData(self, x: int, y: int, w: int, h: int) -> QByteArray:
		# type: (x, y, w, h) -> QByteArray:
		"""@access public Q_SLOTS
 @brief pixelData reads the given rectangle from the Selection's mask and returns it as a byte array. The pixel data starts top-left, and is ordered row-first. The byte array will contain one byte for every pixel, representing the selectedness. 0 is totally unselected, 255 is fully selected. You can read outside the Selection's boundaries; those pixels will be unselected. The byte array is a copy of the original selection data.
@param x x position from where to start reading
@param y y position from where to start reading
@param w row length to read
@param h number of rows to read
@return a QByteArray with the pixel data. The byte array may be empty. """

	def setPixelData(self, value: Union[QByteArray, bytes, bytearray], x: int, y: int, w: int, h: int) -> None:
		# type: (value, x, y, w, h) -> None:
		"""@access public Q_SLOTS
 @brief setPixelData writes the given bytes, of which there must be enough, into the Selection.
@param value the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (w * h) bytes are read.
@param x the x position to start writing from
@param y the y position to start writing from
@param w the width of each row
@param h the number of rows to write """

class Resource(QObject):
	"""* A Resource represents a gradient, pattern, brush tip, brush preset, palette or  workspace definition.
@code
allPresets = Application.resources("preset")
for preset in allPresets:
    print(preset.name())
@endcode  Resources are identified by their type, name and filename. If you want to change the contents of a resource, you should read its data using data(), parse it and write the changed contents back. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 Return the type of this resource. Valid types are: <ul> <li>pattern: a raster image representing a pattern <li>gradient: a gradient <li>brush: a brush tip <li>preset: a brush preset <li>palette: a color set <li>workspace: a workspace definition. </ul> """

	def name(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 The user-visible name of the resource. """

	def setName(self, value: str) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 setName changes the user-visible name of the current resource. """

	def filename(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 The filename of the resource, if present. Not all resources are loaded from files. """

	def image(self) -> QImage:
		# type: () -> QImage:
		"""@access public Q_SLOTS
 An image that can be used to represent the resource in the user interface. For some resources, like patterns, the  image is identical to the resource, for others it's a mere icon. """

	def setImage(self, image: QImage) -> None:
		# type: (image) -> None:
		"""@access public Q_SLOTS
 Change the image for this resource. """

class Preset(QObject):
	"""* @brief The Preset class Preset is a resource object that stores brush preset data. An example for printing the current brush preset and all its settings:
@code
from krita import *

view = Krita.instance().activeWindow().activeView()
preset = Preset(view.currentBrushPreset())

print ( preset.toXML() )
@endcode """

	def toXML(self) -> str:
		# type: () -> str:
		"""@access public
 @brief toXML convert the preset settings into a preset formatted xml.
@return the xml in a string. """

	def fromXML(self, xml: str) -> None:
		# type: (xml) -> None:
		"""@access public
 @brief fromXML convert the preset settings into a preset formatted xml.
@param xml valid xml preset string. """

	def paintOpPreset(self) -> 'KisPaintOpPresetSP':
		# type: () -> 'KisPaintOpPresetSP':
		"""@access private
 @brief paintOpPreset
@return gives a KisPaintOpPreset object back """

class Palette(QObject):
	"""* @brief The Palette class Palette is a resource object that stores organised color data. It's purpose is to allow artists to save colors and store them. An example for printing all the palettes and the entries:
@code
import sys
from krita import *

resources = Application.resources("palette")

for (k, v) in resources.items():
    print(k)
    palette = Palette(v)
    for x in range(palette.numberOfEntries()):
        entry = palette.colorSetEntryByIndex(x)
        print(x, entry.name(), entry.id(), entry.spotColor())
@endcode """

	def numberOfEntries(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief number of filled colors (swatches) in palette NOTE: same as `colorsCountTotal()`
@return total number of colors """

	def columnCount(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Palettes are defined in grids. The number of column define grid width. The number of rows will depend of columns and total number of entries.
@return the number of columns this palette is set to use. """

	def setColumnCount(self, columns: int) -> None:
		# type: (columns) -> None:
		"""@access public Q_SLOTS
 @brief Palettes are defined in grids. The number of column define grid width, this value can be defined. The number of rows will depend of columns and total number of entries.
@param columns Set the amount of columns this palette should use. """

	def rowCount(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief The number of rows in the palette grid. If the palette has groups, the row count is defined by the groups' row count. Otherwise, it's determined by the number of columns and entries.
@return the number of rows this palette has. """

	def rowCountGroup(self, name: str) -> int:
		# type: (name) -> int:
		"""@access public Q_SLOTS
 @brief The number of rows defined in the given group.
@param name of the group to check.
@return the number of rows this group is set to use. """

	def setRowCountGroup(self, rows: int, name: str) -> None:
		# type: (rows, name) -> None:
		"""@access public Q_SLOTS
 @brief Set the number of rows defined in the given group.
@param rows the amount of rows this group should use.
@param name of the group to modify. """

	def comment(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief the comment or description associated with the palette.
@return A string for which value contains the comment/description of palette. """

	def setComment(self, comment: str) -> None:
		# type: (comment) -> None:
		"""@access public Q_SLOTS
 @brief the comment or description associated with the palette.
@param comment set the comment or description associated with the palette. """

	def groupNames(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief Palette content can be organized in groups.
@return The list of group names (list of string). This list follow the order the groups are defined in palette. """

	def addGroup(self, name: str) -> None:
		# type: (name) -> None:
		"""@access public Q_SLOTS
 @brief Palette content can be organized in groups. This method allows to add a new group in palette.
@param name The name of the new group to add. """

	def removeGroup(self, name: str, keepColors: bool = True) -> None:
		# type: (name, keepColors) -> None:
		"""@access public Q_SLOTS
 @brief Palette content can be organized in groups. This method allows to remove an existing group from palette.
@param name The name of the group to remove.
@param keepColors whether or not to delete all the colors inside, or to move them to the default group. """

	def colorsCountTotal(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief number of filled colors (swatches) in palette NOTE: same as `numberOfEntries()`
@return total number of colors """

	def colorsCountGroup(self, name: str) -> int:
		# type: (name) -> int:
		"""@access public Q_SLOTS
 @brief colorsCountGroup
@param name of the group to check. Empty is the default group.
@return the amount of filled colors within that group. """

	def slotCount(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief number of slots for swatches in palette This includes any empty slots not filled by a color.
@return total number of slots """

	def slotCountGroup(self, name: str) -> int:
		# type: (name) -> int:
		"""@access public Q_SLOTS
 @brief number of slots for swatches in group This includes any empty slots not filled by a color.
@param name of the group to check. Empty is the default group.
@return number of slots in group """

	def entryByIndex(self, index: int) -> 'Swatch':
		# type: (index) -> Swatch:
		"""@access public Q_SLOTS
 @brief colorSetEntryByIndex get the colorsetEntry from the global index. DEPRECATED: use `entryByIndex()` instead
@param index the global index
@return the colorset entry/
    Q_DECL_DEPRECATED Swatch *colorSetEntryByIndex(int index);

    /**
@brief get color (swatch) from the global index.
@param index the global index
@return The Swatch color for given index. """

	def entryByIndexFromGroup(self, index: int, groupName: str) -> 'Swatch':
		# type: (index, groupName) -> Swatch:
		"""@access public Q_SLOTS
 @brief colorSetEntryFromGroup DEPRECATED: use `entryByIndexFromGroup()` instead
@param index index in the group.
@param groupName the name of the group to get the color from.
@return the colorsetentry./
    Q_DECL_DEPRECATED Swatch *colorSetEntryFromGroup(int index, const QString &groupName);

    /**
@brief get color (swatch) from the given group index.
@param index index in the group.
@param groupName the name of the group to get the color from.
@return The Swatch color for given index within given group name. """

	def addEntry(self, entry: 'Swatch', groupName: str = str()) -> None:
		# type: (entry, groupName) -> None:
		"""@access public Q_SLOTS
 @brief add a color entry to a group. Color is appended to the end.
@param entry the entry
@param groupName the name of the group to add to. """

	def removeEntry(self, index: int) -> None:
		# type: (index) -> None:
		"""@access public Q_SLOTS
 @brief Remove the color entry at the given index in this palette.
@param index index in this palette. """

	def removeEntryFromGroup(self, index: int, groupName: str) -> None:
		# type: (index, groupName) -> None:
		"""@access public Q_SLOTS
 @brief Remove the color entry at the given index in the given group.
@param index index in the group.
@param groupName the name of the group to remove the entry from. """

	def renameGroup(self, oldGroupName: str, newGroupName: str) -> None:
		# type: (oldGroupName, newGroupName) -> None:
		"""@access public Q_SLOTS
 @brief changeGroupName change the group name. DEPRECATED: use `renameGroup()` instead
@param oldGroupName the old groupname to change.
@param newGroupName the new name to change it into.
@return whether successful. Reasons for failure include not knowing have oldGroupName/
    Q_DECL_DEPRECATED void changeGroupName(QString oldGroupName, QString newGroupName);

    /**
@brief rename a group
@param oldGroupName the old groupname to change.
@param newGroupName the new name to change it into. """

	def moveGroup(self, groupName: str, groupNameInsertBefore: str = str()) -> None:
		# type: (groupName, groupNameInsertBefore) -> None:
		"""@access public Q_SLOTS
 @brief Move the group `groupName` to position before group `groupNameInsertBefore`.
@param groupName group to move.
@param groupNameInsertBefore reference group for which `groupName` have to be moved before. """

	def save(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief save the palette WARNING: this method does nothing and need to be implemented!
@return always False """

	def colorSet(self) -> 'KoColorSetSP':
		# type: () -> 'KoColorSetSP':
		"""@access private
 @brief colorSet
@return gives a KoColorSet object back """

class Notifier(QObject):
	"""* The Notifier can be used to be informed of state changes in the Krita application. """

	def active(self) -> bool:
		# type: () -> bool:
		"""@access public
 @return true if the Notifier is active. """

	def setActive(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public
 Enable or disable the Notifier """

	def applicationClosing(self) -> None:
		# type: () -> None:
		"""@access public
 @brief applicationClosing is emitted when the application is about to close. This happens after any documents and windows are closed. """

	def imageCreated(self, image: 'Document') -> None:
		# type: (image) -> None:
		"""@access public
 @brief imageCreated is emitted whenever a new image is created and registered with the application. """

	def imageSaved(self, filename: str) -> None:
		# type: (filename) -> None:
		"""@access public
 @brief imageSaved is emitted whenever a document is saved.
@param filename the filename of the document that has been saved. """

	def imageClosed(self, filename: str) -> None:
		# type: (filename) -> None:
		"""@access public
 @brief imageClosed is emitted whenever the last view on an image is closed. The image does not exist anymore in Krita
@param filename the filename of the image. """

	def viewCreated(self, view: 'View') -> None:
		# type: (view) -> None:
		"""@access public
 @brief viewCreated is emitted whenever a new view is created.
@param view the view """

	def viewClosed(self, view: 'View') -> None:
		# type: (view) -> None:
		"""@access public
 @brief viewClosed is emitted whenever a view is closed
@param view the view """

	def windowIsBeingCreated(self, window: 'Window') -> None:
		# type: (window) -> None:
		"""@access public
 @brief windowCreated is emitted whenever a window is being created
@param window the window; this is called from the constructor of the window, before the xmlgui file is loaded """

	def windowCreated(self) -> None:
		# type: () -> None:
		"""@access public
 @brief windowIsCreated is emitted after main window is completely created """

	def configurationChanged(self) -> None:
		# type: () -> None:
		"""@access public
 @brief configurationChanged is emitted every time Krita's configuration has changed. """

class Node(QObject):
	"""* Node represents a layer or mask in a Krita image's Node hierarchy. Group layers can contain other layers and masks; layers can contain masks. """

	def __init__(self) -> None:
		""" @brief configurationChanged is emitted every time Krita's configuration has changed. """

	def clone(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief clone clone the current node. The node is not associated with any image. """

	def alphaLocked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief alphaLocked checks whether the node is a paint layer and returns whether it is alpha locked
@return whether the paint layer is alpha locked, or false if the node is not a paint layer """

	def setAlphaLocked(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setAlphaLocked set the layer to value if the node is paint layer. """

	def blendingMode(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the blending mode of the layer. The values of the blending modes are defined in @see KoCompositeOpRegistry.h """

	def setBlendingMode(self, value: str) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setBlendingMode set the blending mode of the node to the given value
@param value one of the string values from @see KoCompositeOpRegistry.h """

	def channels(self) -> List['Channel']:
		# type: () -> List[Channel]:
		"""@access public Q_SLOTS
 @brief channels creates a list of Channel objects that can be used individually to show or hide certain channels, and to retrieve the contents of each channel in a node separately. Only layers have channels, masks do not, and calling channels on a Node that is a mask will return an empty list.
@return the list of channels ordered in by position of the channels in pixel position """

	def childNodes(self) -> List['Node']:
		# type: () -> List[Node]:
		"""@access public Q_SLOTS
 @brief childNodes
@return returns a list of child nodes of the current node. The nodes are ordered from the bottommost up. The function is not recursive. """

	def findChildNodes(self, name: str = str(), recursive: bool = False, partialMatch: bool = False, type: str = str(), colorLabelIndex: int = 0) -> List['Node']:
		# type: (name, recursive, partialMatch, type, colorLabelIndex) -> List[Node]:
		"""@access public Q_SLOTS
 @brief findChildNodes
@param name name of the child node to search for. Leaving this blank will return all nodes.
@param recursive whether or not to search recursively. Defaults to false.
@param partialMatch return if the name partially contains the string (case insensitive). Defaults to false.
@param type filter returned nodes based on type
@param colorLabelIndex filter returned nodes based on color label index
@return returns a list of child nodes and grand child nodes of the current node that match the search criteria. """

	def addChildNode(self, child: 'Node', above: 'Node') -> bool:
		# type: (child, above) -> bool:
		"""@access public Q_SLOTS
 @brief addChildNode adds the given node in the list of children.
@param child the node to be added
@param above the node above which this node will be placed
@return false if adding the node failed """

	def removeChildNode(self, child: 'Node') -> bool:
		# type: (child) -> bool:
		"""@access public Q_SLOTS
 @brief removeChildNode removes the given node from the list of children.
@param child the node to be removed """

	def setChildNodes(self, nodes: List['Node']) -> None:
		# type: (nodes) -> None:
		"""@access public Q_SLOTS
 @brief setChildNodes this replaces the existing set of child nodes with the new set.
@param nodes The list of nodes that will become children, bottom-up -- the first node, is the bottom-most node in the stack. """

	def colorDepth(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@return the color depth. """

	def colorModel(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief colorModel retrieve the current color model of this document: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@return the internal color model string. """

	def colorProfile(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the name of the current color profile """

	def setColorProfile(self, colorProfile: str) -> bool:
		# type: (colorProfile) -> bool:
		"""@access public Q_SLOTS
 @brief setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is <i>not</i> converted.
@param colorProfile
@return if assigning the color profile worked """

	def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> bool:
		# type: (colorModel, colorDepth, colorProfile) -> bool:
		"""@access public Q_SLOTS
 @brief setColorSpace convert the node to the given colorspace
@param colorModel A string describing the color model of the node: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@param colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@param colorProfile a valid color profile for this color model and color depth combination. """

	def animated(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Krita layers can be animated, i.e., have frames.
@return return true if the layer has frames. Currently, the scripting framework does not give access to the animation features. """

	def enableAnimation(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief enableAnimation make the current layer animated, so it can have frames. """

	def setPinnedToTimeline(self, pinned: bool) -> None:
		# type: (pinned) -> None:
		"""@access public Q_SLOTS
 @brief Sets whether or not node should be pinned to the Timeline Docker, regardless of selection activity. """

	def isPinnedToTimeline(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @return Returns true if node is pinned to the Timeline Docker or false if it is not. """

	def setCollapsed(self, collapsed: bool) -> None:
		# type: (collapsed) -> None:
		"""@access public Q_SLOTS
 Sets the state of the node to the value of @param collapsed """

	def collapsed(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 returns the collapsed state of this node """

	def colorLabel(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 Sets a color label index associated to the layer.  The actual color of the label and the number of available colors is defined by Krita GUI configuration. """

	def setColorLabel(self, index: int) -> None:
		# type: (index) -> None:
		"""@access public Q_SLOTS
 @brief setColorLabel sets a color label index associated to the layer.  The actual color of the label and the number of available colors is defined by Krita GUI configuration.
@param index an integer corresponding to the set of available color labels. """

	def inheritAlpha(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief inheritAlpha checks whether this node has the inherits alpha flag set
@return true if the Inherit Alpha is set """

	def setInheritAlpha(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 set the Inherit Alpha flag to the given value """

	def locked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief locked checks whether the Node is locked. A locked node cannot be changed.
@return true if the Node is locked, false if it hasn't been locked. """

	def setLocked(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 set the Locked flag to the give value """

	def hasExtents(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief does the node have any content in it?
@return if node has any content in it """

	def name(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the user-visible name of this node. """

	def setName(self, name: str) -> None:
		# type: (name) -> None:
		"""@access public Q_SLOTS
 rename the Node to the given name """

	def opacity(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 return the opacity of the Node. The opacity is a value between 0 and 255. """

	def setOpacity(self, value: int) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 set the opacity of the Node to the given value. The opacity is a value between 0 and 255. """

	def parentNode(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 return the Node that is the parent of the current Node, or 0 if this is the root Node. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return The type of the node. Valid types are: <ul>  <li>paintlayer  <li>grouplayer  <li>filelayer  <li>filterlayer  <li>filllayer  <li>clonelayer  <li>vectorlayer  <li>transparencymask  <li>filtermask  <li>transformmask  <li>selectionmask  <li>colorizemask </ul> If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def icon(self) -> QIcon:
		# type: () -> QIcon:
		"""@access public Q_SLOTS
 @brief icon
@return the icon associated with the layer. """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 Check whether the current Node is visible in the layer stack """

	def hasKeyframeAtTime(self, frameNumber: int) -> bool:
		# type: (frameNumber) -> bool:
		"""@access public Q_SLOTS
 Check to see if frame number on layer is a keyframe """

	def setVisible(self, visible: bool) -> None:
		# type: (visible) -> None:
		"""@access public Q_SLOTS
 Set the visibility of the current node to @param visible """

	def pixelData(self, x: int, y: int, w: int, h: int) -> QByteArray:
		# type: (x, y, w, h) -> QByteArray:
		"""@access public Q_SLOTS
 @brief pixelData reads the given rectangle from the Node's paintable pixels, if those exist, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first. The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float. You can read outside the node boundaries; those pixels will be transparent black. The order of channels is: <ul> <li>Integer RGBA: Blue, Green, Red, Alpha <li>Float RGBA: Red, Green, Blue, Alpha <li>GrayA: Gray, Alpha <li>Selection: selectedness <li>LabA: L, a, b, Alpha <li>CMYKA: Cyan, Magenta, Yellow, Key, Alpha <li>XYZA: X, Y, Z, A <li>YCbCrA: Y, Cb, Cr, Alpha </ul> The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object. If you read the pixeldata of a mask, a filter or generator layer, you get the selection bytes, which is one channel with values in the range from 0..255. If you want to change the pixels of a node you can write the pixels back after manipulation with setPixelData(). This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.
@param x x position from where to start reading
@param y y position from where to start reading
@param w row length to read
@param h number of rows to read
@return a QByteArray with the pixel data. The byte array may be empty. """

	def pixelDataAtTime(self, x: int, y: int, w: int, h: int, time: int) -> QByteArray:
		# type: (x, y, w, h, time) -> QByteArray:
		"""@access public Q_SLOTS
 @brief pixelDataAtTime a basic function to get pixeldata from an animated node at a given time.
@param x the position from the left to start reading.
@param y the position from the top to start reader
@param w the row length to read
@param h the number of rows to read
@param time the frame number
@return a QByteArray with the pixel data. The byte array may be empty. """

	def projectionPixelData(self, x: int, y: int, w: int, h: int) -> QByteArray:
		# type: (x, y, w, h) -> QByteArray:
		"""@access public Q_SLOTS
 @brief projectionPixelData reads the given rectangle from the Node's projection (that is, what the node looks like after all sub-Nodes (like layers in a group or masks on a layer) have been applied, and returns it as a byte array. The pixel data starts top-left, and is ordered row-first. The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float. You can read outside the node boundaries; those pixels will be transparent black. The order of channels is: <ul> <li>Integer RGBA: Blue, Green, Red, Alpha <li>Float RGBA: Red, Green, Blue, Alpha <li>GrayA: Gray, Alpha <li>Selection: selectedness <li>LabA: L, a, b, Alpha <li>CMYKA: Cyan, Magenta, Yellow, Key, Alpha <li>XYZA: X, Y, Z, A <li>YCbCrA: Y, Cb, Cr, Alpha </ul> The byte array is a copy of the original node data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object. If you read the projection of a mask, you get the selection bytes, which is one channel with values in the range from 0..255. If you want to change the pixels of a node you can write the pixels back after manipulation with setPixelData(). This will only succeed on nodes with writable pixel data, e.g not on groups or file layers.
@param x x position from where to start reading
@param y y position from where to start reading
@param w row length to read
@param h number of rows to read
@return a QByteArray with the pixel data. The byte array may be empty. """

	def setPixelData(self, value: Union[QByteArray, bytes, bytearray], x: int, y: int, w: int, h: int) -> bool:
		# type: (value, x, y, w, h) -> bool:
		"""@access public Q_SLOTS
 @brief setPixelData writes the given bytes, of which there must be enough, into the Node, if the Node has writable pixel data: <ul> <li>paint layer: the layer's original pixels are overwritten <li>filter layer, generator layer, any mask: the embedded selection's pixels are overwritten. <b>Note:</b> for these </ul> File layers, Group layers, Clone layers cannot be written to. Calling setPixelData on those layer types will silently do nothing.
@param value the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.
@param x the x position to start writing from
@param y the y position to start writing from
@param w the width of each row
@param h the number of rows to write
@return true if writing the pixeldata worked """

	def bounds(self) -> QRect:
		# type: () -> QRect:
		"""@access public Q_SLOTS
 @brief bounds return the exact bounds of the node's paint device
@return the bounds, or an empty QRect if the node has no paint device or is empty. """

	def move(self, x: int, y: int) -> None:
		# type: (x, y) -> None:
		"""@access public Q_SLOTS
  move the pixels to the given x, y location in the image coordinate space. """

	def position(self) -> QPoint:
		# type: () -> QPoint:
		"""@access public Q_SLOTS
 @brief position returns the position of the paint device of this node. The position is always 0,0 unless the layer has been moved. If you want to know the topleft position of the rectangle around the actual non-transparent pixels in the node, use bounds().
@return the top-left position of the node """

	def remove(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief remove removes this node from its parent image. """

	def duplicate(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief duplicate returns a full copy of the current node. The node is not inserted in the graphic
@return a valid Node object or 0 if the node couldn't be duplicated. """

	def save(self, filename: str, xRes: float, yRes: float, exportConfiguration: 'InfoObject', exportRect: QRect = QRect()) -> bool:
		# type: (filename, xRes, yRes, exportConfiguration, exportRect) -> bool:
		"""@access public Q_SLOTS
 @brief save exports the given node with this filename. The extension of the filename determines the filetype.
@param filename the filename including extension
@param xRes the horizontal resolution in pixels per pt (there are 72 pts in an inch)
@param yRes the horizontal resolution in pixels per pt (there are 72 pts in an inch)
@param exportConfiguration a configuration object appropriate to the file format.
@param exportRect the export bounds for saving a node as a QRect If \p exportRect is empty, then save exactBounds() of the node. If you'd like to save the image- aligned area of the node, just pass image->bounds() there. See Document->exportImage for InfoObject details.
@return true if saving succeeded, false if it failed. """

	def mergeDown(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief mergeDown merges the given node with the first visible node underneath this node in the layerstack. This will drop all per-layer metadata. """

	def scaleNode(self, origin: QPointF, width: int, height: int, strategy: str) -> None:
		# type: (origin, width, height, strategy) -> None:
		"""@access public Q_SLOTS
 @brief scaleNode
@param origin the origin point
@param width the width
@param height the height
@param strategy the scaling strategy. There's several ones amongst these that aren't available in the regular UI. <ul> <li>Hermite</li> <li>Bicubic - Adds pixels using the color of surrounding pixels. Produces smoother tonal gradations than Bilinear.</li> <li>Box - Replicate pixels in the image. Preserves all the original detail, but can produce jagged effects.</li> <li>Bilinear - Adds pixels averaging the color values of surrounding pixels. Produces medium quality results when the image is scaled from half to two times the original size.</li> <li>Bell</li> <li>BSpline</li> <li>Lanczos3 - Offers similar results than Bicubic, but maybe a little bit sharper. Can produce light and dark halos along strong edges.</li> <li>Mitchell</li> </ul> """

	def rotateNode(self, radians: float) -> None:
		# type: (radians) -> None:
		"""@access public Q_SLOTS
 @brief rotateNode rotate this layer by the given radians.
@param radians amount the layer should be rotated in, in radians. """

	def cropNode(self, x: int, y: int, w: int, h: int) -> None:
		# type: (x, y, w, h) -> None:
		"""@access public Q_SLOTS
 @brief cropNode crop this layer.
@param x the left edge of the cropping rectangle.
@param y the top edge of the cropping rectangle
@param w the right edge of the cropping rectangle
@param h the bottom edge of the cropping rectangle """

	def shearNode(self, angleX: float, angleY: float) -> None:
		# type: (angleX, angleY) -> None:
		"""@access public Q_SLOTS
 @brief shearNode perform a shear operation on this node.
@param angleX the X-angle in degrees to shear by
@param angleY the Y-angle in degrees to shear by """

	def thumbnail(self, w: int, h: int) -> QImage:
		# type: (w, h) -> QImage:
		"""@access public Q_SLOTS
 @brief thumbnail create a thumbnail of the given dimensions. The thumbnail is sized according to the layer dimensions, not the image dimensions. If the requested size is too big a null QImage is created. If the current node cannot generate a thumbnail, a transparent QImage of the requested size is generated.
@return a QImage representing the layer contents. """

	def layerStyleToAsl(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief layerStyleToAsl retrieve the current layer's style in ASL format.
@return a QString in ASL format representing the layer style. """

	def setLayerStyleFromAsl(self, asl: str) -> bool:
		# type: (asl) -> bool:
		"""@access public Q_SLOTS
 @brief setLayerStyleFromAsl set a new layer style for this node.
@param aslContent a string formatted in ASL format containing the layer style
@return true if layer style was set, false if failed. """

	def index(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief index the index of the node inside the parent
@return an integer representing the node's index inside the parent """

	def uniqueId(self) -> QUuid:
		# type: () -> QUuid:
		"""@access public Q_SLOTS
 @brief uniqueId uniqueId of the node
@return a QUuid representing a unique id to identify the node """

	def paintAbility(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief paint a line on the canvas. Uses current brush preset
@param pointOne starting point
@param pointTwo end point
@param pressureOne starting pressure
@param pressureTwo end pressure
@param strokeStyle appearance of the outline, one of: <ul> <li>None - will use Foreground Color, since line would be invisible otherwise <li>ForegroundColor</li> <li>BackgroundColor</li> </ul>/
    void paintLine(const QPointF pointOne,
                   const QPointF pointTwo,
                   double pressureOne = 1.0,
                   double pressureTwo = 1.0,
                   const QString strokeStyle = PaintingResources::defaultStrokeStyle);

    /**
@brief paint a rectangle on the canvas. Uses current brush preset
@param rect QRect with x, y, width, and height
@param strokeStyle appearance of the outline, one of: <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> </ul> Default is ForegroundColor.
@param fillStyle appearance of the fill, one of: <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> <li>Pattern</li> </ul> Default is None./
    void paintRectangle(const QRectF &rect,
                        const QString strokeStyle = PaintingResources::defaultStrokeStyle,
                        const QString fillStyle = PaintingResources::defaultFillStyle);

    /**
@brief paint a polygon on the canvas. Uses current brush preset
@param list of Qpoints <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> </ul> Default is ForegroundColor.
@param fillStyle appearance of the fill, one of: <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> <li>Pattern</li> </ul> Default is None./
    void paintPolygon(const QList<QPointF> points,
                      const QString strokeStyle = PaintingResources::defaultStrokeStyle,
                      const QString fillStyle = PaintingResources::defaultFillStyle);
    /**
@brief paint an ellipse on the canvas. Uses current brush preset
@param rect QRect with x, y, width, and height <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> </ul> Default is ForegroundColor.
@param fillStyle appearance of the fill, one of: <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> <li>Pattern</li> </ul> Default is None./
    void paintEllipse(const QRectF &rect,
                      const QString strokeStyle = PaintingResources::defaultStrokeStyle,
                      const QString fillStyle = PaintingResources::defaultFillStyle);
    /**
@brief paint a custom path on the canvas. Uses current brush preset
@param  path QPainterPath to determine path <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> </ul> Default is ForegroundColor.
@param fillStyle appearance of the fill, one of: <ul> <li>None <li>ForegroundColor</li> <li>BackgroundColor</li> <li>Pattern</li> </ul> Default is None./
    void paintPath(const QPainterPath &path,
                   const QString strokeStyle = PaintingResources::defaultStrokeStyle,
                   const QString fillStyle = PaintingResources::defaultFillStyle);
    /**
@brief paintAbility can be used to determine whether this node can be painted on with the current brush preset.
@return QString, one of the following: <ul> <li>VECTOR - This node is vector-based.</li> <li>CLONE - This node is a Clone Layer.</li> <li>PAINT - This node is paintable by the current brush preset.</li> <li>UNPAINTABLE - This node is not paintable, or a null preset is somehow selected./li> <li>MYPAINTBRUSH_UNPAINTABLE - This node's non-RGBA colorspace cannot be painted on by the currently selected MyPaint brush.</li> </ul> """

	def paintDevice(self) -> 'KisPaintDeviceSP':
		# type: () -> 'KisPaintDeviceSP':
		"""@access private
 @brief paintDevice gives access to the internal paint device of this Node
@return the paintdevice or 0 if the node does not have an editable paint device. """

class ManagedColor(QObject):
	"""* @brief The ManagedColor class is a class to handle colors that are color managed. A managed color is a color of which we know the model(RGB, LAB, CMYK, etc), the bitdepth and the specific properties of its colorspace, such as the whitepoint, chromaticities, trc, etc, as represented by the color profile. Krita has two color management systems. LCMS and OCIO. LCMS is the one handling the ICC profile stuff, and the major one handling that ManagedColor deals with. OCIO support is only in the display of the colors. ManagedColor has some support for it in colorForCanvas() All colors in Krita are color managed. QColors are understood as RGB-type colors in the sRGB space. We recommend you make a color like this:
@code
colorYellow = ManagedColor("RGBA", "U8", "")
QVector<float> yellowComponents = colorYellow.components()
yellowComponents[0] = 1.0
yellowComponents[1] = 1.0
yellowComponents[2] = 0
yellowComponents[3] = 1.0
colorYellow.setComponents(yellowComponents)
QColor yellow = colorYellow.colorForCanvas(canvas)
@endcode """

	def __init__(self) -> 'KisPaintDeviceSP':
		""" @brief paintDevice gives access to the internal paint device of this Node
@return the paintdevice or 0 if the node does not have an editable paint device. """

	def colorForCanvas(self, canvas: 'Canvas') -> QColor:
		# type: (canvas) -> QColor:
		"""@access public
 @brief colorForCanvas
@param canvas the canvas whose color management you'd like to use. In Krita, different views have separate canvasses, and these can have different OCIO configurations active.
@return the QColor as it would be displaying on the canvas. This result can be used to draw widgets with the correct configuration applied. """

	@staticmethod
	def fromQColor(qcolor: QColor, canvas: 'Canvas' = 0) ->  'ManagedColor':
		# type: (qcolor, canvas) ->  ManagedColor:
		"""@access public
 @brief fromQColor is the (approximate) reverse of colorForCanvas()
@param qcolor the QColor to convert to a KoColor.
@param canvas the canvas whose color management you'd like to use.
@return the approximated ManagedColor, to use for canvas resources. """

	def colorDepth(self) -> str:
		# type: () -> str:
		"""@access public
 colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@return the color depth. """

	def colorModel(self) -> str:
		# type: () -> str:
		"""@access public
 @brief colorModel retrieve the current color model of this document: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@return the internal color model string. """

	def colorProfile(self) -> str:
		# type: () -> str:
		"""@access public
 @return the name of the current color profile """

	def setColorProfile(self, colorProfile: str) -> bool:
		# type: (colorProfile) -> bool:
		"""@access public
 @brief setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is <i>not</i> converted.
@param colorProfile
@return false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed. """

	def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> bool:
		# type: (colorModel, colorDepth, colorProfile) -> bool:
		"""@access public
 @brief setColorSpace convert the nodes and the image to the given colorspace. The conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as flags and no blackpoint compensation.
@param colorModel A string describing the color model of the image: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@param colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@param colorProfile a valid color profile for this color model and color depth combination.
@return false the combination of these arguments does not correspond to a colorspace. """

	def components(self) -> List[float]:
		# type: () -> List[float]:
		"""@access public
 @brief components
@return a QVector containing the channel/components of this color normalized. This includes the alphachannel. """

	def componentsOrdered(self) -> List[float]:
		# type: () -> List[float]:
		"""@access public
 @brief componentsOrdered()
@return same as Components, except the values are ordered to the display. """

	def setComponents(self, values: List[float]) -> None:
		# type: (values) -> None:
		"""@access public
 @brief setComponents Set the channel/components with normalized values. For integer colorspace, this obviously means the limit is between 0.0-1.0, but for floating point colorspaces, 2.4 or 103.5 are still meaningful (if bright) values.
@param values the QVector containing the new channel/component values. These should be normalized. """

	def toXML(self) -> str:
		# type: () -> str:
		"""@access public
 Serialize this color following Create's swatch color specification available at https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft """

	def fromXML(self, xml: str) -> None:
		# type: (xml) -> None:
		"""@access public
 Unserialize a color following Create's swatch color specification available at https://web.archive.org/web/20110826002520/http://create.freedesktop.org/wiki/Swatches_-_color_file_format/Draft
@param xml an XML color
@return the unserialized color, or an empty color object if the function failed         to unserialize the color """

	def toQString(self) -> str:
		# type: () -> str:
		"""@access public
 @brief toQString create a user-visible string of the channel names and the channel values
@return a string that can be used to display the values of this color to the user. """

class Krita(QObject):
	"""* Krita is a singleton class that offers the root access to the Krita object hierarchy. The Krita.instance() is aliased as two builtins: Scripter and Application. """

	def activeDocument(self) -> 'Document':
		# type: () -> Document:
		"""@access public Q_SLOTS
 @return the currently active document, if there is one. """

	def setActiveDocument(self, value: 'Document') -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setActiveDocument activates the first view that shows the given document
@param value the document we want to activate """

	def batchmode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief batchmode determines whether the script is run in batch mode. If batchmode is true, scripts should now show messageboxes or dialog boxes. Note that this separate from Document.setBatchmode(), which determines whether export/save option dialogs are shown.
@return true if the script is run in batchmode """

	def setBatchmode(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setBatchmode sets the batchmode to @param value; if true, scripts should not show dialogs or messageboxes. """

	def actions(self) -> List[QAction]:
		# type: () -> List[QAction]:
		"""@access public Q_SLOTS
 @return return a list of all actions for the currently active mainWindow. """

	def action(self, name: str) -> QAction:
		# type: (name) -> QAction:
		"""@access public Q_SLOTS
 @return the action that has been registered under the given name, or 0 if no such action exists. """

	def documents(self) -> List['Document']:
		# type: () -> List[Document]:
		"""@access public Q_SLOTS
 @return a list of all open Documents """

	def dockers(self) -> List[QDockWidget]:
		# type: () -> List[QDockWidget]:
		"""@access public Q_SLOTS
 @return a list of all the dockers """

	def filters(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief Filters are identified by an internal name. This function returns a list of all existing registered filters.
@return a list of all registered filters """

	def filter(self, name: str) -> 'Filter':
		# type: (name) -> Filter:
		"""@access public Q_SLOTS
 @brief filter construct a Filter object with a default configuration.
@param name the name of the filter. Use Krita.instance().filters() to get a list of all possible filters.
@return the filter or None if there is no such filter. """

	def colorModels(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief colorModels creates a list with all color models id's registered.
@return a list of all color models or a empty list if there is no such color models. """

	def colorDepths(self, colorModel: str) -> List[str]:
		# type: (colorModel) -> List[str]:
		"""@access public Q_SLOTS
 @brief colorDepths creates a list with the names of all color depths compatible with the given color model.
@param colorModel the id of a color model.
@return a list of all color depths or a empty list if there is no such color depths. """

	def filterStrategies(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief filterStrategies Retrieves all installed filter strategies. A filter strategy is used when transforming (scaling, shearing, rotating) an image to calculate the value of the new pixels. You can use th
@return the id's of all available filters. """

	def profiles(self, colorModel: str, colorDepth: str) -> List[str]:
		# type: (colorModel, colorDepth) -> List[str]:
		"""@access public Q_SLOTS
 @brief profiles creates a list with the names of all color profiles compatible with the given color model and color depth.
@param colorModel A string describing the color model of the image: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@param colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@return a list with valid names """

	def addProfile(self, profilePath: str) -> bool:
		# type: (profilePath) -> bool:
		"""@access public Q_SLOTS
 @brief addProfile load the given profile into the profile registry.
@param profilePath the path to the profile.
@return true if adding the profile succeeded. """

	def notifier(self) -> 'Notifier':
		# type: () -> Notifier:
		"""@access public Q_SLOTS
 @brief notifier the Notifier singleton emits signals when documents are opened and closed, the configuration changes, views are opened and closed or windows are opened.
@return the notifier object """

	def version(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief version Determine the version of Krita Usage: print(Application.version ())
@return the version string including git sha1 if Krita was built from git """

	def views(self) -> List['View']:
		# type: () -> List[View]:
		"""@access public Q_SLOTS
 @return a list of all views. A Document can be shown in more than one view. """

	def activeWindow(self) -> 'Window':
		# type: () -> Window:
		"""@access public Q_SLOTS
 @return the currently active window or None if there is no window """

	def windows(self) -> List['Window']:
		# type: () -> List[Window]:
		"""@access public Q_SLOTS
 @return a list of all windows """

	def resources(self, type: str) -> Dict[str, 'Resource']:
		# type: (type) -> Dict[str, Resource]:
		"""@access public Q_SLOTS
 @brief resources returns a list of Resource objects of the given type
@param type Valid types are: <ul> <li>pattern</li> <li>gradient</li> <li>brush</li> <li>preset</li> <li>palette</li> <li>workspace</li> </ul> """

	def recentDocuments(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief return all recent documents registered in the RecentFiles group of the kritarc """

	def createDocument(self, width: int, height: int, name: str, colorModel: str, colorDepth: str, profile: str, resolution: float) -> 'Document':
		# type: (width, height, name, colorModel, colorDepth, profile, resolution) -> Document:
		"""@access public Q_SLOTS
 @brief createDocument creates a new document and image and registers the document with the Krita application. Unless you explicitly call Document::close() the document will remain known to the Krita document registry. The document and its image will only be deleted when Krita exits. The document will have one transparent layer. To create a new document and show it, do something like:
@code
from Krita import *

def add_document_to_window():
    d = Application.createDocument(100, 100, "Test", "RGBA", "U8", "", 120.0)
    Application.activeWindow().addView(d)

add_document_to_window()
@endcode
@param width the width in pixels
@param height the height in pixels
@param name the name of the image (not the filename of the document)
@param colorModel A string describing the color model of the image: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@param colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@param profile The name of an icc profile that is known to Krita. If an empty string is passed, the default is taken.
@param resolution the resolution in points per inch.
@return the created document. """

	def openDocument(self, filename: str) -> 'Document':
		# type: (filename) -> Document:
		"""@access public Q_SLOTS
 @brief openDocument creates a new Document, registers it with the Krita application and loads the given file.
@param filename the file to open in the document
@return the document """

	def openWindow(self) -> 'Window':
		# type: () -> Window:
		"""@access public Q_SLOTS
 @brief openWindow create a new main window. The window is not shown by default. """

	def addExtension(self, extension: 'Extension') -> None:
		# type: (extension) -> None:
		"""@access public Q_SLOTS
 @brief addExtension add the given plugin to Krita. There will be a single instance of each Extension in the Krita process.
@param extension the extension to add. """

	def extensions(self) -> List['Extension']:
		# type: () -> List[Extension]:
		"""@access public Q_SLOTS
 return a list with all registered extension objects. """

	def addDockWidgetFactory(self, factory: 'DockWidgetFactoryBase') -> None:
		# type: (factory) -> None:
		"""@access public Q_SLOTS
 @brief addDockWidgetFactory Add the given docker factory to the application. For scripts loaded on startup, this means that every window will have one of the dockers created by the factory.
@param factory The factory object. """

	def writeSetting(self, group: str, name: str, value: str) -> None:
		# type: (group, name, value) -> None:
		"""@access public Q_SLOTS
 @brief writeSetting write the given setting under the given name to the kritarc file in the given settings group.
@param group The group the setting belongs to. If empty, then the setting is written in the general section
@param name The name of the setting
@param value The value of the setting. Script settings are always written as strings. """

	def readSetting(self, group: str, name: str, defaultValue: str) -> str:
		# type: (group, name, defaultValue) -> str:
		"""@access public Q_SLOTS
 @brief readSetting read the given setting value from the kritarc file.
@param group The group the setting is part of. If empty, then the setting is read from the general group.
@param name The name of the setting
@param defaultValue The default value of the setting
@return a string representing the setting. """

	def icon(self, iconName: str) -> QIcon:
		# type: (iconName) -> QIcon:
		"""@access public Q_SLOTS
 @brief icon This allows you to get icons from Krita's internal icons.
@param iconName name of the icon.
@return the icon related to this name. """

	@staticmethod
	def instance() ->  'Krita':
		# type: () ->  Krita:
		"""@access public Q_SLOTS
 @brief instance retrieve the singleton instance of the Application object. """

	def mainWindowIsBeingCreated(self, window: 'KisMainWindow') -> None:
		# type: (window) -> None:
		"""@access private Q_SLOTS
This is called from the constructor of the window, before the xmlgui file is loaded """

class IntParseSpinBox(QObject):
	"""* @brief A wrapper around KisIntParseSpinBox, which is a cleverer SpinBox, able to parse arithmetic expressions. The widget itself is accessed with the widget() function. Use this spinbox instead of the basic one from Qt if you want it to be able to parse arithmetic expressions. """

	def widget(self) -> QSpinBox:
		# type: () -> QSpinBox:
		"""@access public Q_SLOTS
 @brief Get the internal KisIntParseSpinBox as a QWidget, so it may be added to a UI
@return the internal KisIntParseSpinBox as a QWidget """

	def stepBy(self, steps: int) -> None:
		# type: (steps) -> None:
		"""@access public Q_SLOTS
 @brief This is a reimplementation of @ref QSpinBox::stepBy that uses @ref setValue
@param steps Number of steps that the value should change """

	def setValue(self, value: int, overwriteExpression: bool = False) -> None:
		# type: (value, overwriteExpression) -> None:
		"""@access public Q_SLOTS
 @brief Set the value of the spinbox  This reimplementation also tries to clear the current expression and warning message whenever possible. This will happen when the new value is different from the current one and the line edit has not the focus or it is read-only. One can force the reset also by passing true to the
@p overwriteExpression parameter.
@param value The new value
@param overwriteExpression Get if the expression in the edit field (and the warning message) should be reset to reflect the new value. The default is false so that if the user is editing the expression it won't be disrupted by any default call to this function """

	def isLastValid(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Get if the last expression entered is a valid one
@retval true if the last expression entered is valid
@retval false otherwise """

	def veryCleanText(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief This virtual function is similar to cleanText(). But child classes may reimplement it to further process ("clean up") the expression.
@return The processed expression """

	def errorWhileParsing(self, expr: str) -> None:
		# type: (expr) -> None:
		"""@access public Q_SLOTS
 @brief signal emitted when the last parsed expression is not valid. """

	def noMoreParsingError(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief signal emitted when the last parsed expression is valid and the expression before was not valid. """

class InfoObject(QObject):
	"""* InfoObject wrap a properties map. These maps can be used to set the configuration for filters. """

	def __init__(self) -> None:
		""" @brief signal emitted when the last parsed expression is valid and the expression before was not valid. """

	def properties(self) -> Dict[str, QVariant]:
		# type: () -> Dict[str, QVariant]:
		"""@access public
 Return all properties this InfoObject manages. """

	def setProperties(self, propertyMap: Dict[str, QVariant]) -> None:
		# type: (propertyMap) -> None:
		"""@access public
 Add all properties in the @p propertyMap to this InfoObject """

	def setProperty(self, key: str, value: QVariant) -> None:
		# type: (key, value) -> None:
		"""@access public Q_SLOTS
 set the property identified by @p key to @p value If you want create a property that represents a color, you can use a QColor or hex string, as defined in https://doc.qt.io/qt-5/qcolor.html#setNamedColor. """

	def property(self, key: str) -> QVariant:
		# type: (key) -> QVariant:
		"""@access public Q_SLOTS
 return the value for the property identified by key, or None if there is no such key. """

	def configuration(self) -> 'KisPropertiesConfigurationSP':
		# type: () -> 'KisPropertiesConfigurationSP':
		"""@access private
 @brief configuration gives access to the internal configuration object. Must be used internally in libkis
@return the internal configuration object. """

class GuidesConfig(QObject):
	"""* The GuidesConfig class encapsulates a Krita Guides configuration. """

	def __init__(self) -> 'KisPropertiesConfigurationSP':
		""" @brief configuration gives access to the internal configuration object. Must be used internally in libkis
@return the internal configuration object. """

	def color(self) -> QColor:
		# type: () -> QColor:
		"""@access public Q_SLOTS
 @brief Guides color
@return color applied for all guides """

	def setColor(self, color: QColor) -> None:
		# type: (color) -> None:
		"""@access public Q_SLOTS
 @brief Define guides color
@param color color to apply """

	def lineType(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Guides line type
@return line type applied for all guides Can be: - "solid" - "dashed" - "dot" """

	def setLineType(self, lineType: str) -> None:
		# type: (lineType) -> None:
		"""@access public Q_SLOTS
 @brief Define guides lines type
@param lineType line type to use for guides: Can be: - "solid" - "dashed" - "dot" """

	def hasGuides(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief indicate if there's guides defined
@return True if at least one guide is defined, otherwise False """

	def hasSamePositionAs(self, guideConfig: 'GuidesConfig') -> bool:
		# type: (guideConfig) -> bool:
		"""@access public Q_SLOTS
 @brief indicate if position from current guides configuration match positions from another guides configuration
@return True if positions are the same """

	def horizontalGuides(self) -> List[float]:
		# type: () -> List[float]:
		"""@access public Q_SLOTS
 @brief The horizontal guides.
@return a list of the horizontal positions of guides. """

	def setHorizontalGuides(self, lines: List[float]) -> None:
		# type: (lines) -> None:
		"""@access public Q_SLOTS
 @brief Set the horizontal guides.
@param lines a list of the horizontal positions of guides to set """

	def verticalGuides(self) -> List[float]:
		# type: () -> List[float]:
		"""@access public Q_SLOTS
 @brief The vertical guides.
@return a list of vertical positions of guides. """

	def setVerticalGuides(self, lines: List[float]) -> None:
		# type: (lines) -> None:
		"""@access public Q_SLOTS
 @brief Set the vertical guides.
@param lines a list of the vertical positions of guides to set """

	def fromXml(self, xmlContent: str) -> bool:
		# type: (xmlContent) -> bool:
		"""@access public Q_SLOTS
 @brief Load guides definition from an XML document
@param xmlContent xml content provided as a string
@return True if xml content is valid and guides has been loaded, otherwise False """

	def toXml(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Save guides definition as an XML document
@return A string with xml content """

	def removeAllGuides(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Remove all guides """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns guides visibility status.
@return True if guides are visible, otherwise False """

	def setVisible(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief Set guides visibility status
@param value True to set guides visible, otherwise False """

	def locked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns guide lock status
@return True if guides are locked, otherwise False """

	def setLocked(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief Set guides lock status
@param value True to set guides locked, otherwise False """

	def snap(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns guide snap status
@return True if snap to guides is active, otherwise False """

	def setSnap(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief Set guides snap status
@param value True to set snap to guides active, otherwise False """

class GridConfig(QObject):
	"""* The GridConfig class encapsulates a Krita Guides configuration. """

	def __init__(self, value: bool) -> None:
		""" @brief Set guides snap status
@param value True to set snap to guides active, otherwise False """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns grid visibility for document.
@return If grid is visible, return True. """

	def setVisible(self, visible: bool) -> None:
		# type: (visible) -> None:
		"""@access public Q_SLOTS
 @brief Set grid visibility for document.
@param snap Set to True to get grid visible. """

	def snap(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns snap to grid status for document.
@return If snap to grid is active on document, return True. """

	def setSnap(self, snap: bool) -> None:
		# type: (snap) -> None:
		"""@access public Q_SLOTS
 @brief Activate or deactivate snap to grid for document
@param snap Set to True to activate snap to grid. """

	def offset(self) -> QPoint:
		# type: () -> QPoint:
		"""@access public Q_SLOTS
 @brief Returns grid offset (in pixels, from origin) for document.
@return A QPoint that define X and Y offset. """

	def setOffset(self, offset: QPoint) -> None:
		# type: (offset) -> None:
		"""@access public Q_SLOTS
 @brief Define grid offset (in pixels, from origin) for document.
@param offset A QPoint that define X and Y offset (X and Y in range [0 - 500]) """

	def spacing(self) -> QPoint:
		# type: () -> QPoint:
		"""@access public Q_SLOTS
 @brief Returns grid spacing (in pixels) for document. Spacing value is used for grid type "rectangular".
@return A QPoint that define X and Y spacing. """

	def setSpacing(self, spacing: QPoint) -> None:
		# type: (spacing) -> None:
		"""@access public Q_SLOTS
 @brief Set grid spacing (in pixels) for document. Spacing value is used for grid type "rectangular".
@param spacing A QPoint that define X and Y spacing  (minimum value for X and Y is 1) """

	def spacingActiveHorizontal(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns if horizontal grid spacing is active. Spacing value is used for grid type "rectangular".
@returns a boolean which indicate if horizontal grid is active or not """

	def setSpacingActiveHorizontal(self, active: bool) -> None:
		# type: (active) -> None:
		"""@access public Q_SLOTS
 @brief Set horizontal grid spacing active. Spacing value is used for grid type "rectangular".
@param active True to activate horizontal spacing, False to deactivate it. """

	def spacingActiveVertical(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns if vertical grid spacing is active. Spacing value is used for grid type "rectangular".
@returns a boolean which indicate if vertical grid is active or not """

	def setSpacingActiveVertical(self, active: bool) -> None:
		# type: (active) -> None:
		"""@access public Q_SLOTS
 @brief Set vertical grid spacing active. Spacing value is used for grid type "rectangular".
@param active True to activate vertical spacing, False to deactivate it. """

	def subdivision(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Returns number of grid subdivision for document. Subdivision value is used for grid type "rectangular".
@return A positive integer value, starting from 1 """

	def setSubdivision(self, subdivision: int) -> None:
		# type: (subdivision) -> None:
		"""@access public Q_SLOTS
 @brief Set number of grid subdivision for document. Subdivision value is used for grid type "rectangular".
@param subdivision A positive integer value, in range [1 - 10] """

	def angleLeft(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Returns left angle (in degrees) of isometric grid for document. AngleLeft value is used for grid type "isometric".
@return A positive decimal value, in range [0.00 - 89.00] """

	def setAngleLeft(self, angleLeft: float) -> None:
		# type: (angleLeft) -> None:
		"""@access public Q_SLOTS
 @brief Set left angle (in degrees) of isometric grid for document. AngleLeft value is used for grid type "isometric".
@param angleLeft A positive decimal value, in range [0.00 - 89.00] """

	def angleRight(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Returns right angle (in degrees) of isometric grid for document. AngleRight value is used for grid type "isometric".
@return A positive decimal value, in range [0.00 - 89.00] """

	def setAngleRight(self, angleRight: float) -> None:
		# type: (angleRight) -> None:
		"""@access public Q_SLOTS
 @brief Set right angle (in degrees) of isometric grid for document. AngleRight value is used for grid type "isometric".
@param angleRight A positive decimal value, in range [0.00 - 89.00] """

	def angleLeftActive(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns if left angle grid is active. Spacing value is used for grid type "isometric".
@returns a boolean which indicate if left angle grid is active or not """

	def setAngleLeftActive(self, active: bool) -> None:
		# type: (active) -> None:
		"""@access public Q_SLOTS
 @brief Set left angle grid active. Spacing value is used for grid type "isometric".
@param active True to activate left angle grid, False to deactivate it. """

	def angleRightActive(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns if right angle grid is active. Spacing value is used for grid type "isometric".
@returns a boolean which indicate if right angle grid is active or not """

	def setAngleRightActive(self, active: bool) -> None:
		# type: (active) -> None:
		"""@access public Q_SLOTS
 @brief Set right angle grid active. Spacing value is used for grid type "isometric".
@param active True to activate right angle grid, False to deactivate it. """

	def cellSpacing(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Returns grid cell spacing (in pixels) for document. Cell spacing value is used for grid type "isometric_legacy".
@return A positive integer value, minimum value is 10 """

	def setCellSpacing(self, cellSpacing: int) -> None:
		# type: (cellSpacing) -> None:
		"""@access public Q_SLOTS
 @brief Set grid cell spacing for document. Cell spacing value is used for grid type "isometric_legacy".
@param cellSpacing A integer that define spacing, in range [10 - 1000] """

	def cellSize(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Returns grid cell border size (in pixels) for document. Cell spacing value is used for grid type "isometric".
@return A positive integer value, in range [10 - 1000] """

	def setCellSize(self, cellSize: int) -> None:
		# type: (cellSize) -> None:
		"""@access public Q_SLOTS
 @brief Set grid cell size (in pixels) for document. Cell spacing value is used for grid type "isometric".
@param cellSize An integer that define cell border size. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Returns current grid type applied for document.
@return The grid type can be: - "rectangular" - "isometric" - "isometric_legacy" """

	def setType(self, gridType: str) -> None:
		# type: (gridType) -> None:
		"""@access public Q_SLOTS
 @brief Set current grid type applied for document.
@param gridType The grid type can be: - "rectangular" - "isometric" - "isometric_legacy" """

	def offsetAspectLocked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns status of "Aspect locked" property for offset values (X and Y values are linked to keep ratio)
@return If locked, return True. """

	def setOffsetAspectLocked(self, offsetAspectLocked: bool) -> None:
		# type: (offsetAspectLocked) -> None:
		"""@access public Q_SLOTS
 @brief Set status of "Aspect locked" property for offset values (X and Y values are linked to keep ratio)
@param offsetAspectLocked Set to True lock aspect. """

	def spacingAspectLocked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns status of "Aspect locked" property for spacing values (mean, X and Y values are linked to keep ratio) SpacingAspectLocked value is used for grid type "rectangular".
@return If locked, return True. """

	def setSpacingAspectLocked(self, spacingAspectLocked: bool) -> None:
		# type: (spacingAspectLocked) -> None:
		"""@access public Q_SLOTS
 @brief Set status of "Aspect locked" property for spacing values (X and Y values are linked to keep ratio) SpacingAspectLocked value is used for grid type "rectangular".
@param spacingAspectLocked Set to True lock aspect. """

	def angleAspectLocked(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Returns status of "Aspect locked" property for angles values (mean, left and right angles values are linked to keep ratio) AngleAspectLocked value is used for grid type "isometric" and "isometric_legacy".
@return If locked, return True. """

	def setAngleAspectLocked(self, angleAspectLocked: bool) -> None:
		# type: (angleAspectLocked) -> None:
		"""@access public Q_SLOTS
 @brief Set status of "Aspect locked" property for angles values (left and right angles values are linked to keep ratio) AngleAspectLocked value is used for grid type "isometric" and "isometric_legacy".
@param angleAspectLocked Set to True lock aspect. """

	def lineTypeMain(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Returns grid main line type
@return The main line type for grid in current document Can be: - "solid" - "dashed" - "dotted" """

	def setLineTypeMain(self, lineType: str) -> None:
		# type: (lineType) -> None:
		"""@access public Q_SLOTS
 @brief Set grid main line type
@param lineType The main line type to apply for grid Can be: - "solid" - "dashed" - "dotted" """

	def lineTypeSubdivision(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Returns grid subdivision line type
@return The subdivision line type for grid in current document Can be: - "solid" - "dashed" - "dotted" LineTypeSubdivision value is used for grid type "rectangular". """

	def setLineTypeSubdivision(self, lineType: str) -> None:
		# type: (lineType) -> None:
		"""@access public Q_SLOTS
 @brief Set grid subdivision line type
@param lineType The subdivision line type to apply for grid Can be: - "solid" - "dashed" - "dotted" LineTypeSubdivision value is used for grid type "rectangular". """

	def lineTypeVertical(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Returns grid vertical line type
@return The vertical line type for grid in current document Can be: - "solid" - "dashed" - "dotted" - "none" LineTypeVertical value is used for grid type "isometric". """

	def setLineTypeVertical(self, lineType: str) -> None:
		# type: (lineType) -> None:
		"""@access public Q_SLOTS
 @brief Set grid vertical line type
@param lineType The vertical line type to apply for grid Can be: - "solid" - "dashed" - "dotted" - "none" LineTypeVertical value is used for grid type "isometric". """

	def colorMain(self) -> QColor:
		# type: () -> QColor:
		"""@access public Q_SLOTS
 @brief Returns grid main line color
@return The color for grid main line """

	def setColorMain(self, colorMain: QColor) -> None:
		# type: (colorMain) -> None:
		"""@access public Q_SLOTS
 @brief Set grid main line color
@param color The color to apply for grid main line """

	def colorSubdivision(self) -> QColor:
		# type: () -> QColor:
		"""@access public Q_SLOTS
 @brief Returns grid subdivision line color ColorSubdivision value is used for grid type "rectangular".
@return The color for grid subdivision line """

	def setColorSubdivision(self, colorSubdivision: QColor) -> None:
		# type: (colorSubdivision) -> None:
		"""@access public Q_SLOTS
 @brief Set grid subdivision line color ColorSubdivision value is used for grid type "rectangular".
@param color The color to apply for grid subdivision line """

	def colorVertical(self) -> QColor:
		# type: () -> QColor:
		"""@access public Q_SLOTS
 @brief Returns grid vertical line color ColorSubdivision value is used for grid type "isometric".
@return The color for grid vertical line """

	def setColorVertical(self, colorVertical: QColor) -> None:
		# type: (colorVertical) -> None:
		"""@access public Q_SLOTS
 @brief Set grid vertical line color ColorSubdivision value is used for grid type "isometric".
@param color The color to apply for grid vertical line """

	def fromXml(self, xmlContent: str) -> bool:
		# type: (xmlContent) -> bool:
		"""@access public Q_SLOTS
 @brief Load grid definition from an XML document
@param xmlContent xml content provided as a string
@return True if xml content is valid and grid has been loaded, otherwise False """

	def toXml(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Save grid definition as an XML document
@return A string with xml content """

class Filter(QObject):
	"""* Filter: represents a filter and its configuration. A filter is identified by an internal name. The configuration for each filter is defined as an InfoObject: a map of name and value pairs. Currently available filters are: 'autocontrast', 'blur', 'bottom edge detections', 'brightnesscontrast', 'burn', 'colorbalance', 'colortoalpha', 'colortransfer', 'desaturate', 'dodge', 'emboss', 'emboss all directions', 'emboss horizontal and vertical', 'emboss horizontal only', 'emboss laplascian', 'emboss vertical only', 'gaussian blur', 'gaussiannoisereducer', 'gradientmap', 'halftone', 'hsvadjustment', 'indexcolors', 'invert', 'left edge detections', 'lens blur', 'levels', 'maximize', 'mean removal', 'minimize', 'motion blur', 'noise', 'normalize', 'oilpaint', 'perchannel', 'phongbumpmap', 'pixelize', 'posterize', 'raindrops', 'randompick', 'right edge detections', 'roundcorners', 'sharpen', 'smalltiles', 'sobel', 'threshold', 'top edge detections', 'unsharp', 'wave', 'waveletnoisereducer'] """

	def __init__(self) -> str:
		""" @brief Save grid definition as an XML document
@return A string with xml content """

	def name(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief name the internal name of this filter.
@return the name. """

	def setName(self, name: str) -> None:
		# type: (name) -> None:
		"""@access public Q_SLOTS
 @brief setName set the filter's name to the given name. """

	def configuration(self) -> 'InfoObject':
		# type: () -> InfoObject:
		"""@access public Q_SLOTS
 @return the configuration object for the filter """

	def setConfiguration(self, value: 'InfoObject') -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setConfiguration set the configuration object for the filter """

	def apply(self, node: 'Node', x: int, y: int, w: int, h: int) -> bool:
		# type: (node, x, y, w, h) -> bool:
		"""@access public Q_SLOTS
 @brief Apply the filter to the given node.
@param node the node to apply the filter to
@param x
@param y
@param w
@param h describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node.
@return @c true if the filter was applied successfully, or
@c false if the filter could not be applied because the node is locked or does not have an editable paint device. """

	def startFilter(self, node: 'Node', x: int, y: int, w: int, h: int) -> bool:
		# type: (node, x, y, w, h) -> bool:
		"""@access public Q_SLOTS
 @brief startFilter starts the given filter on the given node.
@param node the node to apply the filter to
@param x
@param y
@param w
@param h describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node. """

class Extension(QObject):
	"""* An Extension is the base for classes that extend Krita. An Extension is loaded on startup, when the setup() method will be executed. The extension instance should be added to the Krita Application object using Krita.instance().addViewExtension or Application.addViewExtension or Scripter.addViewExtension. Example:
@code
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from krita import *
class HelloExtension(Extension):
def __init__(self, parent):
    super().__init__(parent)
def hello(self):
    QMessageBox.information(QWidget(), "Test", "Hello! This is Krita " + Application.version())
def setup(self):
    qDebug("Hello Setup")
def createActions(self, window)
    action = window.createAction("hello")
    action.triggered.connect(self.hello)
Scripter.addExtension(HelloExtension(Krita.instance()))
@endcode """

class DoubleParseSpinBox(QObject):
	"""* @brief A wrapper around KisDoubleParseSpinBox, which is a cleverer doubleSpinBox, able to parse arithmetic expressions. The widget itself is accessed with the widget() function. Use this spinbox instead of the basic one from Qt if you want it to be able to parse arithmetic expressions. """

	def widget(self) -> QDoubleSpinBox:
		# type: () -> QDoubleSpinBox:
		"""@access public Q_SLOTS
 @brief Get the internal KisDoubleParseSpinBox as a QWidget, so it may be added to a UI
@return the internal KisDoubleParseSpinBox as a QWidget """

	def stepBy(self, steps: int) -> None:
		# type: (steps) -> None:
		"""@access public Q_SLOTS
 @brief This is a reimplementation of @ref QDoubleSpinBox::stepBy that uses @ref setValue
@param steps Number of steps that the value should change """

	def setValue(self, value: float, overwriteExpression: bool = False) -> None:
		# type: (value, overwriteExpression) -> None:
		"""@access public Q_SLOTS
 @brief Set the value of the spinbox  This reimplementation also tries to clear the current expression and warning message whenever possible. This will happen when the new value is different from the current one and the line edit has not the focus or it is read-only. One can force the reset also by passing true to the
@p overwriteExpression parameter.
@param value The new value
@param overwriteExpression Get if the expression in the edit field (and the warning message) should be reset to reflect the new value. The default is false so that if the user is editing the expression it won't be disrupted by any default call to this function """

	def isLastValid(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Get if the last expression entered is a valid one
@retval true if the last expression entered is valid
@retval false otherwise """

	def veryCleanText(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief This virtual function is similar to cleanText(). But child classes may reimplement it to further process ("clean up") the expression.
@return The processed expression """

	def errorWhileParsing(self, expr: str) -> None:
		# type: (expr) -> None:
		"""@access public Q_SLOTS
 @brief signal emitted when the last parsed expression is not valid. """

	def noMoreParsingError(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief signal emitted when the last parsed expression is valid and the expression before was not valid. """

class Document(QObject):
	"""* The Document class encapsulates a Krita Document/Image. A Krita document is an Image with a filename. Libkis does not differentiate between a document and an image, like Krita does internally. """

	def __init__(self) -> None:
		""" @brief signal emitted when the last parsed expression is valid and the expression before was not valid. """

	def clone(self) -> 'Document':
		# type: () -> Document:
		"""@access public Q_SLOTS
 @brief DEPRECATED - use guidesConfig() instead The horizontal guides.
@return a list of the horizontal positions of guides./
    Q_DECL_DEPRECATED QList<qreal> horizontalGuides() const;
    /**
@brief DEPRECATED - use guidesConfig() instead The vertical guide lines.
@return a list of vertical guides./
    Q_DECL_DEPRECATED QList<qreal> verticalGuides() const;

    /**
@brief DEPRECATED - use guidesConfig() instead Returns guide visibility.
@return whether the guides are visible./
    Q_DECL_DEPRECATED bool guidesVisible() const;
    /**
@brief DEPRECATED - use guidesConfig() instead Returns guide lockedness.
@return whether the guides are locked./
    Q_DECL_DEPRECATED bool guidesLocked() const;

    /**
@brief clone create a shallow clone of this document.
@return a new Document that should be identical to this one in every respect. """

	def batchmode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 Batchmode means that no actions on the document should show dialogs or popups.
@return true if the document is in batchmode. """

	def setBatchmode(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 Set batchmode to @p value. If batchmode is true, then there should be no popups or dialogs shown to the user. """

	def activeNode(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief activeNode retrieve the node that is currently active in the currently active window
@return the active node. If there is no active window, the first child node is returned. """

	def setActiveNode(self, value: 'Node') -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setActiveNode make the given node active in the currently active view and window
@param value the node to make active. """

	def topLevelNodes(self) -> List['Node']:
		# type: () -> List[Node]:
		"""@access public Q_SLOTS
 @brief toplevelNodes return a list with all top level nodes in the image graph """

	def nodeByName(self, name: str) -> 'Node':
		# type: (name) -> Node:
		"""@access public Q_SLOTS
 @brief nodeByName searches the node tree for a node with the given name and returns it
@param name the name of the node
@return the first node with the given name or 0 if no node is found """

	def nodeByUniqueID(self, id: QUuid) -> 'Node':
		# type: (id) -> Node:
		"""@access public Q_SLOTS
 @brief nodeByUniqueID searches the node tree for a node with the given name and returns it.
@param uuid the unique id of the node
@return the node with the given unique id, or 0 if no node is found. """

	def colorDepth(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@return the color depth. """

	def colorModel(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief colorModel retrieve the current color model of this document: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@return the internal color model string. """

	def colorProfile(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the name of the current color profile """

	def setColorProfile(self, colorProfile: str) -> bool:
		# type: (colorProfile) -> bool:
		"""@access public Q_SLOTS
 @brief setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is <i>not</i> converted.
@param colorProfile
@return false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed. """

	def setColorSpace(self, colorModel: str, colorDepth: str, colorProfile: str) -> bool:
		# type: (colorModel, colorDepth, colorProfile) -> bool:
		"""@access public Q_SLOTS
 @brief setColorSpace convert the nodes and the image to the given colorspace. The conversion is done with Perceptual as intent, High Quality and No LCMS Optimizations as flags and no blackpoint compensation.
@param colorModel A string describing the color model of the image: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul>
@param colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul>
@param colorProfile a valid color profile for this color model and color depth combination.
@return false the combination of these arguments does not correspond to a colorspace. """

	def backgroundColor(self) -> QColor:
		# type: () -> QColor:
		"""@access public Q_SLOTS
 @brief backgroundColor returns the current background color of the document. The color will also include the opacity.
@return QColor """

	def setBackgroundColor(self, color: QColor) -> bool:
		# type: (color) -> bool:
		"""@access public Q_SLOTS
 @brief setBackgroundColor sets the background color of the document. It will trigger a projection update.
@param color A QColor. The color will be converted from sRGB.
@return bool """

	def documentInfo(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief documentInfo creates and XML document representing document and author information.
@return a string containing a valid XML document with the right information about the document and author. The DTD can be found here: https://phabricator.kde.org/source/krita/browse/master/krita/dtd/
@code
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE document-info PUBLIC '-//KDE//DTD document-info 1.1//EN' 'http://www.calligra.org/DTD/document-info-1.1.dtd'>
<document-info xmlns="http://www.calligra.org/DTD/document-info">
<about>
 <title>My Document</title>
  <description></description>
  <subject></subject>
  <abstract><![CDATA[]]></abstract>
  <keyword></keyword>
  <initial-creator>Unknown</initial-creator>
  <editing-cycles>1</editing-cycles>
  <editing-time>35</editing-time>
  <date>2017-02-27T20:15:09</date>
  <creation-date>2017-02-27T20:14:33</creation-date>
  <language></language>
 </about>
 <author>
  <full-name>Boudewijn Rempt</full-name>
  <initial></initial>
  <author-title></author-title>
  <email></email>
  <telephone></telephone>
  <telephone-work></telephone-work>
  <fax></fax>
  <country></country>
  <postal-code></postal-code>
  <city></city>
  <street></street>
  <position></position>
  <company></company>
 </author>
</document-info>
@endcode """

	def setDocumentInfo(self, document: str) -> None:
		# type: (document) -> None:
		"""@access public Q_SLOTS
 @brief setDocumentInfo set the Document information to the information contained in document
@param document A string containing a valid XML document that conforms to the document-info DTD that can be found here: https://phabricator.kde.org/source/krita/browse/master/krita/dtd/ """

	def fileName(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the full path to the document, if it has been set. """

	def setFileName(self, value: str) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setFileName set the full path of the document to @param value """

	def height(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the height of the image in pixels """

	def setHeight(self, value: int) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setHeight resize the document to @param value height. This is a canvas resize, not a scale. """

	def name(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @return the name of the document. This is the title field in the @ref documentInfo """

	def setName(self, value: str) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setName sets the name of the document to @p value. This is the title field in the @ref documentInfo """

	def resolution(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the resolution in pixels per inch """

	def setResolution(self, value: int) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setResolution set the resolution of the image; this does not scale the image
@param value the resolution in pixels per inch """

	def rootNode(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief rootNode the root node is the invisible group layer that contains the entire node hierarchy.
@return the root of the image """

	def selection(self) -> 'Selection':
		# type: () -> Selection:
		"""@access public Q_SLOTS
 @brief selection Create a Selection object around the global selection, if there is one.
@return the global selection or None if there is no global selection. """

	def setSelection(self, value: 'Selection') -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setSelection set or replace the global selection
@param value a valid selection object. """

	def width(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the width of the image in pixels. """

	def setWidth(self, value: int) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setWidth resize the document to @param value width. This is a canvas resize, not a scale. """

	def xOffset(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the left edge of the canvas in pixels. """

	def setXOffset(self, x: int) -> None:
		# type: (x) -> None:
		"""@access public Q_SLOTS
 @brief setXOffset sets the left edge of the canvas to @p x. """

	def yOffset(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @return the top edge of the canvas in pixels. """

	def setYOffset(self, y: int) -> None:
		# type: (y) -> None:
		"""@access public Q_SLOTS
 @brief setYOffset sets the top edge of the canvas to @p y. """

	def xRes(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return xRes the horizontal resolution of the image in pixels per inch """

	def setXRes(self, xRes: float) -> None:
		# type: (xRes) -> None:
		"""@access public Q_SLOTS
 @brief setXRes set the horizontal resolution of the image to xRes in pixels per inch """

	def yRes(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return yRes the vertical resolution of the image in pixels per inch """

	def setYRes(self, yRes: float) -> None:
		# type: (yRes) -> None:
		"""@access public Q_SLOTS
 @brief setYRes set the vertical resolution of the image to yRes in pixels per inch """

	def pixelData(self, x: int, y: int, w: int, h: int) -> QByteArray:
		# type: (x, y, w, h) -> QByteArray:
		"""@access public Q_SLOTS
 @brief pixelData reads the given rectangle from the image projection and returns it as a byte array. The pixel data starts top-left, and is ordered row-first. The byte array can be interpreted as follows: 8 bits images have one byte per channel, and as many bytes as there are channels. 16 bits integer images have two bytes per channel, representing an unsigned short. 16 bits float images have two bytes per channel, representing a half, or 16 bits float. 32 bits float images have four bytes per channel, representing a float. You can read outside the image boundaries; those pixels will be transparent black. The order of channels is: <ul> <li>Integer RGBA: Blue, Green, Red, Alpha <li>Float RGBA: Red, Green, Blue, Alpha <li>LabA: L, a, b, Alpha <li>CMYKA: Cyan, Magenta, Yellow, Key, Alpha <li>XYZA: X, Y, Z, A <li>YCbCrA: Y, Cb, Cr, Alpha </ul> The byte array is a copy of the original image data. In Python, you can use bytes, bytearray and the struct module to interpret the data and construct, for instance, a Pillow Image object.
@param x x position from where to start reading
@param y y position from where to start reading
@param w row length to read
@param h number of rows to read
@return a QByteArray with the pixel data. The byte array may be empty. """

	def close(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief close Close the document: remove it from Krita's internal list of documents and close all views. If the document is modified, you should save it first. There will be no prompt for saving. After closing the document it becomes invalid.
@return true if the document is closed. """

	def crop(self, x: int, y: int, w: int, h: int) -> None:
		# type: (x, y, w, h) -> None:
		"""@access public Q_SLOTS
 @brief crop the image to rectangle described by @p x, @p y,
@p w and @p h
@param x x coordinate of the top left corner
@param y y coordinate of the top left corner
@param w width
@param h height """

	def exportImage(self, filename: str, exportConfiguration: 'InfoObject') -> bool:
		# type: (filename, exportConfiguration) -> bool:
		"""@access public Q_SLOTS
 @brief exportImage export the image, without changing its URL to the given path.
@param filename the full path to which the image is to be saved
@param exportConfiguration a configuration object appropriate to the file format. An InfoObject will used to that configuration. The supported formats have specific configurations that must be used when in batchmode. They are described below:\b png <ul> <li>alpha: bool (True or False) <li>compression: int (1 to 9) <li>forceSRGB: bool (True or False) <li>indexed: bool (True or False) <li>interlaced: bool (True or False) <li>saveSRGBProfile: bool (True or False) <li>transparencyFillcolor: rgb (Ex:[255,255,255]) </ul>\b jpeg <ul> <li>baseline: bool (True or False) <li>exif: bool (True or False) <li>filters: bool (['ToolInfo', 'Anonymizer']) <li>forceSRGB: bool (True or False) <li>iptc: bool (True or False) <li>is_sRGB: bool (True or False) <li>optimize: bool (True or False) <li>progressive: bool (True or False) <li>quality: int (0 to 100) <li>saveProfile: bool (True or False) <li>smoothing: int (0 to 100) <li>subsampling: int (0 to 3) <li>transparencyFillcolor: rgb (Ex:[255,255,255]) <li>xmp: bool (True or False) </ul>
@return true if the export succeeded, false if it failed. """

	def flatten(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief flatten all layers in the image """

	def resizeImage(self, x: int, y: int, w: int, h: int) -> None:
		# type: (x, y, w, h) -> None:
		"""@access public Q_SLOTS
 @brief resizeImage resizes the canvas to the given left edge, top edge, width and height. Note: This doesn't scale, use scale image for that.
@param x the new left edge
@param y the new top edge
@param w the new width
@param h the new height """

	def scaleImage(self, w: int, h: int, xres: int, yres: int, strategy: str) -> None:
		# type: (w, h, xres, yres, strategy) -> None:
		"""@access public Q_SLOTS
 @brief scaleImage
@param w the new width
@param h the new height
@param xres the new xres
@param yres the new yres
@param strategy the scaling strategy. There's several ones amongst these that aren't available in the regular UI. The list of filters is extensible and can be retrieved with Krita::filter <ul> <li>Hermite</li> <li>Bicubic - Adds pixels using the color of surrounding pixels. Produces smoother tonal gradations than Bilinear.</li> <li>Box - Replicate pixels in the image. Preserves all the original detail, but can produce jagged effects.</li> <li>Bilinear - Adds pixels averaging the color values of surrounding pixels. Produces medium quality results when the image is scaled from half to two times the original size.</li> <li>Bell</li> <li>BSpline</li> <li>Kanczos3 - Offers similar results than Bicubic, but maybe a little bit sharper. Can produce light and dark halos along strong edges.</li> <li>Mitchell</li> </ul> """

	def rotateImage(self, radians: float) -> None:
		# type: (radians) -> None:
		"""@access public Q_SLOTS
 @brief rotateImage Rotate the image by the given radians.
@param radians the amount you wish to rotate the image in radians """

	def shearImage(self, angleX: float, angleY: float) -> None:
		# type: (angleX, angleY) -> None:
		"""@access public Q_SLOTS
 @brief shearImage shear the whole image.
@param angleX the X-angle in degrees to shear by
@param angleY the Y-angle in degrees to shear by """

	def save(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief save the image to its currently set path. The modified flag of the document will be reset
@return true if saving succeeded, false otherwise. """

	def saveAs(self, filename: str) -> bool:
		# type: (filename) -> bool:
		"""@access public Q_SLOTS
 @brief saveAs save the document under the @p filename. The document's filename will be reset to @p filename.
@param filename the new filename (full path) for the document
@return true if saving succeeded, false otherwise. """

	def createNode(self, name: str, nodeType: str) -> 'Node':
		# type: (name, nodeType) -> Node:
		"""@access public Q_SLOTS
 @brief createNode create a new node of the given type. The node is not added to the node hierarchy; you need to do that by finding the right parent node, getting its list of child nodes and adding the node in the right place, then calling Node::SetChildNodes
@param name The name of the node
@param nodeType The type of the node. Valid types are: <ul>  <li>paintlayer  <li>grouplayer  <li>filelayer  <li>filterlayer  <li>filllayer  <li>clonelayer  <li>vectorlayer  <li>transparencymask  <li>filtermask  <li>transformmask  <li>selectionmask </ul> When relevant, the new Node will have the colorspace of the image by default; that can be changed with Node::setColorSpace. The settings and selections for relevant layer and mask types can also be set after the Node has been created.
@code
d = Application.createDocument(1000, 1000, "Test", "RGBA", "U8", "", 120.0)
root = d.rootNode();
print(root.childNodes())
l2 = d.createNode("layer2", "paintLayer")
print(l2)
root.addChildNode(l2, None)
print(root.childNodes())
@endcode
@return the new Node. """

	def createGroupLayer(self, name: str) -> 'GroupLayer':
		# type: (name) -> GroupLayer:
		"""@access public Q_SLOTS
 @brief createGroupLayer Returns a grouplayer object. Grouplayers are nodes that can have other layers as children and have the passthrough mode.
@param name the name of the layer.
@return a GroupLayer object. """

	def createFileLayer(self, name: str, fileName: str, scalingMethod: str, scalingFilter: str = "Bicubic") -> 'FileLayer':
		# type: (name, fileName, scalingMethod, scalingFilter) -> FileLayer:
		"""@access public Q_SLOTS
 @brief createFileLayer returns a layer that shows an external image.
@param name name of the file layer.
@param fileName the absolute filename of the file referenced. Symlinks will be resolved.
@param scalingMethod how the dimensions of the file are interpreted        can be either "None", "ImageToSize" or "ImageToPPI"
@param scalingFilter filter used to scale the file        can be "Bicubic", "Hermite", "NearestNeighbor", "Bilinear", "Bell", "BSpline", "Lanczos3", "Mitchell"
@return a FileLayer """

	def createFilterLayer(self, name: str, filter: 'Filter', selection: 'Selection') -> 'FilterLayer':
		# type: (name, filter, selection) -> FilterLayer:
		"""@access public Q_SLOTS
 @brief createFilterLayer creates a filter layer, which is a layer that represents a filter applied non-destructively.
@param name name of the filterLayer
@param filter the filter that this filter layer will us.
@param selection the selection.
@return a filter layer object. """

	def createFillLayer(self, name: str, generatorName: str, configuration: 'InfoObject', selection: 'Selection') -> 'FillLayer':
		# type: (name, generatorName, configuration, selection) -> FillLayer:
		"""@access public Q_SLOTS
 @brief createFillLayer creates a fill layer object, which is a layer
@param name
@param generatorName - name of the generation filter.
@param configuration - the configuration for the generation filter.
@param selection - the selection.
@return a filllayer object.
@code
from krita import *
d = Krita.instance().activeDocument()
i = InfoObject();
i.setProperty("pattern", "Cross01.pat")
s = Selection();
s.select(0, 0, d.width(), d.height(), 255)
n = d.createFillLayer("test", "pattern", i, s)
r = d.rootNode();
c = r.childNodes();
r.addChildNode(n, c[0])
d.refreshProjection()
@endcode """

	def createCloneLayer(self, name: str, source: 'Node') -> 'CloneLayer':
		# type: (name, source) -> CloneLayer:
		"""@access public Q_SLOTS
 @brief createCloneLayer
@param name
@param source
@return """

	def createVectorLayer(self, name: str) -> 'VectorLayer':
		# type: (name) -> VectorLayer:
		"""@access public Q_SLOTS
 @brief createVectorLayer Creates a vector layer that can contain vector shapes.
@param name the name of this layer.
@return a VectorLayer. """

	def createFilterMask(self, name: str, filter: 'Filter', selection_source: 'Node') -> 'FilterMask':
		# type: (name, filter, selection_source) -> FilterMask:
		"""@access public Q_SLOTS
 @brief createFilterMask Creates a filter mask object that much like a filterlayer can apply a filter non-destructively.
@param name the name of the layer.
@param filter the filter assigned.
@param selection_source a node from which the selection should be initialized
@return a FilterMask """

	def createSelectionMask(self, name: str) -> 'SelectionMask':
		# type: (name) -> SelectionMask:
		"""@access public Q_SLOTS
 @brief createSelectionMask Creates a selection mask, which can be used to store selections.
@param name - the name of the layer.
@return a SelectionMask """

	def createTransparencyMask(self, name: str) -> 'TransparencyMask':
		# type: (name) -> TransparencyMask:
		"""@access public Q_SLOTS
 @brief createTransparencyMask Creates a transparency mask, which can be used to assign transparency to regions.
@param name - the name of the layer.
@return a TransparencyMask """

	def createTransformMask(self, name: str) -> 'TransformMask':
		# type: (name) -> TransformMask:
		"""@access public Q_SLOTS
 @brief createTransformMask Creates a transform mask, which can be used to apply a transformation non-destructively.
@param name - the name of the layer mask.
@return a TransformMask """

	def createColorizeMask(self, name: str) -> 'ColorizeMask':
		# type: (name) -> ColorizeMask:
		"""@access public Q_SLOTS
 @brief createColorizeMask Creates a colorize mask, which can be used to color fill via keystrokes.
@param name - the name of the layer.
@return a TransparencyMask """

	def projection(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0) -> QImage:
		# type: (x, y, w, h) -> QImage:
		"""@access public Q_SLOTS
 @brief projection creates a QImage from the rendered image or a cutout rectangle. """

	def thumbnail(self, w: int, h: int) -> QImage:
		# type: (w, h) -> QImage:
		"""@access public Q_SLOTS
 @brief thumbnail create a thumbnail of the given dimensions. If the requested size is too big a null QImage is created.
@return a QImage representing the layer contents. """

	def lock(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 [low-level] Lock the image without waiting for all the internal job queues are processed WARNING: Don't use it unless you really know what you are doing! Use barrierLock() instead! Waits for all the **currently running** internal jobs to complete and locks the image for writing. Please note that this function does **not** wait for all the internal queues to process, so there might be some non-finished actions pending. It means that you just postpone these actions until you unlock() the image back. Until then, then image might easily be frozen in some inconsistent state. The only sane usage for this function is to lock the image for **emergency** processing, when some internal action or scheduler got hung up, and you just want to fetch some data from the image without races. In all other cases, please use barrierLock() instead! """

	def unlock(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Unlocks the image and starts/resumes all the pending internal jobs. If the image has been locked for a non-readOnly access, then all the internal caches of the image (e.g. lod-planes) are reset and regeneration jobs are scheduled. """

	def waitForDone(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Wait for all the internal image jobs to complete and return without locking the image. This function is handy for tests or other synchronous actions, when one needs to wait for the result of his actions. """

	def tryBarrierLock(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Tries to lock the image without waiting for the jobs to finish Same as barrierLock(), but doesn't block execution of the calling thread until all the background jobs are finished. Instead, in case of presence of unfinished jobs in the queue, it just returns false
@return whether the lock has been acquired """

	def refreshProjection(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 Starts a synchronous recomposition of the projection: everything will wait until the image is fully recomputed. """

	def modified(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief DEPRECATED - use guidesConfig() instead replace all existing horizontal guides with the entries in the list.
@param lines a list of floats containing the new guides./
    Q_DECL_DEPRECATED void setHorizontalGuides(const QList<qreal> &lines);
    /**
@brief DEPRECATED - use guidesConfig() instead replace all existing horizontal guides with the entries in the list.
@param lines a list of floats containing the new guides./
    Q_DECL_DEPRECATED void setVerticalGuides(const QList<qreal> &lines);

    /**
@brief DEPRECATED - use guidesConfig() instead set guides visible on this document.
@param visible whether or not the guides are visible./
    Q_DECL_DEPRECATED void setGuidesVisible(bool visible);

    /**
@brief DEPRECATED - use guidesConfig() instead set guides locked on this document
@param locked whether or not to lock the guides on this document./
    Q_DECL_DEPRECATED void setGuidesLocked(bool locked);

    /**
@brief modified returns true if the document has unsaved modifications. """

	def setModified(self, modified: bool) -> None:
		# type: (modified) -> None:
		"""@access public Q_SLOTS
 @brief setModified sets the modified status of the document
@param modified if true, the document is considered modified and closing it will ask for saving. """

	def bounds(self) -> QRect:
		# type: () -> QRect:
		"""@access public Q_SLOTS
 @brief bounds return the bounds of the image
@return the bounds """

	def importAnimation(self, files: List[str], firstFrame: int, step: int) -> bool:
		# type: (files, firstFrame, step) -> bool:
		"""@access public Q_SLOTS
 Animation Related API****/


    /**
@brief Import an image sequence of files from a directory. This will grab all images from the directory and import them with a potential offset (firstFrame) and step (images on 2s, 3s, etc)
@returns whether the animation import was successful """

	def framesPerSecond(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief frames per second of document
@return the fps of the document """

	def setFramesPerSecond(self, fps: int) -> None:
		# type: (fps) -> None:
		"""@access public Q_SLOTS
 @brief set frames per second of document """

	def setFullClipRangeStartTime(self, startTime: int) -> None:
		# type: (startTime) -> None:
		"""@access public Q_SLOTS
 @brief set start time of animation """

	def fullClipRangeStartTime(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get the full clip range start time
@return full clip range start time """

	def setFullClipRangeEndTime(self, endTime: int) -> None:
		# type: (endTime) -> None:
		"""@access public Q_SLOTS
 @brief set full clip range end time """

	def fullClipRangeEndTime(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get the full clip range end time
@return full clip range end time """

	def animationLength(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get total frame range for animation
@return total frame range for animation """

	def setPlayBackRange(self, start: int, stop: int) -> None:
		# type: (start, stop) -> None:
		"""@access public Q_SLOTS
 @brief set temporary playback range of document """

	def playBackStartTime(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get start time of current playback
@return start time of current playback """

	def playBackEndTime(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get end time of current playback
@return end time of current playback """

	def currentTime(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief get current frame selected of animation
@return current frame selected of animation """

	def setCurrentTime(self, time: int) -> None:
		# type: (time) -> None:
		"""@access public Q_SLOTS
 @brief set current time of document's animation """

	def annotationTypes(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief annotationTypes returns the list of annotations present in the document. Each annotation type is unique. """

	def annotationDescription(self, type: str) -> str:
		# type: (type) -> str:
		"""@access public Q_SLOTS
 @brief annotationDescription gets the pretty description for the current annotation
@param type the type of the annotation
@return a string that can be presented to the user """

	def annotation(self, type: str) -> QByteArray:
		# type: (type) -> QByteArray:
		"""@access public Q_SLOTS
 @brief annotation the actual data for the annotation for this type. It's a simple QByteArray, what's in it depends on the type of the annotation
@param type the type of the annotation
@return a bytearray, possibly empty if this type of annotation doesn't exist """

	def setAnnotation(self, type: str, description: str, annotation: Union[QByteArray, bytes, bytearray]) -> None:
		# type: (type, description, annotation) -> None:
		"""@access public Q_SLOTS
 @brief setAnnotation Add the given annotation to the document
@param type the unique type of the annotation
@param description the user-visible description of the annotation
@param annotation the annotation itself """

	def removeAnnotation(self, type: str) -> None:
		# type: (type) -> None:
		"""@access public Q_SLOTS
 @brief removeAnnotation remove the specified annotation from the image
@param type the type defining the annotation """

	def setAutosave(self, active: bool) -> None:
		# type: (active) -> None:
		"""@access public Q_SLOTS
 @brief Allow to activate/deactivate autosave for document When activated, it will use default Krita autosave settings It means that even when autosave is set to True, under condition Krita will not proceed to automatic save of document: - autosave is globally deactivated - document is read-only Being able to deactivate autosave on a document can make sense when a plugin use internal document (document is not exposed in a view, only created for internal process purposes)
@param active True to activate autosave """

	def autosave(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Return autosave status for document Notes: - returned value is Autosave flag value   Even if autosave is set to True, under condition Krita will not proceed to automatic save of document:   - autosave is globally deactivated   - document is read-only - When autosave is set to False, Krita never execute automatic save for document
@return True if autosave is active, otherwise False """

	def guidesConfig(self) -> 'GuidesConfig':
		# type: () -> GuidesConfig:
		"""@access public Q_SLOTS
 @brief Returns a GuidesConfig guides configuration for current document
@return a GuidesConfig object with guides configuration """

	def setGuidesConfig(self, guidesConfig: 'GuidesConfig') -> None:
		# type: (guidesConfig) -> None:
		"""@access public Q_SLOTS
 @brief Set guides configuration for current document
@param guidesConfig a GuidesConfig object to apply for guides configuration To modify/set guides property on a document
@code
# get document (create one or get active one for example)
newDoc = Krita.instance().createDocument(500, 500, "Test", "RGBA", "U8", "", 300)

# retrieve document guides configuration
newDocGuides = newDoc.guidesConfig()

# update properties
newDocGuides.setColor(QColor('#ff00ff'))
newDocGuides.setLineType('dotted')
newDocGuides.setVisible(True)
newDocGuides.setLocked(True)
newDocGuides.setSnap(True)
newDocGuides.setHorizontalGuides([100,200])

# set guides configuration to document
newDoc.setGuidesConfig(newDocGuides)
@endcode """

	def gridConfig(self) -> 'GridConfig':
		# type: () -> GridConfig:
		"""@access public Q_SLOTS
 @brief Returns a GridConfig grid configuration for current document
@return a GridConfig object with grid configuration """

	def setGridConfig(self, gridConfig: 'GridConfig') -> None:
		# type: (gridConfig) -> None:
		"""@access public Q_SLOTS
 @brief Set grid configuration for current document
@param gridConfig a GridConfig object to apply for grid configuration To modify/set grid property on a document
@code
# get document (create one or get active one for example)
newDoc = Krita.instance().createDocument(500, 500, "Test", "RGBA", "U8", "", 300)

# retrieve document grid configuration
newDocGrid = newDoc.gridConfig()

# update properties
newDocGrid.setColorMain(QColor('#ff00ff'))
newDocGrid.setLineTypeMain('dashed')
newDocGrid.setVisible(True)
newDocGrid.setAngleLeft(30)
newDocGrid.setAngleRight(15)
newDocGrid.setType('isometric')

# set grid configuration to document
newDoc.setGridConfig(newDocGrid)
@endcode """

	def audioLevel(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Return current audio level for document
@return A value between 0.0 and 1.0 (1.0 = 100%) """

	def setAudioLevel(self, level: float) -> None:
		# type: (level) -> None:
		"""@access public Q_SLOTS
 @brief Set current audio level for document
@param level Audio volume between 0.0 and 1.0 (1.0 = 100%) """

	def audioTracks(self) -> List[str]:
		# type: () -> List[str]:
		"""@access public Q_SLOTS
 @brief Return a list of current audio tracks for document
@return List of absolute path/file name of audio files """

	def setAudioTracks(self, files: List[str]) -> bool:
		# type: (files) -> bool:
		"""@access public Q_SLOTS
 @brief Set a list of audio tracks for document Note: the function allows to add more than one file while from Krita's UI, importing a file will replace the complete list The reason why this method let the ability to provide more than one file is related to the internal's Krita method from KisDocument class: void KisDocument::setAudioTracks(QVector<QFileInfo> f)
@param files List of absolute path/file name of audio files
@return True if all files from list have been added, otherwise False (a file was not found) """

class Channel(QObject):
	"""* A Channel represents a single channel in a Node. Krita does not use channels to store local selections: these are strictly the color and alpha channels. """

	def visible(self) -> bool:
		# type: () -> bool:
		"""@access public
 @brief visible checks whether this channel is visible in the node
@return the status of this channel """

	def setVisible(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public
 @brief setvisible set the visibility of the channel to the given value. """

	def name(self) -> str:
		# type: () -> str:
		"""@access public
 @return the name of the channel """

	def position(self) -> int:
		# type: () -> int:
		"""@access public
 @returns the position of the first byte of the channel in the pixel """

	def channelSize(self) -> int:
		# type: () -> int:
		"""@access public
 @return the number of bytes this channel takes """

	def bounds(self) -> QRect:
		# type: () -> QRect:
		"""@access public
 @return the exact bounds of the channel. This can be smaller than the bounds of the Node this channel is part of. """

	def pixelData(self, rect: QRect) -> QByteArray:
		# type: (rect) -> QByteArray:
		"""@access public
 Read the values of the channel into the a byte array for each pixel in the rect from the Node this channel is part of, and returns it. Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita returns 32 bits float for every channel; the libkis scripting API does not support half. """

	def setPixelData(self, value: Union[QByteArray, bytes, bytearray], rect: QRect) -> None:
		# type: (value, rect) -> None:
		"""@access public
 @brief setPixelData writes the given data to the relevant channel in the Node. This is only possible for Nodes that have a paintDevice, so nothing will happen when trying to write to e.g. a group layer. Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita expects to be given a 4 byte, 32 bits float for every channel; the libkis scripting API does not support half.
@param value a byte array with exactly enough bytes.
@param rect the rectangle to write the bytes into """

class Canvas(QObject):
	"""* Canvas wraps the canvas inside a view on an image/document. It is responsible for the view parameters of the document: zoom, rotation, mirror, wraparound and instant preview. """

	def zoomLevel(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return the current zoomlevel. 1.0 is 100%. """

	def setZoomLevel(self, value: float) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setZoomLevel set the zoomlevel to the given @p value. 1.0 is 100%. """

	def setPreferredCenter(self, imagePos: QPointF) -> None:
		# type: (imagePos) -> None:
		"""@access public Q_SLOTS
 @brief setPan Centers the image pixel at \p imagePos in the current view """

	def preferredCenter(self) -> QPointF:
		# type: () -> QPointF:
		"""@access public Q_SLOTS
 @brief \return the position of the image pixel that is placed in the center of the current view """

	def pan(self, offset: QPoint) -> None:
		# type: (offset) -> None:
		"""@access public Q_SLOTS
 @brief pan the current view in pixels. """

	def resetZoom(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief resetZoom set the zoomlevel to 100% """

	def rotation(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @return the rotation of the canvas in degrees. """

	def setRotation(self, angle: float) -> None:
		# type: (angle) -> None:
		"""@access public Q_SLOTS
 @brief setRotation set the rotation of the canvas to the given  @param angle in degrees. """

	def resetRotation(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief resetRotation reset the canvas rotation. """

	def mirror(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @return return true if the canvas is mirrored, false otherwise. """

	def setMirror(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setMirror turn the canvas mirroring on or off depending on @param value """

	def wrapAroundMode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @return true if the canvas is in wraparound mode, false if not. Only when OpenGL is enabled, is wraparound mode available. """

	def setWrapAroundMode(self, enable: bool) -> None:
		# type: (enable) -> None:
		"""@access public Q_SLOTS
 @brief setWrapAroundMode set wraparound mode to  @param enable """

	def levelOfDetailMode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @return true if the canvas is in Instant Preview mode, false if not. Only when OpenGL is enabled, is Instant Preview mode available. """

	def setLevelOfDetailMode(self, enable: bool) -> None:
		# type: (enable) -> None:
		"""@access public Q_SLOTS
 @brief setLevelOfDetailMode sets Instant Preview to @param enable """

	def view(self) -> 'View':
		# type: () -> View:
		"""@access public Q_SLOTS
 @return the view that holds this canvas """

class AngleSelector(QObject):
	"""* @brief A wrapper around KisAngleSelector, a widget with several options to select an angle. The widget itself is accessed with the widget() function.  This widget is a combination of a @ref KisAngleGauge and a spin box, along with some flipping options """

	def widget(self) -> QWidget:
		# type: () -> QWidget:
		"""@access public Q_SLOTS
 @brief Get the internal KisAngleSelector as a QWidget, so it may be added to a UI
@return the internal KisAngleSelector as a QWidget """

	def setAngle(self, newAngle: float) -> None:
		# type: (newAngle) -> None:
		"""@access public Q_SLOTS
 @brief Sets the current angle
@param newAngle the new angle
@see angle() const """

	def reset(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Sets the current angle to the reset angle
@see resetAngle() const
@see setResetAngle(qreal) const """

	def angle(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Gets the current angle
@return The current angle
@see setAngle(qreal) """

	def snapAngle(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Gets the angle to which multiples the selected angle will snap  The default snap angle is 15 degrees so the selected angle will snap to its multiples (0, 15, 30, 45, etc.)
@return The angle to which multiples the selected angle will snap
@see setSnapAngle(qreal) """

	def resetAngle(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Gets the angle that is used to reset the current angle  This angle is used when the user double clicks on the widget
@return The angle that is used to reset the current angle
@see setResetAngle(qreal) """

	def decimals(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Gets the number of decimals (precision) used by the angle  If you want to simulate integer angles, set it to 0. The default is 2.
@return The number of decimals being used
@see setDecimals(int) """

	def maximum(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Gets the maximum value for the angle  The default is 360
@return The maximum value for the angle
@see setMaximum(qreal)
@see setRange(qreal, qreal) """

	def minimum(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief Gets the minimum value for the angle  The default is 0
@return The minimum value for the angle
@see setMinimum(qreal)
@see setRange(qreal, qreal) """

	def prefix(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Gets the prefix shown in the spin box
@return The prefix shown in the spin box
@see setPrefix(const QString&) """

	def wrapping(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Gets if the angle should wrap pass the minimum or maximum angles
@return True if the angle should wrap pass the minimum or maximum angles, false otherwise
@see setWrapping(bool) """

	def flipOptionsMode(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Gets the mode in which the flip options should be shown  The default is Buttons
@return The mode in which the flip options should be shown.
@see setFlipOptionsMode(QString) """

	def widgetsHeight(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Gets the common height of the widgets inside this angle selector
@return The height of the internal widgets (angle gauge, spin box, etc.).         Returns 0 if each widget has its default height.
@see setWidgetsHeight(int) """

	def increasingDirection(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief Gets the direction in which the angle increases in the angle gauge
@return The direction in which the angle increases
@see setIncreasingDirection(QString) """

	def isUsingFlatSpinBox(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Gets if the spin box is flat (no border or background)
@return True if the spin box is flat, false otherwise
@see useFlatSpinBox(bool) """

	def setSnapAngle(self, newSnapAngle: float) -> None:
		# type: (newSnapAngle) -> None:
		"""@access public Q_SLOTS
 @brief Sets the angle to which multiples the selected angle will snap
@param newSnapAngle the new angle to which multiples the selected angle will snap
@see snapAngle() const """

	def setResetAngle(self, newResetAngle: float) -> None:
		# type: (newResetAngle) -> None:
		"""@access public Q_SLOTS
 @brief Sets the angle that is used to reset the current angle
@param newResetAngle the new angle that is used to reset the current angle
@see resetAngle() const """

	def setDecimals(self, newNumberOfDecimals: int) -> None:
		# type: (newNumberOfDecimals) -> None:
		"""@access public Q_SLOTS
 @brief Sets the number of decimals (precision) used by the angle
@param newNumberOfDecimals the new number of decimals used by the angle
@see decimals() const """

	def setMaximum(self, newMaximum: float) -> None:
		# type: (newMaximum) -> None:
		"""@access public Q_SLOTS
 @brief Sets the maximum value for the angle
@param newMaximum the new maximum value for the angle
@see maximum() const
@see setRange(qreal, qreal) """

	def setMinimum(self, newMinimum: float) -> None:
		# type: (newMinimum) -> None:
		"""@access public Q_SLOTS
 @brief Sets the minimum value for the angle
@param newMinimum the new minimum value for the angle
@see minimum() const
@see setRange(qreal, qreal) """

	def setRange(self, newMinimum: float, newMaximum: float) -> None:
		# type: (newMinimum, newMaximum) -> None:
		"""@access public Q_SLOTS
 @brief Sets the minimum and maximum values for the angle
@param newMinimum the new minimum value for the angle
@param newMaximum the new maximum value for the angle
@see minimum() const
@see maximum() const
@see setMinimum(qreal)
@see setMaximum(qreal) """

	def setPrefix(self, newPrefix: str) -> None:
		# type: (newPrefix) -> None:
		"""@access public Q_SLOTS
 @brief Sets the prefix shown in the spin box
@param newPrefix the new prefix for the spin box
@see prefix() const """

	def setWrapping(self, newWrapping: bool) -> None:
		# type: (newWrapping) -> None:
		"""@access public Q_SLOTS
 @brief Sets if the angle should wrap pass the minimum or maximum angles
@param newWrapping true if the angle should wrap pass the minimum or maximum angles, false otherwise
@see wrapping() const """

	def setFlipOptionsMode(self, newMode: str) -> None:
		# type: (newMode) -> None:
		"""@access public Q_SLOTS
 @brief Sets the mode in which the flip options should be shown
@param newMode the new mode in which the flip options should be shown Valid arguments: <ul> <li>NoFlipOptions - There are no flip options available</li> <li>MenuButton - The flip options are shown as a menu accessible via a options button</li> <li>Buttons - The flip options are shown as individual buttons</li> <li>ContextMenu - The flip options are shown only as a context menu when right-clicking the gauge widget</li> <ul>
@see flipOptionsMode() const """

	def setWidgetsHeight(self, newHeight: int) -> None:
		# type: (newHeight) -> None:
		"""@access public Q_SLOTS
 @brief Sets the common height of the widgets inside this angle selector.        Use 0 to reset widgets to default height.
@param newHeight the new height of the internal widgets (angle gauge, spin box, etc.)
@see widgetsHeight() const """

	def setIncreasingDirection(self, newIncreasingDirection: str) -> None:
		# type: (newIncreasingDirection) -> None:
		"""@access public Q_SLOTS
 @brief Sets the increasing direction in the angle gauge
@param newIncreasingDirection The new increasing direction Valid arguments: CounterClockwise or Clockwise.
@see increasingDirection() const """

	def useFlatSpinBox(self, newUseFlatSpinBox: bool) -> None:
		# type: (newUseFlatSpinBox) -> None:
		"""@access public Q_SLOTS
 @brief Sets if the spin box should be flat
@param newUseFlatSpinBox True if the spin box should be flat, false otherwise
@see isUsingFlatSpinBox() const """

	def closestCoterminalAngleInRange(self, angle: float, ok: bool = nullptr) -> float:
		# type: (angle, ok) -> float:
		"""@access public Q_SLOTS
 @brief Gets the closest coterminal angle to the provided angle that is in the range established  A coterminal angle to the provided angle is one that differs in size by an integer multiple of a turn (360 degrees)
@param angle The reference angle for which the function will try to find a coterminal angle
@param[out] ok This parameter will be set to true if a coterminal angle exists in the specified range, or to false otherwise
@return The closest coterminal angle in the specified range if one exists, or the closest value in the range (the minimum or maximum) otherwise. If the reference angle is already in the range then it is returned """

	@staticmethod
	def flipAngle(angle: float, minimum: float, maximum: float, orientations: Qt::Orientations, ok: bool = nullptr) ->  float:
		# type: (angle, minimum, maximum, orientations, ok) ->  float:
		"""@access public Q_SLOTS
 @brief Flips an angle horizontally, vertically, or both  This function will always try to get the closest angle to the provided one that satisfies the flipping requirements
@param angle The angle to be flipped
@param minimum The lower bound of the valid range
@param maximum The upper bound of the valid range
@param orientations Flags indicating in which directions the angle should be flipped
@param[out] ok This parameter will be set to true if the flipped angle is in the provided range, or to false otherwise
@return The flipped angle if it lies in the provided range or the closest value in the range (the minimum or maximum) otherwise """

	def flip(self, orientations: Qt::Orientations) -> None:
		# type: (orientations) -> None:
		"""@access public Q_SLOTS
 @brief Flips the angle horizontally, vertically, or both  This function will always try to set the closest angle to the stablished one that satisfies the flipping requirements
@param orientations Flags indicating in which directions the angle should be flipped """

class VectorLayer(Node):
	"""* @brief The VectorLayer class A vector layer is a special layer that stores and shows vector shapes. Vector shapes all have their coordinates in points, which is a unit that represents 1/72th of an inch. Keep this in mind wen parsing the bounding box and position data. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return vectorlayer """

	def shapes(self) -> List['Shape']:
		# type: () -> List[Shape]:
		"""@access public Q_SLOTS
 @brief shapes
@return the list of top-level shapes in this vector layer. """

	def toSvg(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief toSvg convert the shapes in the layer to svg.
@return the svg in a string. """

	def addShapesFromSvg(self, svg: str) -> List['Shape']:
		# type: (svg) -> List[Shape]:
		"""@access public Q_SLOTS
 @brief addShapesFromSvg add shapes to the layer from a valid svg.
@param svg valid svg string.
@return the list of shapes added to the layer from the svg. """

	def shapeAtPosition(self, position: QPointF) -> 'Shape':
		# type: (position) -> Shape:
		"""@access public Q_SLOTS
 @brief shapeAtPoint check if the position is located within any non-group shape's boundingBox() on the current layer.
@param position a QPointF of the position.
@return the shape at the position, or None if no shape is found. """

	def shapesInRect(self, rect: QRectF, omitHiddenShapes: bool = True, containedMode: bool = False) -> List['Shape']:
		# type: (rect, omitHiddenShapes, containedMode) -> List[Shape]:
		"""@access public Q_SLOTS
 @brief shapeInRect get all non-group shapes that the shape's boundingBox() intersects or is contained within a given rectangle on the current layer.
@param rect a QRectF
@param omitHiddenShapes true if non-visible() shapes should be omitted, false if they should be included. \p omitHiddenShapes defaults to true.
@param containedMode false if only shapes that are within or intersect with the outline should be included, true if only shapes that are fully contained within the outline should be included. \p containedMode defaults to false
@return returns a list of shapes. """

	def createGroupShape(self, name: str, shapes: List['Shape']) -> 'Shape':
		# type: (name, shapes) -> Shape:
		"""@access public Q_SLOTS
 @brief createGroupShape combine a list of top level shapes into a group.
@param name the name of the shape.
@param shapes list of top level shapes.
@return if successful, a GroupShape object will be returned. """

	def isAntialiased(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief return antialiasing status for the Vector layer
@return True if antialiasing is active for the layer """

	def setAntialiased(self, antialiased: bool) -> None:
		# type: (antialiased) -> None:
		"""@access public Q_SLOTS
 @brief set antialiasing status for the Vector layer
@param antialiased set to True to activate antialiasing """

class TransparencyMask(Node):
	"""* @brief The TransparencyMask class A transparency mask is a mask type node that can be used to show and hide parts of a layer. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return transparencymask If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def selection(self) -> 'Selection':
		# type: () -> Selection:
		"""@access public Q_SLOTS
 """

	def setSelection(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 """

class TransformMask(Node):
	"""* @brief The TransformMask class A transform mask is a mask type node that can be used to store transformations. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return transformmask If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def toXML(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief toXML
@return a string containing XML formatted transform parameters. """

	def fromXML(self, xml: str) -> bool:
		# type: (xml) -> bool:
		"""@access public Q_SLOTS
 @brief fromXML set the transform of the transform mask from XML formatted data. The xml must have a valid id dumbparams - placeholder for static transform masks tooltransformparams - static transform mask animatedtransformparams - animated transform mask
@code
<!DOCTYPE transform_params>
<transform_params>
  <main id="tooltransformparams"/>
  <data mode="0">
   <free_transform>
    <transformedCenter type="pointf" x="12.3102137276208" y="11.0727768562035"/>
    <originalCenter type="pointf" x="20" y="20"/>
    <rotationCenterOffset type="pointf" x="0" y="0"/>
    <transformAroundRotationCenter value="0" type="value"/>
    <aX value="0" type="value"/>
    <aY value="0" type="value"/>
    <aZ value="0" type="value"/>
    <cameraPos z="1024" type="vector3d" x="0" y="0"/>
    <scaleX value="1" type="value"/>
    <scaleY value="1" type="value"/>
    <shearX value="0" type="value"/>
    <shearY value="0" type="value"/>
    <keepAspectRatio value="0" type="value"/>
    <flattenedPerspectiveTransform m23="0" m31="0" m32="0" type="transform" m33="1" m12="0" m13="0" m22="1" m11="1" m21="0"/>
    <filterId value="Bicubic" type="value"/>
   </free_transform>
  </data>
</transform_params>
@endcode
@param xml a valid formatted XML string with proper main and data elements.
@return a true response if successful, a false response if failed. """

class SliderSpinBox(IntParseSpinBox):
	"""* @brief This class is a wrapper around KisSliderSpinBox, a spinbox in which  you can click and drag to set the value, with a slider like bar displayed inside. The widget itself is accessed with the widget() function.  The value can be set by click and dragging with the mouse or pen or by typing in with the keyboard. To enter the edit mode, in which the keyboard can be used, one has to right-click inside the spinbox or click and hold the pointer inside or press the enter key. To leave the edit mode, one can press the enter key again, in which case the value is committed, or press the escape key, in which case the value is rejected.  When dragging with the pointer, one can fine tune the value by dragging far away vertically from the spinbox. The farther the pointer is, the slower the value will change. If the pointer is inside the spinbox plus a certain margin, the value will not be scaled. By pressing the shift key the slow down will be even more pronounced and by pressing the control key the value will snap to the increment set by
@ref setFastSliderStep. The two keys can be used at the same time.  A "soft range" can be set to make the slider display only a sub-range of the spinbox range. This way one can have a large range but display and set with the pointer and with more precision only the most commonly used sub-set of values. A value outside the "soft range" can be set by entering the edit mode and using the keyboard. The "soft range" is considered valid if the "soft maximum" is greater than the "soft minimum". """

	def widget(self) -> QWidget:
		# type: () -> QWidget:
		"""@access public Q_SLOTS
 @brief Get the internal KisDoubleSliderSpinBox as a QWidget, so it may be added to a UI
@return the internal KisDoubleSliderSpinBox as a QWidget """

	def fastSliderStep(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Get the value to which multiples the spinbox value snaps when the control key is pressed
@return the value to which multiples the spinbox value snaps when the control key is pressed
@see setFastSliderStep(int) """

	def softMinimum(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Get the minimum value of the "soft range"
@return the minimum value of the "soft range"
@see setSoftMinimum(int)
@see setSoftRange(int, int)
@see softMaximum() const  """

	def softMaximum(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief Get the maximum value of the "soft range"
@return the maximum value of the "soft range"
@see setSoftMaximum(int)
@see setSoftRange(int, int)
@see softMinimum) const  """

	def isDragging(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief Get if the user is currently dragging the slider with the pointer
@return true if the user is currently dragging the slider with the pointer, false otherwise """

	def setValue(self, newValue: int) -> None:
		# type: (newValue) -> None:
		"""@access public Q_SLOTS
 @brief Set the value
@param newValue the new value """

	def setRange(self, newMinimum: float, newMaximum: float, newNumberOfDecimals: int = 0, computeNewFastSliderStep: bool = True) -> None:
		# type: (newMinimum, newMaximum, newNumberOfDecimals, computeNewFastSliderStep) -> None:
		"""@access public Q_SLOTS
 @brief Set the minimum and the maximum values of the range  The soft range will be adapted to fit inside the range The number of decimals used can be changed with the newNumberOfDecimals parameter
@param newMinimum the new minimum value
@param newMaximum the new maximum value
@param newNumberOfDecimals the new number of decimals
@param computeNewFastSliderStep true if a new "fast slider step" must be computed based on the range
@see setMinimum(qreal)
@see setMaximum(qreal) """

	def setMinimum(self, newMinimum: int, computeNewFastSliderStep: bool = True) -> None:
		# type: (newMinimum, computeNewFastSliderStep) -> None:
		"""@access public Q_SLOTS
 @brief Set the minimum value of the range  The soft range will be adapted to fit inside the range
@param newMinimum the new minimum value
@param computeNewFastSliderStep true if a new "fast slider step" must be computed based on the range
@see setRange(int,int)
@see setMaximum(int) """

	def setMaximum(self, newMaximum: int, computeNewFastSliderStep: bool = True) -> None:
		# type: (newMaximum, computeNewFastSliderStep) -> None:
		"""@access public Q_SLOTS
 @brief Set the maximum value of the range  The soft range will be adapted to fit inside the range
@param newMaximum the new maximum value
@param computeNewFastSliderStep true if a new "fast slider step" must be computed based on the range
@see setRange(int,int)
@see setMinimum(int) """

	def setExponentRatio(self, newExponentRatio: float) -> None:
		# type: (newExponentRatio) -> None:
		"""@access public Q_SLOTS
 @brief Set the exponent used by a power function to modify the values as a function of the horizontal position.  This allows having more values concentrated in one side of the slider than the other
@param newExponentRatio the new exponent to be used by the power function """

	def setBlockUpdateSignalOnDrag(self, newBlockUpdateSignalOnDrag: bool) -> None:
		# type: (newBlockUpdateSignalOnDrag) -> None:
		"""@access public Q_SLOTS
 @brief Set if the spinbox should not Q_EMIT signals when dragging the slider.  This is useful to prevent multiple updates when changing the value if the update operation is costly. A valueChanged signal will be emitted when the pointer is released from the slider.
@param newBlockUpdateSignalOnDrag true if the spinbox should not emit signals when dragging the slider. false otherwise """

	def setFastSliderStep(self, newFastSliderStep: int) -> None:
		# type: (newFastSliderStep) -> None:
		"""@access public Q_SLOTS
 @brief Set the value to which multiples the spinbox value snaps when the control key is pressed
@param newFastSliderStep value to which multiples the spinbox value snaps when the control key is pressed
@see fastSliderStep() const """

	def setSoftRange(self, newSoftMinimum: int, newSoftMaximum: int) -> None:
		# type: (newSoftMinimum, newSoftMaximum) -> None:
		"""@access public Q_SLOTS
 @brief Set the minimum and the maximum values of the soft range
@param newSoftMinimum the new minimum value
@param newSoftMaximum the new maximum value
@see setSoftMinimum(int)
@see setSoftMaximum(int)
@see softMinimum() const
@see softMaximum() const """

	def setSoftMinimum(self, newSoftMinimum: int) -> None:
		# type: (newSoftMinimum) -> None:
		"""@access public Q_SLOTS
 @brief Set the minimum value of the soft range
@param newSoftMinimum the new minimum value
@see setSoftRange(int,int)
@see setSoftMaximum(int)
@see softMinimum() const
@see softMaximum() const """

	def setSoftMaximum(self, newSoftMaximum: int) -> None:
		# type: (newSoftMaximum) -> None:
		"""@access public Q_SLOTS
 @brief Set the maximum value of the soft range
@param newSoftMaximum the new maximum value
@see setSoftRange(int,int)
@see setSoftMinimum(int)
@see softMinimum() const
@see softMaximum() const """

class SelectionMask(Node):
	"""* @brief The SelectionMask class A selection mask is a mask type node that can be used to store selections. In the gui, these are referred to as local selections. A selection mask can hold both raster and vector selections, though the API only supports raster selections. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return selectionmask If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def selection(self) -> 'Selection':
		# type: () -> Selection:
		"""@access public Q_SLOTS
 """

	def setSelection(self, selection: 'Selection') -> None:
		# type: (selection) -> None:
		"""@access public Q_SLOTS
 """

class Scratchpad(QWidget):
	"""* @brief The Scratchpad class A scratchpad is a type of blank canvas area that can be painted on  with the normal painting devices """

	def clear(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Clears out scratchpad with color specified set during setup """

	def fillDefault(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with default color """

	def fillBackground(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with current gradient
@param gradientVectorStart is a QPoint to define origin of gradient Set an empty QPoint() to use default scratchpad top-left
@param gradientVectorEnd is a QPoint to define end of gradient set an empty QPoint() to use default scratchpad bottom-right
@param gradientShape define which gradient to apply, can be: - "linear" - "bilinear" - "radial" - "square" - "conical" - "conicalSymmetric" - "spiral" - "reverseSpiral" - "polygonal"
@param gradientRepeat define how to repeat gradient, can be: - "none" - "alternate" - "forwards"
@param reverseGradient a boolean to define if gradient is reversed or not
@param dither a boolean to define if gradient is dithered or not/
    void fillGradient(const QPoint &gradientVectorStart = QPoint(),
                      const QPoint &gradientVectorEnd = QPoint(),
                      const QString &gradientShape = "linear",
                      const QString &gradientRepeat = "none",
                      bool reverseGradient = false,
                      bool dither = false);

    /**
@brief Fill the entire scratchpad with current background color """

	def fillForeground(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with current foreground color """

	def fillTransparent(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with a transparent color """

	def fillDocument(self, fullContent: bool = True) -> None:
		# type: (fullContent) -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with current document projection content
@param fullContent when True, full document projection is loaded in scratchpad, otherwise only content matching scratchpad viewport is loaded """

	def fillLayer(self, fullContent: bool = True) -> None:
		# type: (fullContent) -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with current layer content
@param fullContent when True, full layer content is loaded in scratchpad, otherwise only content matching scratchpad viewport is loaded """

	def fillPattern(self, transform: QTransform = QTransform()) -> None:
		# type: (transform) -> None:
		"""@access public Q_SLOTS
 @brief Fill the entire scratchpad with current pattern
@param transform is QTransform that let define pattern scale/rotation property """

	def setFillColor(self, color: QColor) -> None:
		# type: (color) -> None:
		"""@access public Q_SLOTS
 @brief Define default fill color for scratchpad
@param Color to fill the canvas with """

	def setModeManually(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief Switches between a GUI controlling the current mode and when mouse clicks control mode
@param value Set to True allows GUI to control the mode with explicitly setting mode """

	def setMode(self, modeName: str) -> None:
		# type: (modeName) -> None:
		"""@access public Q_SLOTS
 @brief Manually set what mode scratchpad is in. Ignored if "setModeManually is set to false
@param modeName Available options are: - "painting" - "panning" - "colorsampling" """

	def linkCanvasZoom(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief DEPRECATED -- USE setCanvasZoomLink() instead Makes a connection between the zoom of the canvas and scratchpad area so they zoom in sync
@param value If True (default) the scratchpad will share the current view zoom level. If False, then use scratchpad scale methods to define current zoom level """

	def canvasZoomLink(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief return if scratchpad zoom level is linked with current view zoom level
@return return True if connection between the zoom of the canvas and scratchpad (so they zoom in sync) is active """

	def setCanvasZoomLink(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief Makes a connection between the zoom of the canvas and scratchpad area so they zoom in sync
@param value If True (default) the scratchpad will share the current view zoom level. If False, then use scratchpad scale methods to define current zoom level """

	def scale(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief return current zoom level applied on scratchpad (whatever the zoom source is: view zoom level or set manually)
@return a float value (1.00 = 100%) """

	def setScale(self, scale: float) -> bool:
		# type: (scale) -> bool:
		"""@access public Q_SLOTS
 @brief allow to manually set scratchpad zoom level Note: call method is ignored if canvasZoomLink() is True,
@param scale zoom level to apply (1.00 = 100%)
@return if scale has been applied return True, otherwise return False """

	def scaleToFit(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief calculate scale automatically to fit scratchpad content in scratchpad viewport Note: call method is ignored if canvasZoomLink() is True """

	def scaleReset(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief reset scale and pan to origin Note: call method is ignored if canvasZoomLink() is True """

	def panTo(self, x: qint32, y: qint32) -> None:
		# type: (x, y) -> None:
		"""@access public Q_SLOTS
 @brief pan scratchpad content to top-left position of scratchpad viewport Provided value are absolute
@param x abscissa position to pan to
@param y ordinate position to pan to """

	def panCenter(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief pan scratchpad content to center content in viewport """

	def loadScratchpadImage(self, image: QImage) -> None:
		# type: (image) -> None:
		"""@access public Q_SLOTS
 @brief Load image data to the scratchpad
@param image Image object to load """

	def copyScratchpadImageData(self) -> QImage:
		# type: () -> QImage:
		"""@access public Q_SLOTS
 @brief Take what is on the scratchpad area and grab image
@return the image data from the scratchpad """

	def viewportBounds(self) -> QRect:
		# type: () -> QRect:
		"""@access public Q_SLOTS
 @brief The viewport indicates which part of scratchpad content is visible. It takes in account the current translation & scale Example 1: - Scratchpad size: 500x500 - Scratchpad content: 2000x2000 - Scratchpad scale: 1.0 - Scratchpad pan:   0, 0 Returned viewport is a QRect(0, 0, 500, 500) matching content really visible in scratchpad. If scale is 2.00, returned viewport will be QRect(0, 0, 250, 250) If scale is 0.50, returned viewport will be QRect(0, 0, 1000, 1000) Example 2: - Scratchpad size: 500x500 - Scratchpad content: 2000x2000 - Scratchpad scale: 2.0 - Scratchpad pan:   500, 1500 Returned viewport is a QRect(500, 1500, 250, 250) matching content really visible in scratchpad.
@return scratchpad viewport bounds as a QRect """

	def contentBounds(self) -> QRect:
		# type: () -> QRect:
		"""@access public Q_SLOTS
 @brief The content of scratchpad can be bigger or smaller than scratchpad dimension. The bounds return the area in which there's some content
@return scratchpad content bounds as a QRect """

	def scaleChanged(self, scale: float) -> None:
		# type: (scale) -> None:
		"""@access public Q_SLOTS
 @brief signal is emitted when scratchpad scale is changed (from zoom canvas or manually)
@param scale updated scale value (1.00 = 100%) """

	def contentChanged(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief signal is emitted when scratchpad content is changed (stroke or fill) """

	def viewportChanged(self, rect: QRect) -> None:
		# type: (rect) -> None:
		"""@access public Q_SLOTS
 @brief signal is emitted when scratchpad viewport has been modified (pan, zoom)
@param rect new viewport bounds """

class PresetChooser(KisPresetChooser):
	"""* @brief The PresetChooser widget wraps the KisPresetChooser widget. The widget provides for selecting brush presets. It has a tagging bar and a filter field. It is not automatically synchronized with  the currently selected preset in the current Windows. """

	def setCurrentPreset(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 Make the given preset active. """

	def currentPreset(self) -> 'Resource':
		# type: () -> Resource:
		"""@access public Q_SLOTS
 @return a Resource wrapper around the currently selected preset.  """

	def presetSelected(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 Emitted whenever a user selects the given preset. """

	def presetClicked(self, resource: 'Resource') -> None:
		# type: (resource) -> None:
		"""@access public Q_SLOTS
 Emitted whenever a user clicks on the given preset. """

class PaletteView(QWidget):
	"""* @class PaletteView
@brief The PaletteView class is a wrapper around a MVC method for handling palettes. This class shows a nice widget that can drag and drop, edit colors in a colorset and will handle adding and removing entries if you'd like it to. """

	def setPalette(self, palette: 'Palette') -> None:
		# type: (palette) -> None:
		"""@access public Q_SLOTS
 @brief setPalette Set a new palette.
@param palette """

	def addEntryWithDialog(self, color: 'ManagedColor') -> bool:
		# type: (color) -> bool:
		"""@access public Q_SLOTS
 @brief addEntryWithDialog This gives a simple dialog for adding colors, with options like adding name, id, and to which group the color should be added.
@param color the default color to add
@return whether it was successful. """

	def addGroupWithDialog(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief addGroupWithDialog gives a little dialog to ask for the desired groupname.
@return whether this was successful. """

	def removeSelectedEntryWithDialog(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief removeSelectedEntryWithDialog removes the selected entry. If it is a group, it pop up a dialog asking whether the colors should also be removed.
@return whether this was successful """

	def trySelectClosestColor(self, color: 'ManagedColor') -> None:
		# type: (color) -> None:
		"""@access public Q_SLOTS
 @brief trySelectClosestColor tries to select the closest color to the one given. It does not force a change on the active color.
@param color the color to compare to. """

	def entrySelectedForeGround(self, entry: 'Swatch') -> None:
		# type: (entry) -> None:
		"""@access public Q_SLOTS
 @brief entrySelectedForeGround fires when a swatch is selected with leftclick.
@param entry """

	def entrySelectedBackGround(self, entry: 'Swatch') -> None:
		# type: (entry) -> None:
		"""@access public Q_SLOTS
 @brief entrySelectedBackGround fires when a swatch is selected with rightclick.
@param entry """

class GroupShape(Shape):
	"""* @brief The GroupShape class A group shape is a vector object with child shapes. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type returns the type.
@return "groupshape" """

	def children(self) -> List['Shape']:
		# type: () -> List[Shape]:
		"""@access public Q_SLOTS
 @brief children
@return the child shapes of this group shape. """

class GroupLayer(Node):
	"""* @brief The GroupLayer class A group layer is a layer that can contain other layers. In Krita, layers within a group layer are composited first before they are added into the composition code for where the group is in the stack. This has a significant effect on how it is interpreted for blending modes. PassThrough changes this behaviour. Group layer cannot be animated, but can contain animated layers or masks. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return grouplayer """

	def setPassThroughMode(self, passthrough: bool) -> None:
		# type: (passthrough) -> None:
		"""@access public Q_SLOTS
 @brief setPassThroughMode This changes the way how compositing works. Instead of compositing all the layers before compositing it with the rest of the image, the group layer becomes a sort of formal way to organise everything. Passthrough mode is the same as it is in photoshop, and the inverse of SVG's isolation attribute(with passthrough=false being the same as isolation="isolate").
@param passthrough whether or not to set the layer to passthrough. """

	def passThroughMode(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief passThroughMode
@return returns whether or not this layer is in passthrough mode. @see setPassThroughMode """

class FilterMask(Node):
	"""* @brief The FilterMask class A filter mask, unlike a filter layer, will add a non-destructive filter to the composited image of the node it is attached to. You can set grayscale pixeldata on the filter mask to adjust where the filter is applied. Filtermasks can be animated. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return The type of the node. Valid types are: <ul>  <li>paintlayer  <li>grouplayer  <li>filelayer  <li>filterlayer  <li>filllayer  <li>clonelayer  <li>vectorlayer  <li>transparencymask  <li>filtermask  <li>transformmask  <li>selectionmask  <li>colorizemask </ul> If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def setFilter(self, filter: 'Filter') -> None:
		# type: (filter) -> None:
		"""@access public Q_SLOTS
 """

class FilterLayer(Node):
	"""* @brief The FilterLayer class A filter layer will, when compositing, take the composited image up to the point of the location of the filter layer in the stack, create a copy and apply a filter. This means you can use blending modes on the filter layers, which will be used to blend the filtered image with the original. Similarly, you can activate things like alpha inheritance, or you can set grayscale pixeldata on the filter layer to act as a mask. Filter layers can be animated. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return "filterlayer" """

	def setFilter(self, filter: 'Filter') -> None:
		# type: (filter) -> None:
		"""@access public Q_SLOTS
 """

class FillLayer(Node):
	"""* @brief The FillLayer class A fill layer is much like a filter layer in that it takes a name and filter. It however specializes in filters that fill the whole canvas, such as a pattern or full color fill. """

	def __init__(self, filter: 'Filter') -> None:
		""" """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return The type of the node. Valid types are: <ul>  <li>paintlayer  <li>grouplayer  <li>filelayer  <li>filterlayer  <li>filllayer  <li>clonelayer  <li>vectorlayer  <li>transparencymask  <li>filtermask  <li>transformmask  <li>selectionmask  <li>colorizemask </ul> If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def setGenerator(self, generatorName: str, filterConfig: 'InfoObject') -> bool:
		# type: (generatorName, filterConfig) -> bool:
		"""@access public Q_SLOTS
 @brief setGenerator set the given generator for this fill layer
@param generatorName "pattern" or "color"
@param filterConfig a configuration object appropriate to the given generator plugin
@return true if the generator was correctly created and set on the layer """

class FileLayer(Node):
	"""* @brief The FileLayer class A file layer is a layer that can reference an external image and show said reference in the layer stack. If the external image is updated, Krita will try to update the file layer image as well. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return "filelayer" """

	def setProperties(self, fileName: str, scalingMethod: str = str("None"), scalingFilter: str = str("Bicubic")) -> None:
		# type: (fileName, scalingMethod, scalingFilter) -> None:
		"""@access public Q_SLOTS
 @brief setProperties Change the properties of the file layer.
@param fileName - A String containing the absolute file name.
@param scalingMethod - a string with the scaling method, defaults to "None",  other options are "ToImageSize" and "ToImagePPI"
@param scalingFilter - a string with the scaling filter, defaults to "Bicubic",  other options are "Hermite", "NearestNeighbor", "Bilinear", "Bell", "BSpline", "Lanczos3", "Mitchell" """

	def resetCache(self) -> None:
		# type: () -> None:
		"""@access public Q_SLOTS
 @brief makes the file layer to reload the connected image from disk """

	def path(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief path
@return A QString with the full path of the referenced image. """

	def scalingMethod(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief scalingMethod returns how the file referenced is scaled.
@return one of the following: <ul>  <li> None - The file is not scaled in any way.  <li> ToImageSize - The file is scaled to the full image size;  <li> ToImagePPI - The file is scaled by the PPI of the image. This keep the physical dimensions the same. </ul> """

	def scalingFilter(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief scalingFilter returns the filter with which the file referenced is scaled. """

	def getFileNameFromAbsolute(self, basePath: str, filePath: str) -> str:
		# type: (basePath, filePath) -> str:
		"""@access private
 @brief getFileNameFromAbsolute referenced from the fileLayer dialog, this will jumps through all the hoops to ensure that an appropriate filename will be gotten.
@param baseName the location of the document.
@param absolutePath the absolute location of the file referenced.
@return the appropriate relative path. """

class FileDialog(QDialog):
	"""* Wrapper around KoFileDialog, which is a wrapper around QFileDialog, providing native file dialogs on KDE/Gnome/Windows/OSX/etc. FileDialog respects Krita's "Don't use native file dialogs" setting. """

	def setDefaultDir(self, defaultDir: str, force: bool = False) -> None:
		# type: (defaultDir, force) -> None:
		"""@access public
 @brief constructor
@param parent The parent of the file dialog
@param dialogType usage of the file dialog Valid arguments: <ul> <li>FileDialog.DialogType.OpenFile</li> <li>FileDialog.DialogType.OpenFiles</li> <li>FileDialog.DialogType.OpenDirectory</li> <li>FileDialog.DialogType.ImportFile</li> <li>FileDialog.DialogType.ImportFiles</li> <li>FileDialog.DialogType.ImportDirectory</li> <li>FileDialog.DialogType.SaveFile</li> <ul>
@param dialogName the name for the file dialog. This will be used to open the filedialog in the last open location, instead of the specified directory.
@return The name of the entry user selected in the file dialog/
    FileDialog(QWidget *parent = nullptr,
               const FileDialog::DialogType = DialogType::OpenFile,
               const QString &dialogName = "");

    ~FileDialog() override;

    // Set the text in the dialog's title bar.
    // Not all native dialogs show this.
    void setCaption(const QString &caption);

    /**
@brief setDefaultDir set the default directory to defaultDir.
@param defaultDir a path to a file or directory """

	def setDirectoryUrl(self, defaultUri: QUrl) -> None:
		# type: (defaultUri) -> None:
		"""@access public
 @brief setDirectoryUrl set the default URI to defaultUri.
@param defaultUri a Uri to a file from some ContentProvider """

	def setImageFilters(self) -> None:
		# type: () -> None:
		"""@access public
 @brief setImageFilters sets the name filters for the file dialog to all image formats Qt's QImageReader supports. """

	@staticmethod
	def getOpenFileName(parent: QWidget = nullptr, caption: str = str(), directory: str = str(), filter: str = str(), selectedFilter: str = str(), dialogName: str = str()) ->  str:
		# type: (parent, caption, directory, filter, selectedFilter, dialogName) ->  str:
		"""@access public
 @brief setMimeTypeFilters Update the list of file filters from mime types.
@param mimeTypeList A list of mime types that forms the basis of this dialog's file filters
@param defaultMimeType Sets the default filter based on this mime type/
    void setMimeTypeFilters(const QStringList &mimeTypeList,
                            QString defaultMimeType = QString());

    // Set the file type filter
    void setNameFilter(const QString &filter);

    //Set the selected file type filter
    void selectNameFilter(const QString &filter);

    /// Show the file dialog and return multiple file names the user selected
    QStringList filenames();

    /// Show the file dialog and return the file name the user selected
    QString filename();

    /**
@brief Create and show a file dialog and return the name of an existing file selected by the user
@param parent Dialog parent widget
@param caption Dialog caption
@param directory Starting directory for the file dialog
@param filter Name filters for files shown
@param selectedFilter The selected name filter
@param dialogName Internal name of the dialog used for remembering the opened directory
@return the name of an existing file selected by the user """

	@staticmethod
	def getOpenFileNames(parent: QWidget = nullptr, caption: str = str(), directory: str = str(), filter: str = str(), selectedFilter: str = str(), dialogName: str = str()) ->  List[str]:
		# type: (parent, caption, directory, filter, selectedFilter, dialogName) ->  List[str]:
		"""@access public
 @brief Create and show a file dialog and return the name of multiple existing files selected by the user
@param parent Dialog parent widget
@param caption Dialog caption
@param directory Starting directory for the file dialog
@param filter Name filters for files shown
@param selectedFilter The selected name filter
@param dialogName Internal name of the dialog used for remembering the opened directory
@return the name of multiple existing files selected by the user """

	@staticmethod
	def getExistingDirectory(parent: QWidget = nullptr, caption: str = str(), directory: str = str(), dialogName: str = str()) ->  str:
		# type: (parent, caption, directory, dialogName) ->  str:
		"""@access public
 @brief Create and show a file dialog and return the name of an existing directory selected by the user
@param parent Dialog parent widget
@param caption Dialog caption
@param directory Starting directory for the file dialog
@param dialogName Internal name of the dialog used for remembering the opened directory
@return the name of an existing directory selected by the user """

	@staticmethod
	def getSaveFileName(parent: QWidget = nullptr, caption: str = str(), directory: str = str(), filter: str = str(), selectedFilter: str = str(), dialogName: str = str()) ->  str:
		# type: (parent, caption, directory, filter, selectedFilter, dialogName) ->  str:
		"""@access public
 @brief Create and show a file dialog and return the name of a file to save to selected by the user
@param parent Dialog parent widget
@param caption Dialog caption
@param directory Starting directory for the file dialog
@param filter Name filters for files shown
@param selectedFilter The selected name filter
@param dialogName Internal name of the dialog used for remembering the opened directory
@return the name of a file to save to selected by the user """

	def selectedNameFilter(self) -> str:
		# type: () -> str:
		"""@access public
 @brief selectedNameFilter returns the name filter the user selected, either    directory or by clicking on it.
@return """

	def selectedMimeType(self) -> str:
		# type: () -> str:
		"""@access public
 """

class DockWidgetFactoryBase(KoDockFactoryBase):
	"""* @brief The DockWidgetFactoryBase class is the base class for plugins that want to add a dock widget to every window. You do not need to implement this class yourself, but create a DockWidget implementation and then add the DockWidgetFactory to the Krita instance like this:
@code
class HelloDocker(DockWidget):
  def __init__(self):
      super().__init__()
      label = QLabel("Hello", self)
      self.setWidget(label)
      self.label = label
def canvasChanged(self, canvas):
      self.label.setText("Hellodocker: canvas changed");
Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))
@endcode """

class DockWidget(QDockWidget):
	"""* DockWidget is the base class for custom Dockers. Dockers are created by a factory class which needs to be registered by calling Application.addDockWidgetFactory:
@code
class HelloDocker(DockWidget):
  def __init__(self):
      super().__init__()
      label = QLabel("Hello", self)
      self.setWidget(label)
      self.label = label
      self.setWindowTitle("Hello Docker")
def canvasChanged(self, canvas):
      self.label.setText("Hellodocker: canvas changed");
Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))
@endcode One docker per window will be created, not one docker per canvas or view. When the user switches between views/canvases, canvasChanged will be called. You can override that method to reset your docker's internal state, if necessary. """

	def canvas(self) -> 'Canvas':
		# type: () -> Canvas:
		"""@access public
 @@return the canvas object that this docker is currently associated with """

	def canvasChanged(self, canvas: 'Canvas') -> None:
		# type: (canvas) -> None:
		"""@access public
 @brief canvasChanged is called whenever the current canvas is changed in the mainwindow this dockwidget instance is shown in.
@param canvas The new canvas. """

class ColorizeMask(Node):
	"""* @brief The ColorizeMask class A colorize mask is a mask type node that can be used to color in line art.
@code
window = Krita.instance().activeWindow()
doc = Krita.instance().createDocument(10, 3, "Test", "RGBA", "U8", "", 120.0)
window.addView(doc)
root = doc.rootNode();
node = doc.createNode("layer", "paintLayer")
root.addChildNode(node, None)
nodeData = QByteArray.fromBase64(b"AAAAAAAAAAAAAAAAEQYMBhEGDP8RBgz/EQYMAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARBgz5EQYM/xEGDAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQYMAhEGDAkRBgwCAAAAAAAAAAAAAAAA");
node.setPixelData(nodeData,0,0,10,3)

cols = [ ManagedColor('RGBA','U8',''), ManagedColor('RGBA','U8','') ]
cols[0].setComponents([0.65490198135376, 0.345098048448563, 0.474509805440903, 1.0]);
cols[1].setComponents([0.52549022436142, 0.666666686534882, 1.0, 1.0]);
keys = [
        QByteArray.fromBase64(b"/48AAAAAAAAAAAAAAAAAAAAAAACmCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
        QByteArray.fromBase64(b"AAAAAAAAAACO9ocAAAAAAAAAAAAAAAAAAAAAAMD/uQAAAAAAAAAAAAAAAAAAAAAAGoMTAAAAAAAAAAAA")
        ]

mask = doc.createColorizeMask('c1')
node.addChildNode(mask,None)
mask.setEditKeyStrokes(True)

mask.setUseEdgeDetection(True)
mask.setEdgeDetectionSize(4.0)
mask.setCleanUpAmount(70.0)
mask.setLimitToDeviceBounds(True)
mask.initializeKeyStrokeColors(cols)

for col,key in zip(cols,keys):
    mask.setKeyStrokePixelData(key,col,0,0,20,3)

mask.updateMask()
mask.setEditKeyStrokes(False);
mask.setShowOutput(True);
@endcode """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return colorizemask If the Node object isn't wrapping a valid Krita layer or mask object, and empty string is returned. """

	def keyStrokesColors(self) -> List['ManagedColor']:
		# type: () -> List[ManagedColor]:
		"""@access public Q_SLOTS
 @brief keyStrokesColors Colors used in the Colorize Mask's keystrokes.
@return a ManagedColor list containing the colors of keystrokes. """

	def initializeKeyStrokeColors(self, colors: List['ManagedColor'], transparentIndex: int = -1) -> None:
		# type: (colors, transparentIndex) -> None:
		"""@access public Q_SLOTS
 @brief initializeKeyStrokeColors Set the colors to use for the Colorize Mask's keystrokes.
@param colors a list of ManagedColor to use for the keystrokes.
@param transparentIndex index of the color that should be marked as transparent. """

	def removeKeyStroke(self, color: 'ManagedColor') -> None:
		# type: (color) -> None:
		"""@access public Q_SLOTS
 @brief removeKeyStroke Remove a color from the Colorize Mask's keystrokes.
@param color a ManagedColor to be removed from the keystrokes. """

	def transparencyIndex(self) -> int:
		# type: () -> int:
		"""@access public Q_SLOTS
 @brief transparencyIndex Index of the transparent color.
@return an integer containing the index of the current color marked as transparent. """

	def keyStrokePixelData(self, color: 'ManagedColor', x: int, y: int, w: int, h: int) -> QByteArray:
		# type: (color, x, y, w, h) -> QByteArray:
		"""@access public Q_SLOTS
 @brief keyStrokePixelData reads the given rectangle from the keystroke image data and returns it as a byte array. The pixel data starts top-left, and is ordered row-first.
@param color a ManagedColor to get keystrokes pixeldata from.
@param x x position from where to start reading
@param y y position from where to start reading
@param w row length to read
@param h number of rows to read
@return a QByteArray with the pixel data. The byte array may be empty. """

	def setKeyStrokePixelData(self, value: Union[QByteArray, bytes, bytearray], color: 'ManagedColor', x: int, y: int, w: int, h: int) -> bool:
		# type: (value, color, x, y, w, h) -> bool:
		"""@access public Q_SLOTS
 @brief setKeyStrokePixelData writes the given bytes, of which there must be enough, into the keystroke, the keystroke's original pixels are overwritten
@param value the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (number of channels * size of channel * w * h) bytes are read.
@param color a ManagedColor to set keystrokes pixeldata for.
@param x the x position to start writing from
@param y the y position to start writing from
@param w the width of each row
@param h the number of rows to write
@return true if writing the pixeldata worked """

	def setUseEdgeDetection(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setUseEdgeDetection Activate this for line art with large solid areas, for example shadows on an object.
@param value true to enable edge detection, false to disable. """

	def useEdgeDetection(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief useEdgeDetection
@return true if Edge detection is enabled, false if disabled. """

	def setEdgeDetectionSize(self, value: float) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setEdgeDetectionSize Set the value to the thinnest line on the image.
@param value a float value of the edge size to detect in pixels. """

	def edgeDetectionSize(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief edgeDetectionSize
@return a float value of the edge detection size in pixels. """

	def setCleanUpAmount(self, value: float) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setCleanUpAmount This will attempt to handle messy strokes that overlap the line art where they shouldn't.
@param value a float value from 0.0 to 100.00 where 0.0 is no cleanup is done and 100.00 is most aggressive. """

	def cleanUpAmount(self) -> float:
		# type: () -> float:
		"""@access public Q_SLOTS
 @brief cleanUpAmount
@return a float value of 0.0 to 100.0 representing the cleanup amount where 0.0 is no cleanup is done and 100.00 is most aggressive. """

	def setLimitToDeviceBounds(self, value: bool) -> None:
		# type: (value) -> None:
		"""@access public Q_SLOTS
 @brief setLimitToDeviceBounds Limit the colorize mask to the combined layer bounds of the strokes and the line art it is filling. This can speed up the use of the mask on complicated compositions, such as comic pages.
@param value set true to enabled limit bounds, false to disable. """

	def limitToDeviceBounds(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief limitToDeviceBounds
@return true if limit bounds is enabled, false if disabled. """

	def updateMask(self, force: bool = False) -> None:
		# type: (force) -> None:
		"""@access public Q_SLOTS
 @brief updateMask Process the Colorize Mask's keystrokes and generate a projection of the computed colors.
@param force force an update """

	def showOutput(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief showOutput Show output mode allows the user to see the result of the Colorize Mask's algorithm.
@return true if edit show coloring mode is enabled, false if disabled. """

	def setShowOutput(self, enabled: bool) -> None:
		# type: (enabled) -> None:
		"""@access public Q_SLOTS
 @brief setShowOutput Toggle Colorize Mask's show output mode.
@param enabled set true to enable show coloring mode and false to disable it. """

	def editKeyStrokes(self) -> bool:
		# type: () -> bool:
		"""@access public Q_SLOTS
 @brief editKeyStrokes Edit keystrokes mode allows the user to modify keystrokes on the active Colorize Mask.
@return true if edit keystrokes mode is enabled, false if disabled. """

	def setEditKeyStrokes(self, enabled: bool) -> None:
		# type: (enabled) -> None:
		"""@access public Q_SLOTS
 @brief setEditKeyStrokes Toggle Colorize Mask's edit keystrokes mode.
@param enabled set true to enable edit keystrokes mode and false to disable it. """

class CloneLayer(Node):
	"""* @brief The CloneLayer class A clone layer is a layer that takes a reference inside the image and shows the exact same pixeldata. If the original is updated, the clone layer will update too. """

	def __init__(self, enabled: bool) -> None:
		""" @brief setEditKeyStrokes Toggle Colorize Mask's edit keystrokes mode.
@param enabled set true to enable edit keystrokes mode and false to disable it. """

	def type(self) -> str:
		# type: () -> str:
		"""@access public Q_SLOTS
 @brief type Krita has several types of nodes, split in layers and masks. Group layers can contain other layers, any layer can contain masks.
@return clonelayer """

	def sourceNode(self) -> 'Node':
		# type: () -> Node:
		"""@access public Q_SLOTS
 @brief sourceNode
@return the node the clone layer is based on. """

	def setSourceNode(self, node: 'Node') -> None:
		# type: (node) -> None:
		"""@access public Q_SLOTS
 @brief setSourceNode
@param node the node to use as the source of the clone layer. """
