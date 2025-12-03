# Modifier Details

## Mega is the Center

Mega is the foundation. All other modifiers derive from it:

**macOS:**
```
              ❖ Giga (⇧⌃⌥⌘)
                ↑ +Shift
                │
 ⭑ Wish ←───── ⁂ Mega ─────→ ❋ Chaos
   (⌃⌥)         (⌃⌥⌘)          (⌥⌘)
  -Cmd          │             -Ctrl
                ↓
              ▲ Force (⌃⌘)
                -Opt
```

**Windows/Linux:**
```
               ❖ Giga (Shift+Ctrl+Win+Alt)
                 ↑ +Shift
                 │
 ⭑ Main ←────── ⁂ Mega ──────→ ❋ Chaos
 (Ctrl+Win)    (Ctrl+Win+Alt)  (Win+Alt)
   -Alt          │              -Ctrl
                 ↓
               ▲ Sub (Ctrl+Alt)
                  -Win
```

## Why Mega/Giga Instead of Hyper/Meh?

The terms "Hyper" and "Meh" are ambiguous:
- **Hyper**: Sometimes ⇧⌃⌥⌘ (all 4), sometimes ⌃⌥⌘ (without Shift)
- **Meh**: Sometimes ⌃⌥⇧ (without Cmd), sometimes ⌃⌥⌘ (without Shift)

**Mega/Giga are unambiguous** and follow SI prefix progression (Mega → Giga = 1000x bigger).

## Cross-Platform Names

Each modifier name relates to the key it **omits** (opposite meaning):

| macOS | Win/Linux | Omit (macOS) | Omit (Win/Linux) | Position | Keys (macOS) | Keys (Win/Linux) |
|-------|-----------|--------------|------------------|----------|--------------|------------------|
| Chaos | Chaos     | Ctrl         | Ctrl             | Outside  | Opt-Cmd      | Win/Super-Alt    |
| Force | Sub       | Option       | Win/Super        | Middle   | Ctrl-Cmd     | Ctrl-Alt         |
| Wish  | Main      | Cmd          | Alt              | Inside   | Ctrl-Opt     | Ctrl-Win/Super   |

**Name origins:**
- **Chaos** - opposite of Ctrl (Control) - same on both platforms
- **Force** (macOS) - opposite of Option (choice) 
- **Sub** (Win/Linux) - opposite of Super/Win
- **Wish** (macOS) - soft command, desire
- **Main** (Win/Linux) - opposite of Alt (alternate)

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
