# MegaKey

> **Hyper key standardized and extended**

MegaKey transforms your keyboard with 5 custom modifier combinations using [Karabiner-Elements](https://karabiner-elements.pqrs.org/), giving you conflict-free shortcuts that don't clash with system or app bindings.

## The Modifier System

| Symbol | Name | Physical Key | Modifiers | Notes |
|--------|------|--------------|----------:|-------|
| **⁂** | Mega | <kbd>CapsLock</kbd> | ⌃⌥⌘ | The foundation |
| **❖** | Giga | <kbd>Tab</kbd> | ⇧⌃⌥⌘ | Mega + Shift |
| **❋** | Chaos | <kbd>Right Ctrl</kbd> | ⌃⌥ | Mega - Cmd |
| **▲** | Force | <kbd>Right Option</kbd> | ⌃⌘ | Mega - Opt |
| **⭑** | Wish | <kbd>Right Cmd</kbd> | ⌥⌘ | Mega - Ctrl |

### Mega is the Center

Mega (⌃⌥⌘) is the foundation. All other modifiers derive from it:

```
              ❖ Giga (⇧⌃⌥⌘)
                ↑ +Shift
                │
 ❋ Chaos ←───── ⁂ Mega ─────→ ⭑ Wish
   (⌃⌥)         (⌃⌥⌘)          (⌥⌘)
   -Cmd           │            -Ctrl
                  ↓
                ▲ Force (⌃⌘)
                  -Opt
```

### Why Mega/Giga Instead of Hyper/Meh?

The terms "Hyper" and "Meh" are ambiguous:
- **Hyper**: Sometimes ⇧⌃⌥⌘ (all 4), sometimes ⌃⌥⌘ (without Shift)
- **Meh**: Sometimes ⌃⌥⇧ (without Cmd), sometimes ⌃⌥⌘ (without Shift)

**Mega/Giga are unambiguous** and follow SI prefix progression (Mega → Giga = 1000x bigger).

## Installation

### Prerequisites

Install [Karabiner-Elements](https://karabiner-elements.pqrs.org/) first.

### Option 1: Import URL (Recommended)

Copy and paste one of the following URLs into your browser:

**Default** (CapsLock tap → CapsLock):

```
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json
```

**Esc variant** (CapsLock tap → Esc):

```
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json
```

### Option 2: Manual Installation

1. Download `megakey.json` or `megakey-esc.json`
2. Copy to `~/.config/karabiner/assets/complex_modifications/`
3. Open Karabiner-Elements → Complex Modifications → Add Rule
4. Enable the MegaKey rules

## Key Behaviors

### Hold vs Tap

| Key | Hold | Tap |
|-----|------|-----|
| <kbd>CapsLock</kbd> | ⁂ Mega (⌃⌥⌘) | CapsLock (or Esc) |
| <kbd>Tab</kbd> | ❖ Giga (⇧⌃⌥⌘) | Tab |
| <kbd>Right Ctrl</kbd> | ❋ Chaos (⌃⌥) | - |
| <kbd>Right Option</kbd> | ▲ Force (⌃⌘) | - |
| <kbd>Right Cmd</kbd> | ⭑ Wish (⌥⌘) | - |

### Shifted Modifiers

Add <kbd>Shift</kbd> to any modifier for even more combinations:

| Combo | Result |
|-------|--------|
| <kbd>Shift</kbd>+<kbd>CapsLock</kbd> | ❖ Giga (⇧⌃⌥⌘) |
| <kbd>Shift</kbd>+<kbd>Right Ctrl</kbd> | ⇧❋ Shift+Chaos (⇧⌃⌥) |
| <kbd>Shift</kbd>+<kbd>Right Option</kbd> | ⇧▲ Shift+Force (⇧⌃⌘) |
| <kbd>Shift</kbd>+<kbd>Right Cmd</kbd> | ⇧⭑ Shift+Wish (⇧⌥⌘) |

## Versions

Choose one:

- **megakey.json** - CapsLock tap sends CapsLock (preserves toggle functionality)
- **megakey-esc.json** - CapsLock tap sends Esc (popular for Vim users)

## License

MIT
