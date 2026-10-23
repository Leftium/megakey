# Behavior reference

These tables describe the supplied macOS rules. Enable only the rows you want. See the [modifier guide](modifiers) for the names and [installation](installation) for importing or removing rules.

## Mega is the center

The macOS combinations differ from Mega by one modifier:

```text
                      Giga (Shift+Ctrl+Opt+Cmd)
                                ^ +Shift
                                |
 Wish (Ctrl+Opt) <------ Mega (Ctrl+Opt+Cmd) ------> Chaos (Opt+Cmd)
       -Cmd                     |                    -Ctrl
                                v
                         Force (Ctrl+Cmd)
                               -Opt
```

The [modifier guide](modifiers#names-on-windows-and-linux) shows the corresponding Windows/Linux naming proposal. The supplied software remains macOS-only.

## Physical input and output

| Physical input | Name | Output with rule enabled |
|----------------|------|--------------------------|
| Hold <kbd>Caps Lock</kbd> with another key | ⁂ Mega | <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> with that key |
| Hold <kbd>Tab</kbd> with another key | ❖ Giga | <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> with that key |
| <kbd>Right Ctrl</kbd> | ❋ Chaos | <kbd>Opt</kbd>+<kbd>Cmd</kbd> |
| <kbd>Right Option</kbd> | ▲ Force | <kbd>Ctrl</kbd>+<kbd>Cmd</kbd> |
| <kbd>Right Cmd</kbd> | ⭑ Wish | <kbd>Ctrl</kbd>+<kbd>Opt</kbd> |
| Tap <kbd>Caps Lock</kbd> alone | | <kbd>Caps Lock</kbd> in `megakey.json`; <kbd>Esc</kbd> in `megakey-esc.json` |
| Tap <kbd>Tab</kbd> alone | | <kbd>Tab</kbd> in both files |
| <kbd>Fn</kbd>+<kbd>Caps Lock</kbd> | | <kbd>Caps Lock</kbd>, if the keyboard exposes Fn to Karabiner |

- Tap actions apply when you release the key alone within Karabiner's `basic.to_if_alone_timeout_milliseconds` (1000 ms by default).
- Another key, mouse button, or scroll event cancels the tap action.
- The right modifiers have no separate tap action; their original behavior is replaced.

## Shifted combinations

| Physical input, held with another key | Output |
|--------------------------------------|--------|
| <kbd>Shift</kbd>+<kbd>Caps Lock</kbd> | ❖ Giga: <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> |
| <kbd>Shift</kbd>+<kbd>Tab</kbd> | ❖ Giga: <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> |
| <kbd>Shift</kbd>+<kbd>Right Ctrl</kbd> | Shift+Chaos: <kbd>Shift</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> |
| <kbd>Shift</kbd>+<kbd>Right Option</kbd> | Shift+Force: <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Cmd</kbd> |
| <kbd>Shift</kbd>+<kbd>Right Cmd</kbd> | Shift+Wish: <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd> |

## Optional clipboard demo

This is a separate rule in both files. Importing a file does not enable it; add **Optional clipboard demo** explicitly in Karabiner's Complex Modifications to use it.

| Input | Demo disabled | Demo enabled |
|-------|---------------|--------------|
| Mega+C | <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd>+<kbd>C</kbd> | <kbd>Cmd</kbd>+<kbd>C</kbd> (Copy) |
| Mega+V | <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd>+<kbd>V</kbd> | <kbd>Cmd</kbd>+<kbd>V</kbd> (Paste) |
| Giga+V | <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd>+<kbd>V</kbd> | <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> |
| Giga+C | <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd>+<kbd>C</kbd> | <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> |

<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> pastes without formatting in Google Docs and many web apps. Its action elsewhere, and the action of <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd>, depend on the app. The demo matches the full <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> combination, whether produced by <kbd>Caps Lock</kbd>, <kbd>Tab</kbd>, or the modifiers pressed directly. It overrides existing bindings for those C/V combinations. Chaos, Force, and Wish alone do not match it. Extra modifiers other than Shift prevent the demo from matching.

### Why the rules work this way

Karabiner evaluates manipulators [from top to bottom and uses the first match](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-evaluation-priority/). The <kbd>Fn</kbd>+<kbd>Caps Lock</kbd> exception comes first. The general <kbd>Caps Lock</kbd> rule accepts optional modifiers, so it also handles <kbd>Shift</kbd>+<kbd>Caps Lock</kbd>: optional Shift passes through and turns Mega into Giga. A separate Shift-specific rule after it would never run. Removing that unreachable rule preserves both the effective chord behavior and the variant's tap action.

The clipboard rule requires Control, Option, and Command and allows optional Shift. Karabiner [removes mandatory modifiers and keeps optional modifiers](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/modifiers/) in output events. Sending Command+C/V therefore keeps Shift for Giga+C/V without a separate mapping.

The default variant gives its synthetic <kbd>Caps Lock</kbd> tap a `hold_down_milliseconds` value of 200, following [Karabiner's Caps Lock guidance](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-alone/#about-sending-caps-lock). The Escape variant needs no <kbd>Caps Lock</kbd> tap delay. <kbd>Fn</kbd>+<kbd>Caps Lock</kbd> forwards the physical press and release rather than using `to_if_alone`.

## Manual checks

The regression script checks configuration structure and expected modifier matching; it does not drive Karabiner or prove an app's behavior. Test these on your keyboard before relying on the mappings:

1. Enable the base rules you want, leaving the clipboard demo disabled. In Karabiner-EventViewer, hold each mapped key with a letter and compare its modifier flags with the first two tables. Check <kbd>Shift</kbd>+<kbd>Caps Lock</kbd> with either Shift key, and check both key release orders for stuck modifiers.
2. Tap <kbd>Caps Lock</kbd> alone in each variant (enable only one variant at a time). Expect <kbd>Caps Lock</kbd> in the default and Escape in the alternate. Tap <kbd>Tab</kbd> for <kbd>Tab</kbd>; hold it with a letter for Giga. A chord should not also emit a tap.
3. If your keyboard exposes Fn, press <kbd>Fn</kbd>+<kbd>Caps Lock</kbd> to toggle <kbd>Caps Lock</kbd>. If it does not, keep the default variant or another <kbd>Caps Lock</kbd> binding.
4. With the demo disabled, confirm Mega+C/V retains <kbd>Ctrl</kbd>+<kbd>Opt</kbd>+<kbd>Cmd</kbd> in EventViewer. With it enabled, select text in a text editor, copy with <kbd>Caps Lock</kbd>+<kbd>C</kbd>, and paste with <kbd>Caps Lock</kbd>+<kbd>V</kbd>.
5. In Google Docs or another web editor that supports <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>, copy formatted text and paste with <kbd>Tab</kbd>+<kbd>V</kbd> or <kbd>Shift</kbd>+<kbd>Caps Lock</kbd>+<kbd>V</kbd>. Expect paste without formatting. Check Giga+C produces <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> in EventViewer; only test its app action where you know what that shortcut does.
6. Remove the demo and then the base rules from Complex Modifications. Confirm the original shortcuts and key behavior return.
