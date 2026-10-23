# Behavior reference

These tables describe the supplied macOS rules. Enable only the rows you want. See the [modifier guide](modifiers) for the names and [installation](installation) for importing or removing rules.

## Physical input and output

| Physical input | Name | Output with rule enabled |
|----------------|------|--------------------------|
| Hold Caps Lock with another key | ⁂ Mega | Control+Option+Command with that key |
| Hold Tab with another key | ❖ Giga | Shift+Control+Option+Command with that key |
| Right Control | ❋ Chaos | Option+Command |
| Right Option | ▲ Force | Control+Command |
| Right Command | ⭑ Wish | Control+Option |
| Tap Caps Lock alone | | Caps Lock in `megakey.json`; Escape in `megakey-esc.json` |
| Tap Tab alone | | Tab in both files |
| Fn+Caps Lock | | Caps Lock, if the keyboard exposes Fn to Karabiner |

Tap actions apply when you release the key alone within Karabiner's `basic.to_if_alone_timeout_milliseconds` (1000 ms by default). Another key, mouse button, or scroll event cancels the tap action. The right modifiers have no separate tap action; their original behavior is replaced.

## Shifted combinations

| Physical input, held with another key | Output |
|--------------------------------------|--------|
| Shift+Caps Lock | ❖ Giga: Shift+Control+Option+Command |
| Shift+Tab | ❖ Giga: Shift+Control+Option+Command |
| Shift+Right Control | Shift+Chaos: Shift+Option+Command |
| Shift+Right Option | Shift+Force: Shift+Control+Command |
| Shift+Right Command | Shift+Wish: Shift+Control+Option |

## Optional clipboard demo

This is a separate rule in both files. Importing a file does not enable it; add **Optional clipboard demo** explicitly in Karabiner's Complex Modifications to use it.

| Input | Demo disabled | Demo enabled |
|-------|---------------|--------------|
| Mega+C | Control+Option+Command+C | Command+C (Copy) |
| Mega+V | Control+Option+Command+V | Command+V (Paste) |
| Giga+V | Shift+Control+Option+Command+V | Command+Shift+V |
| Giga+C | Shift+Control+Option+Command+C | Command+Shift+C |

Command+Shift+V pastes without formatting in Google Docs and many web apps. Its action elsewhere, and the action of Command+Shift+C, depend on the app. The demo matches the full Control+Option+Command combination, whether produced by Caps Lock, Tab with Shift, or the modifiers pressed directly. It overrides existing bindings for those C/V combinations. Chaos, Force, and Wish alone do not match it. Extra modifiers other than Shift prevent the demo from matching.

### Why the rules work this way

Karabiner evaluates manipulators [from top to bottom and uses the first match](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-evaluation-priority/). The Fn+Caps Lock exception comes first. The general Caps Lock rule accepts optional modifiers, so it also handles Shift+Caps Lock: optional Shift passes through and turns Mega into Giga. A separate Shift-specific rule after it would never run. Removing that unreachable rule preserves both the effective chord behavior and the variant's tap action.

The clipboard rule requires Control, Option, and Command and allows optional Shift. Karabiner [removes mandatory modifiers and keeps optional modifiers](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/from/modifiers/) in output events. Sending Command+C/V therefore keeps Shift for Giga+C/V without a separate mapping.

The default variant gives its synthetic Caps Lock tap a `hold_down_milliseconds` value of 200, following [Karabiner's Caps Lock guidance](https://karabiner-elements.pqrs.org/docs/json/complex-modifications-manipulator-definition/to-if-alone/#about-sending-caps-lock). The Escape variant needs no Caps Lock tap delay. Fn+Caps Lock forwards the physical press and release rather than using `to_if_alone`.

## Manual checks

The regression script checks configuration structure and expected modifier matching; it does not drive Karabiner or prove an app's behavior. Test these on your keyboard before relying on the mappings:

1. Enable the base rules you want, leaving the clipboard demo disabled. In Karabiner-EventViewer, hold each mapped key with a letter and compare its modifier flags with the first two tables. Check Shift+Caps Lock with either Shift key, and check both key release orders for stuck modifiers.
2. Tap Caps Lock alone in each variant (enable only one variant at a time). Expect Caps Lock in the default and Escape in the alternate. Tap Tab for Tab; hold it with a letter for Giga. A chord should not also emit a tap.
3. If your keyboard exposes Fn, press Fn+Caps Lock to toggle Caps Lock. If it does not, keep the default variant or another Caps Lock binding.
4. With the demo disabled, confirm Mega+C/V retains Control+Option+Command in EventViewer. With it enabled, select text in a text editor, copy with Caps Lock+C, and paste with Caps Lock+V.
5. In Google Docs or another web editor that supports Command+Shift+V, copy formatted text and paste with Tab+V or Shift+Caps Lock+V. Expect paste without formatting. Check Giga+C produces Command+Shift+C in EventViewer; only test its app action where you know what that shortcut does.
6. Remove the demo and then the base rules from Complex Modifications. Confirm the original shortcuts and key behavior return.
