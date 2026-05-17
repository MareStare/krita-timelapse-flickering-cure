# Krita Timelapse Flickering Cure

This is Krita plugin, that removes white frames from timelapse data before rendering it. It is a workaround for [the long-standing bug in Krita builtin Recorder](https://bugs.kde.org/show_bug.cgi?id=476326).

## Installation

1. Open Krita.
2. Go `Tools > Scripts > Import Plugin from Web...`
3. Paste this link: https://github.com/MareStare/krita-timelapse-flickering-cure
4. Restart Krita.

If you did everything right, you should see `Export (without flickering)` button in your Recorder docker.

## Development

Clone this repository and create symlinks to `timelapse_flickering_cure.desktop` file and `timelapse_flickering_cure` folder in your `{KritaResources}/pykrita` directory. You can find the location of your `{KritaResources}` directory in Krita `Settings > Configure Krita > Resources` section.

If you are on windows, don't create "shortcuts" via Windows context menu. Instead, run a terminal as an administrator and use these commands (replace `$repo` with your repository path):

```ps1
New-Item -ItemType SymbolicLink -Path timelapse_flickering_cure.desktop -Target "$repo\timelapse_flickering_cure.desktop"
New-Item -ItemType SymbolicLink -Path timelapse_flickering_cure         -Target "$repo\timelapse_flickering_cure"
```

## License

<sup>
Licensed under <a href="https://github.com/MareStare/krita-maregrind/blob/master/LICENSE-MIT">MIT license</a>.
</sup>

<br>

<sub>
Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
</sub>
