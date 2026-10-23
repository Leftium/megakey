[GitHub repository](https://github.com/Leftium/megakey)

# MegaKey

- A proposed standardization and extension of the Hyper (and Meh) key
- A system of 5 pseudo-modifier keys that works on standard keyboards

![MegaKey keyboard layout](assets/keyboard.png)

- [Mental tools (for your mind)](#1-mental-tools-for-your-mind): names and symbols for thinking about shortcuts.
- [Software tools (for your fingers)](#2-software-tools-for-your-fingers): single-key mappings via [Karabiner-Elements](https://karabiner-elements.pqrs.org/) on macOS.
- With the optional clipboard demo, <kbd>Caps Lock</kbd>+<kbd>C</kbd> copies and <kbd>Caps Lock</kbd>+<kbd>V</kbd> pastes.

## Mental tools + Software tools

### 1. Mental tools (for your mind)

- Give a modifier combination a name and symbol: `Giga+C` (❖C) instead of <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd>+<kbd>C</kbd>.
- Think of Mega as the base pseudo-modifier, with four variations that each add or remove one modifier.
- Use the names to think about, read, write, or dictate shortcuts. The naming concept is platform-neutral.

### 2. Software tools (for your fingers)

- Reach a modifier combination with one physical key using [Karabiner-Elements](https://karabiner-elements.pqrs.org/).
- Hold <kbd>Caps Lock</kbd> for Mega; tap it alone for <kbd>Caps Lock</kbd> in the default configuration.
- The supplied rules are macOS-only. There is no Windows or Linux implementation in this repository.

## The five pseudo-modifiers

| Symbol | Name | Physical key (hold) | Equivalent keys | ⇧ | ⌃ | ⌥ | ⌘ | Relation to Mega |
|:------:|------|---------------------|-----------------|---|---|---|---|------------------|
| ⁂ | Mega | <kbd>Caps Lock</kbd> | <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> | | ⌃ | ⌥ | ⌘ | Base combination |
| ❖ | Giga | <kbd>Tab</kbd> | <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> | ⇧ | ⌃ | ⌥ | ⌘ | Add Shift |
| ❋ | Chaos | <kbd>Right Ctrl</kbd> | <kbd>Opt</kbd>+<kbd>Cmd</kbd> | | | ⌥ | ⌘ | Remove Control |
| ▲ | Force | <kbd>Right Option</kbd> | <kbd>Ctrl</kbd>+<kbd>Cmd</kbd> | | ⌃ | | ⌘ | Remove Option |
| ⭑ | Wish | <kbd>Right Cmd</kbd> | <kbd>Ctrl</kbd>+<kbd>Opt</kbd> | | ⌃ | ⌥ | | Remove Command |

These are names used by this project, not an adopted keyboard standard. You can assign the combinations in apps that accept custom shortcuts, though existing system or app bindings may already use them.

## Quick Start

You need macOS, a keyboard with <kbd>Caps Lock</kbd>, and Karabiner-Elements installed with its required permissions granted. You only need <kbd>Tab</kbd> and the right modifier keys if you enable their rules.

1. Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/) and finish its setup prompts.
2. [Import MegaKey (Caps Lock tap stays Caps Lock)](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json). If the link does not open, use the [manual installation](installation#manual-installation).
3. In Karabiner-Elements, open **Complex Modifications**, choose **Add rule** (or **Add predefined rule**), and enable the **Caps Lock** rule and **Optional clipboard demo** individually. Leave the other rules disabled for now.
4. In a text editor, type and select a few words. Hold <kbd>Caps Lock</kbd>, press <kbd>C</kbd>, then release both keys. Move the cursor, hold <kbd>Caps Lock</kbd>, and press <kbd>V</kbd>. The copied words should appear.

Without the optional demo, Mega+C/V sends the full <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> combination; it does not automatically copy or paste. The demo overrides those two combinations, including when you press the three modifiers directly. Leave it disabled if you already use those shortcuts.

With the demo enabled:

- <kbd>Shift</kbd>+<kbd>Caps Lock</kbd>+<kbd>V</kbd> sends <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>, used for paste without formatting in Google Docs and many web apps. Other apps may assign it differently.
- <kbd>Shift</kbd>+<kbd>Caps Lock</kbd>+<kbd>C</kbd> sends <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd>, whose action also depends on the app.

Prefer to check the keys without touching the clipboard? Leave the demo disabled and open Karabiner-EventViewer. Hold <kbd>Caps Lock</kbd> and press a letter: expect Control, Option, and Command with that letter. [More checks](etc#manual-checks) cover all five combinations.

## Choose what to remap

- The default file preserves <kbd>Caps Lock</kbd> when tapped. The [Escape variant](installation#choose-a-variant) sends <kbd>Esc</kbd> instead.
- Both retain <kbd>Tab</kbd> on tap. Tap actions require releasing the key alone within Karabiner's timeout (normally one second).
- Enable the <kbd>Tab</kbd> or right modifier rules only if you want them. <kbd>Tab</kbd> becomes Giga while held; the right modifiers lose their original function while their rules are enabled.
- <kbd>Fn</kbd>+<kbd>Caps Lock</kbd> can toggle <kbd>Caps Lock</kbd> in either variant if your keyboard exposes Fn to Karabiner. Some keyboards handle Fn internally.

To undo a mapping, remove its enabled entry from **Complex Modifications**. See [installation and removal](installation), the [modifier guide](modifiers), and the [behavior reference](etc).

## License

[MIT](https://github.com/Leftium/megakey/blob/main/LICENSE)
