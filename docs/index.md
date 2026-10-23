[GitHub repository](https://github.com/Leftium/megakey)

# MegaKey

MegaKey gives five modifier combinations names and single-key shortcuts. Hold Caps Lock for Mega (Control+Option+Command), or hold Tab for Giga (Shift+Control+Option+Command). With the optional clipboard demo enabled, Mega+C copies and Mega+V pastes.

![MegaKey keyboard layout](assets/keyboard.png)

Hyper and Meh mappings use the same basic idea: put several modifiers on one key. MegaKey names five related combinations so you can describe a shortcut as `Chaos+V` or `Giga+C` instead of spelling out every modifier. It uses [Karabiner-Elements](https://karabiner-elements.pqrs.org/) for the actual remapping.

| Symbol | Name | Hold this key | Sends | Relation to Mega |
|:------:|------|---------------|-------|------------------|
| ⁂ | Mega | Caps Lock | Control+Option+Command | Base combination |
| ❖ | Giga | Tab | Shift+Control+Option+Command | Add Shift |
| ❋ | Chaos | Right Control | Option+Command | Remove Control |
| ▲ | Force | Right Option | Control+Command | Remove Option |
| ⭑ | Wish | Right Command | Control+Option | Remove Command |

These are names used by this project, not an adopted keyboard standard. The naming concept is platform-neutral; the supplied software is macOS-only. You can assign these combinations in apps that accept custom shortcuts, though existing system or app bindings may already use them.

## Quick Start

You need macOS, a keyboard with Caps Lock, and Karabiner-Elements installed with its required permissions granted. You only need Tab and the right modifier keys if you enable their rules.

1. Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/) and finish its setup prompts.
2. [Import MegaKey (Caps Lock tap stays Caps Lock)](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json). If the link does not open, use the [manual installation](installation#manual-installation).
3. In Karabiner-Elements, open **Complex Modifications**, choose **Add rule** (or **Add predefined rule**), and enable the **Caps Lock** rule and **Optional clipboard demo** individually. Leave the other rules disabled for now.
4. In a text editor, type and select a few words. Hold Caps Lock, press C, then release both keys. Move the cursor, hold Caps Lock, and press V. The copied words should appear.

Without the optional demo, Mega+C/V sends the full Control+Option+Command combination; it does not automatically copy or paste. The demo overrides those two combinations, including when you press the three modifiers directly. Leave it disabled if you already use those shortcuts.

With the demo enabled, Shift+Caps Lock+V sends Command+Shift+V, used for paste without formatting in Google Docs and many web apps. Other apps may assign it differently. Shift+Caps Lock+C sends Command+Shift+C, whose action also depends on the app.

Prefer to check the keys without touching the clipboard? Leave the demo disabled and open Karabiner-EventViewer. Hold Caps Lock and press a letter: expect Control, Option, and Command with that letter. [More checks](etc#manual-checks) cover all five combinations.

## Choose what to remap

The default file preserves Caps Lock when tapped. The [Escape variant](installation#choose-a-variant) sends Escape instead. Both retain Tab on tap. Tap actions require releasing the key alone within Karabiner's timeout (normally one second).

Enable the Tab or right modifier rules only if you want them. Tab becomes Giga while held, and the right modifiers lose their original function while their rules are enabled. Fn+Caps Lock can toggle Caps Lock in either variant if your keyboard exposes Fn to Karabiner; some keyboards handle Fn internally.

To undo a mapping, remove its enabled entry from **Complex Modifications**. See [installation and removal](installation), the [modifier guide](modifiers), and the [behavior reference](etc).

## License

[MIT](https://github.com/Leftium/megakey/blob/main/LICENSE)
