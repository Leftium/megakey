# Modifier guide

MegaKey names five combinations of ordinary modifiers. You can press the modifiers yourself or use the supplied macOS rules to put each combination on one key.

![MegaKey keyboard layout](assets/keyboard.png)

## Mega and Giga

Mega is Control+Option+Command. Its symbol, ⁂, represents the three modifiers. The name plays on "Meh," a name used for modifier combinations in other keyboard setups.

Giga is Mega with Shift: Shift+Control+Option+Command. Its symbol is ❖, representing four modifiers. The names follow the order of the SI prefixes, Mega then Giga.

With the Karabiner rules enabled, hold Caps Lock for Mega or Tab for Giga. Shift+Caps Lock also gives Giga. Tab still sends Tab when tapped alone; Caps Lock sends Caps Lock or Escape, depending on the file you chose.

```text
                    Giga: add Shift
                           |
Wish: remove Command <- Mega -> Chaos: remove Control
                           |
                    Force: remove Option
```

## Chaos, Force, and Wish

Each of these removes one modifier from Mega. The names give you a way to remember which one:

| Symbol | Name | Sends | Name and mnemonic |
|:------:|------|-------|-------------------|
| ❋ | Chaos | Option+Command | Remove Control: chaos is uncontrolled. The symbol resembles a [Chaos Star](https://en.wikipedia.org/wiki/Symbol_of_Chaos). |
| ▲ | Force | Control+Command | Remove Option: force leaves no option. The triangle recalls the [Triforce](https://en.wikipedia.org/wiki/Triforce). |
| ⭑ | Wish | Control+Option | Remove Command: "Your wish is my command." Wish upon a star. |

The supplied rules map Right Control to Chaos, Right Option to Force, and Right Command to Wish. Enable each separately; an enabled rule replaces that key's original function.

Shift can be added to all three. Shift+Mega is already Giga, and adding Shift to Giga leaves the same four-modifier combination. The [behavior reference](etc) lists the exact inputs and outputs.

## Relation to Hyper and Meh

Hyper and Meh are established names for multi-modifier mappings, but usage varies between setups. Hyper often means all four modifiers, the combination MegaKey calls Giga. MegaKey uses explicit definitions for five related combinations; it does not require you to replace a working Hyper setup or use a new remapping engine.

For shortcuts, write `Giga+C` or `❖C` instead of `Shift+Control+Option+Command+C`. These names do not assign actions by themselves. You still need to bind shortcuts in an app or enable a rule such as the optional clipboard demo.

## Names on Windows and Linux

The naming concept can be carried to Windows or Linux using Control, Win/Super, and Alt. This repository supplies no remapping software for those platforms. The following is a naming proposal, not an installable configuration.

The alternate names follow the omitted key: "Sub" is the opposite of Super, and "Main" is the opposite of Alt (alternate). They can be written as `Sub.Force` and `Main.Wish`, or shortened to `Sub` and `Main`. The symbols stay the same.

| Symbol | macOS name and combination | Windows/Linux name and combination | Omitted key |
|:------:|----------------------------|------------------------------------|-------------|
| ⁂ | Mega: Control+Option+Command | Mega: Control+Win/Super+Alt | None |
| ❖ | Giga: Shift+Control+Option+Command | Giga: Shift+Control+Win/Super+Alt | None; add Shift |
| ❋ | Chaos: Option+Command | Chaos: Win/Super+Alt | Control |
| ▲ | Force: Control+Command | Sub.Force: Control+Alt | Option / Win/Super |
| ⭑ | Wish: Control+Option | Main.Wish: Control+Win/Super | Command / Alt |

## Related work

The [Space-cadet keyboard](https://en.wikipedia.org/wiki/Space-cadet_keyboard) had a physical Hyper key. Modern remapping tools bring similar combinations to ordinary keyboards. Examples and discussions include:

- [Raycast's Hyper key](https://manual.raycast.com/hyper-key)
- [Ben Davis's Karabiner setup](https://www.davis7.sh/karabiner)
- [Meh and Hyper for normal keyboards](https://kevinkipp.com/blog/meh-and-hyper-for-normal-keyboards/)
- [How to get your very own Hyper key](https://zenmushie.medium.com/how-to-get-your-very-own-hyper-key-0c91ed4a84ff)
- [Remapping Caps Lock to Hyper](https://juleslibert.com/en/thoughts/remapping-capslock-to-hyperkey)
