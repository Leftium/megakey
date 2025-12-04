[GitHub Repository](https://github.com/Leftium/megakey#README)

## Standardization and extension of the Hyper (and Meh) key

![](https://leftium.github.io/megakey/assets/keyboard.png)

### A system of 5 pseudo-modifier keys that works on standard keyboards
- Useful for (global) keyboard shortcuts that don't clash with system or app bindings.
- Can bind `Mega` for universal cut/copy/paste/etc on both Windows (`Ctrl`) and MacOS (`Cmd`). (Plus `Mega` is more comfortable/ergonomic!)
- Free to choose memorable keys like `Chaos-V` for pasting from clipboard history.
- Especially helpful for window managers that require several global keybindings.
 
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

|        | Name  | Single Key              | Multiple Keys                                               | ⇧ | ⌃ | ⌥ | ⌘ | Notes             |
|-------:|-------|-------------------------|-------------------------------------------------------------|---|---|---|---|-------------------|
| **⁂** | Mega  | <kbd>CapsLock</kbd>     | <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd>                 |   | ⌃ | ⌥ | ⌘ | Base combination  |
| **❖** | Giga  | <kbd>Tab</kbd>          | <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd> | ⇧ | ⌃ | ⌥ | ⌘ | Mega with Shift   |
| **⭑** | Wish  | <kbd>Right Cmd</kbd>    | <kbd>Ctrl</kbd><kbd>Opt</kbd>                               |   | ⌃ | ⌥ |   | Mega without Cmd  |
| **▲** | Force | <kbd>Right Option</kbd> | <kbd>Ctrl</kbd><kbd>Cmd</kbd>                               |   | ⌃ |   | ⌘ | Mega without Opt  |
| **❋** | Chaos | <kbd>Right Ctrl</kbd>   | <kbd>Opt</kbd><kbd>Cmd</kbd>                                |   |   | ⌥ | ⌘ | Mega without Ctrl |



### The 4 variations of Mega differ by a single modifier key:
```
             Shift added
             ❖ Giga
                 ↑
⭑ Wish ←──── ⁂ Mega ────→ ❋ Chaos 
Cmd removed      │        Ctrl removed
                 ↓
             ▲ Force
             Opt removed                
```


## Quick Start

1. Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/)
2. Import the MegaKey rule: [Caps Lock → MegaKey](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json)
3. Enable it in Karabiner-Elements → Complex Modifications

That's it! Hold Caps Lock to activate MegaKey. Tap it for Escape.

> [!TIP]
> Press Fn+CapsLock to toggle Caps Lock on/off.

## Installation

### Prerequisites

Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/) first.

### Option 1: Import URL (Recommended)

Copy and paste one of the following URLs into your browser:

[**Default** (CapsLock tap → CapsLock)](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json):

```
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json
```


[**Esc variant** (CapsLock tap → Esc)](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json):

```
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json
```

### Option 2: Manual Installation

1. Download `megakey.json` or `megakey-esc.json`
2. Copy to `~/.config/karabiner/assets/complex_modifications/`
3. Open Karabiner-Elements → Complex Modifications → Add Rule
4. Enable the MegaKey rules

## Versions

Choose one:

- **megakey.json** - CapsLock tap sends CapsLock (preserves toggle functionality)
- **megakey-esc.json** - CapsLock tap sends Esc (popular for Vim users)

> [!TIP]
> Both versions support Fn+CapsLock to toggle Caps Lock on/off.

## License

MIT
