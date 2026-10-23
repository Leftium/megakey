# Installation

MegaKey's supplied configurations require macOS and [Karabiner-Elements](https://karabiner-elements.pqrs.org/). Install Karabiner and grant the permissions requested during setup before importing rules. Start with Caps Lock; Tab and the right modifier keys are optional.

## Choose a variant

Import one file, then enable individual rules from it:

| File | Caps Lock held with another key | Caps Lock tapped alone |
|------|--------------------------------|------------------------|
| `megakey.json` (default) | Mega: Control+Option+Command | Caps Lock |
| `megakey-esc.json` | Mega: Control+Option+Command | Escape |

Everything else is identical. Do not enable the Caps Lock rules from both files at once: Karabiner uses the first matching rule. When switching variants, remove the old Caps Lock rule before enabling the new one.

## Import from your browser

[Import the default](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json), which keeps Caps Lock on tap:

```text
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json
```

Or [import the Escape variant](karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json):

```text
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json
```

Accept the browser's request to open Karabiner, then confirm the import. Importing makes the rules available; each rule stays off until you enable it. The links fetch files from `main`. To try an unmerged PR, download its files and install them manually.

## Manual installation

If the import link does not open, download [megakey.json](https://raw.githubusercontent.com/Leftium/megakey/main/megakey.json) or [megakey-esc.json](https://raw.githubusercontent.com/Leftium/megakey/main/megakey-esc.json). Save the JSON file, not the GitHub HTML page.

1. Create `~/.config/karabiner/assets/complex_modifications/` if it does not exist.
2. Copy your chosen file into that directory.
3. Open Karabiner-Elements, then **Complex Modifications** and **Add rule** (or **Add predefined rule**, depending on your version).
4. Enable the **Caps Lock** rule. For a quick Copy/Paste test, enable **Optional clipboard demo** separately. Add Tab, Right Ctrl, Right Option, or Right Cmd only if you want those mappings.

Follow the [Quick Start test](./#quick-start) to copy and paste in a text editor, or use [EventViewer](etc#manual-checks) without the clipboard demo. With the demo enabled, Mega+C/V sends Command+C/V, Giga+V sends Command+Shift+V, and shifted Mega+C sends Command+Shift+C. The shifted actions depend on the app. The demo also overrides existing full Control+Option+Command+C/V bindings.

## What changes, and how to undo it

Caps Lock and Tab act as modifiers while held with another key. A tap alone sends Caps Lock (or Escape) and Tab respectively, provided you release within the tap timeout. The right modifier mappings replace those keys' original behavior; they have no separate tap action.

Fn+Caps Lock sends Caps Lock in either variant, provided your keyboard reports Fn to Karabiner. If it does not, use the default variant to keep a Caps Lock tap available.

To disable a rule, remove its enabled entry from **Complex Modifications** using the remove/trash control. This restores the key's original behavior. Remove the optional clipboard demo independently to restore full Mega+C/V shortcuts. Deleting an imported JSON file alone does not remove enabled rules, which Karabiner copies into your profile. You can delete the downloaded asset after removing its enabled entries if you no longer want it in the rule picker.
