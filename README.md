# MegaKey

- A proposed standardization and extension of the Hyper (and Meh) key
- A system of 5 pseudo-modifier keys that works on standard keyboards

![MegaKey keyboard layout](https://leftium.github.io/megakey/assets/keyboard.png)

- [Mental tools (for your mind)](https://leftium.github.io/megakey/#1-mental-tools-for-your-mind): names and symbols for thinking about shortcuts.
- [Software tools (for your fingers)](https://leftium.github.io/megakey/#2-software-tools-for-your-fingers): single-key mappings via [Karabiner-Elements](https://karabiner-elements.pqrs.org/) on macOS.
- With the optional clipboard demo, <kbd>Caps Lock</kbd>+<kbd>C</kbd> copies and <kbd>Caps Lock</kbd>+<kbd>V</kbd> pastes.

| Symbol | Name | Physical key (hold) | Equivalent keys | ⇧ | ⌃ | ⌥ | ⌘ | Relation to Mega |
|:------:|------|---------------------|-----------------|---|---|---|---|------------------|
| ⁂ | Mega | <kbd>Caps Lock</kbd> | <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> | | ⌃ | ⌥ | ⌘ | Base combination |
| ❖ | Giga | <kbd>Tab</kbd> | <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> | ⇧ | ⌃ | ⌥ | ⌘ | Add Shift |
| ❋ | Chaos | <kbd>Right Ctrl</kbd> | <kbd>Opt</kbd>+<kbd>Cmd</kbd> | | | ⌥ | ⌘ | Remove Control |
| ▲ | Force | <kbd>Right Option</kbd> | <kbd>Ctrl</kbd>+<kbd>Cmd</kbd> | | ⌃ | | ⌘ | Remove Option |
| ⭑ | Wish | <kbd>Right Cmd</kbd> | <kbd>Ctrl</kbd>+<kbd>Opt</kbd> | | ⌃ | ⌥ | | Remove Command |

- The supplied rules require macOS and [Karabiner-Elements](https://karabiner-elements.pqrs.org/).
- The naming concept can be used on other platforms; this repository has no Windows or Linux implementation.
- These combinations can still conflict with existing shortcuts.

## Try it

Follow the [Quick Start](https://leftium.github.io/megakey/#quick-start) to import `megakey.json`, which preserves <kbd>Caps Lock</kbd> on tap, and enable only the rules you want. The optional clipboard demo gives you a shortcut to test immediately. An [Escape-on-tap variant](https://leftium.github.io/megakey/installation#choose-a-variant) is also available.

- <kbd>Tab</kbd> still sends <kbd>Tab</kbd> when tapped.
- Enabling a right modifier rule replaces that key's original behavior. Remove its rule in Karabiner to restore it.

[Installation and removal](https://leftium.github.io/megakey/installation) | [Modifier guide](https://leftium.github.io/megakey/modifiers) | [Behavior reference](https://leftium.github.io/megakey/etc) | [Useful shortcuts](https://leftium.github.io/megakey/shortcuts)

## Validation

Run `python3 scripts/validate.py` for configuration regression checks. If Karabiner is installed, also run `karabiner_cli --lint-complex-modifications 'megakey*.json'`. Physical keyboard and app checks are listed in the [behavior reference](https://leftium.github.io/megakey/etc#manual-checks).

## License

[MIT](LICENSE)
