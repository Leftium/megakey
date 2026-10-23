# MegaKey

MegaKey gives five modifier combinations names and single-key shortcuts. On macOS, hold Caps Lock for Control+Option+Command (Mega), or hold Tab to add Shift (Giga). With the optional clipboard demo enabled, Caps Lock+C copies and Caps Lock+V pastes.

![MegaKey keyboard layout](https://leftium.github.io/megakey/assets/keyboard.png)

If you already use Hyper or Meh, the idea will be familiar. MegaKey adds a vocabulary for five related combinations and Karabiner-Elements rules to reach them. Karabiner does the remapping; MegaKey supplies the names and configuration.

| Symbol | Name | Hold this key | Sends | Relation to Mega |
|:------:|------|---------------|-------|------------------|
| ⁂ | Mega | Caps Lock | Control+Option+Command | Base combination |
| ❖ | Giga | Tab | Shift+Control+Option+Command | Add Shift |
| ❋ | Chaos | Right Control | Option+Command | Remove Control |
| ▲ | Force | Right Option | Control+Command | Remove Option |
| ⭑ | Wish | Right Command | Control+Option | Remove Command |

The supplied rules require macOS and [Karabiner-Elements](https://karabiner-elements.pqrs.org/). The naming concept can be used on other platforms, but this repository has no Windows or Linux implementation. These combinations can still conflict with existing shortcuts.

## Try it

Follow the [Quick Start](https://leftium.github.io/megakey/#quick-start) to import `megakey.json`, which preserves Caps Lock on tap, and enable only the rules you want. The optional clipboard demo gives you a shortcut to test immediately. An [Escape-on-tap variant](https://leftium.github.io/megakey/installation#choose-a-variant) is also available.

Tab still sends Tab when tapped. Enabling a right modifier rule replaces that key's original behavior. You can remove individual rules in Karabiner to restore it.

[Installation and removal](https://leftium.github.io/megakey/installation) | [Modifier guide](https://leftium.github.io/megakey/modifiers) | [Behavior reference](https://leftium.github.io/megakey/etc)

## Validation

Run `python3 scripts/validate.py` for configuration regression checks. If Karabiner is installed, also run `karabiner_cli --lint-complex-modifications 'megakey*.json'`. Physical keyboard and app checks are listed in the [behavior reference](https://leftium.github.io/megakey/etc#manual-checks).

## License

[MIT](LICENSE)
