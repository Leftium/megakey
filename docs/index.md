[GitHub Repository](https://github.com/Leftium/megakey#README)

## Standardization and extension of the Hyper (and Meh) key

![](https://leftium.github.io/megakey/assets/keyboard.png)

### A system of 5 pseudo-modifier keys that works on standard keyboards
- Keyboard shortcuts that don't conflict with system or app bindings.
- Can bind `Mega` for universal cut/copy/paste/etc on both Windows (`Ctrl`) and MacOS (`Cmd`). (Plus `Mega` is more comfortable/ergonomic!)
- Opens up memorable keys like `Chaos-V` for pasting from clipboard history.
- Especially useful for global keybindings such as those required for transcription tools and windows managers.
 
MegaKey consists of two parts:

#### 1. Mental tools (for your mind)

- Simplify complex combinations of modifiers to a single word or symbol.
- 5 pseudo-modifiers designed as single pseudo-modifier with 4 extra variations.
- Easier to remember/read/write/dictate: `Giga-C` (<kbd>❖</kbd><kbd>C</kbd>) vs `Shift-Ctrl-Option-Cmd-C` (<kbd>⇧</kbd><kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘C</kbd>).
- The mental tools are cross-platform and work with standard keyboard layouts.

#### 2. Software tools (for your fingers)

- Simplify complex/awkward combinations of modifiers to a single keypress via [Karabiner-Elements](https://karabiner-elements.pqrs.org/)
- For example: `CapsLock` converts to `Ctrl-Option-Cmd` (tapping `CapsLock` by itself still results in `CapsLock`)
- Presently MacOS-only, but straight-forward to implement on other platforms.

## The 5 new pseudo-modifier keys

|        | Name  | Single Key              | Multiple Keys                                               | Notes             |
|-------:|-------|-------------------------|------------------------------------------------------------:|-------------------|
| **⁂** | Mega  | <kbd>CapsLock</kbd>     | <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd>                 | Base combination  |
| **❖** | Giga  | <kbd>Tab</kbd>          | <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd> | Mega with Shift   |
| **⭑** | Wish  | <kbd>Right Cmd</kbd>    | <kbd>Ctrl</kbd><kbd>Opt</kbd>                               | Mega without Cmd  |
| **▲** | Force | <kbd>Right Option</kbd> | <kbd>Ctrl</kbd><kbd>Cmd</kbd>                               | Mega without Opt  |
| **❋** | Chaos | <kbd>Right Ctrl</kbd>   | <kbd>Opt</kbd><kbd>Cmd</kbd>                                | Mega without Ctrl |

See detailed [pseudo-modifier guide](https://leftium.github.io/megakey/modifiers) for:
- Design rationale
- Mnemonics to help remember
- Windows/Linux version
- Prior art

## Quick Start

1. Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/)
2. Import the MegaKey rule: [Caps Lock → MegaKey](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json)
3. Enable it in Karabiner-Elements → Complex Modifications

That's it! Hold Caps Lock to activate MegaKey. Tap it for Escape.

> [!TIP]
>
> Press Fn+CapsLock to toggle Caps Lock on/off.

See detailed [installation guide](https://leftium.github.io/megakey/installation) for:
- Manual installation
- Version that preserves CapsLock

## License

MIT
