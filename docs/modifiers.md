# Modifier Details
![](https://leftium.github.io/megakey/assets/keyboard.png)

## The two main keys

### It starts with the Mega key

- Mega is a pseudo-key; there is no physical "Mega" key
- "Mega" represents pressing all three modifier keys at the same time (<kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd>)
- This combination is relatively easy. Both to recall and press.
- The name "Mega" was chosen because some related conventions call this combination "Meh" ("Meh"-ga)
- ⁂ is the symbol for Mega. It represents the three keys that are pressed. 
- Software can be used to repurpose the <kbd>CapsLock</kbd> key into a physical <kbd>Mega</kbd> key.

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
*The 4 variations of Mega differ by a single modifier key*

### Giga is the bigger variant

- Giga is another pseudo-key: Shift+Mega (<kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd>)
- Giga is the shifted version of Mega. (Think SI prefixes)
- ❖ is the symbol for Mega. It represents the four keys that are pressed. 
- Software can be used to repurpose the <kbd>Tab</kbd> key into a physical <kbd>Giga</kbd>
- Giga can also be accessed via <kbd>Shift</kbd><kbd>CapsLock</kbd> if CapsLock has been configured as the Mega key.

## The three additional "anti" keys

- There are three "anti" keys.
- The anti keys are variations of Mega with one key removed.
- Unlike Mega/Giga, the anti keys have shifted versions (that don't have special names on their own)
  - For example both `Wish` and `Shift-Wish` are unique. While `Shift-Mega` is just `Giga` and `Shift-Giga` doesn't make sense.

### Wish

- Wish is the "Anti-cmd" pseudo-key: Mega minus Cmd (<kbd>Ctrl</kbd><kbd>Opt</kbd>)
- ⭑ is the symbol for Wish.
- Software can be used to repurpose <kbd>Right Cmd</kbd> for <kbd>Wish</kbd>
- Mnemonics
  - "Your wish is my command"
  - "Wish" is a less agressive form of "command"
  - "Wish upon a star" (for the ⭑ symbol)

### Force

- Force is the "Anti-opt" pseudo-key: Mega minus Opt (<kbd>Ctrl</kbd><kbd>Cmd</kbd>)
- ▲ is the symbol for Force.
- Software can be used to repurpose <kbd>Right Option</kbd> for <kbd>Force</kbd>
- Mnemonics
  - To "force" is to leave no "option."
  - Triforce (▲ resembles artifact from [Zelda](https://en.wikipedia.org/wiki/Triforce))

### Chaos

- Chaos is the "Anti-ctrl" pseudo-key: Mega minus Ctrl (<kbd>Opt</kbd><kbd>Cmd</kbd>)
- ❋ is the symbol for Chaos.
- Software can be used to repurpose <kbd>Right Ctrl</kbd> for <kbd>Chaos</kbd>
- Mnemonics
  - "Chaos" implies "uncontrolled."
  - ❋ symbol is similar to the [Chaos Star](https://en.wikipedia.org/wiki/Symbol_of_Chaos)

## The following table summarizes all the keys:

|        | Name  | Single Key              | Multiple Keys                                               | ⇧ | ⌃ | ⌥ | ⌘ | Notes             |
|-------:|-------|-------------------------|-------------------------------------------------------------|---|---|---|---|-------------------|
| **⁂** | Mega  | <kbd>CapsLock</kbd>     | <kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd>                 |   | ⌃ | ⌥ | ⌘ | Base combination  |
| **❖** | Giga  | <kbd>Tab</kbd>          | <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>Opt</kbd><kbd>Cmd</kbd> | ⇧ | ⌃ | ⌥ | ⌘ | Mega with Shift   |
| **❋** | Chaos | <kbd>Right Ctrl</kbd>   | <kbd>Opt</kbd><kbd>Cmd</kbd>                                |   |   | ⌥ | ⌘ | Mega without Ctrl |
| **▲** | Force | <kbd>Right Option</kbd> | <kbd>Ctrl</kbd><kbd>Cmd</kbd>                               |   | ⌃ |   | ⌘ | Mega without Opt  |
| **⭑** | Wish  | <kbd>Right Cmd</kbd>    | <kbd>Ctrl</kbd><kbd>Opt</kbd>                               |   | ⌃ | ⌥ |   | Mega without Cmd  |


## Windows/Linux versions

- While Mega/Giga/Chaos work across platforms, some keys are slightly MacOS-centric.
- For the remaining two keys, words that play with the Linux key names may be used
  - "Main" vs "Alt" ("Alternate")
  - "Sub" vs "Super" ([Win] key on some Linux distros)
- Used either prepended (`Main.Wish-C`) or by itself (`Main-C`)
- The symbols remain unchanged.

```
             Shift added
             ❖ Giga
                 ↑
⭑ Main ←──── ⁂ Mega ────→ ❋ Chaos 
Alt removed      │        Ctrl removed
                 ↓
             ▲ Sub
             Win removed                
```

|        | Name  | Single Key              | Multiple Keys                                               | Notes             |
|-------:|-------|-------------------------|-------------------------------------------------------------|-------------------|
| **⁂** | Mega  | <kbd>CapsLock</kbd>     | <kbd>Ctrl</kbd><kbd>Win</kbd><kbd>Alt</kbd>                 | Base combination  |
| **❖** | Giga  | <kbd>Tab</kbd>          | <kbd>Shift</kbd><kbd>Ctrl</kbd><kbd>Win</kbd><kbd>Alt</kbd> | Mega with Shift   |
| **❋** | Chaos | <kbd>Right Ctrl</kbd>   | <kbd>Win</kbd><kbd>Alt</kbd>                                | Mega without Ctrl |
| **▲** | Sub.Force   | <kbd>Right Alt</kbd>    | <kbd>Ctrl</kbd><kbd>Alt</kbd>                               | Mega without Win  |
| **⭑** | Main.Wish  | <kbd>Right Win</kbd>    | <kbd>Ctrl</kbd><kbd>Win</kbd>                               | Mega without Alt  |

## Prior Art

TODO

---


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
