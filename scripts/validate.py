#!/usr/bin/env python3
"""Check distributed rules against MegaKey's documented modifier contract.

This models first-match and modifier propagation only, not Karabiner's event
queue, tap timing, or physical keyboard behavior. Run Karabiner's linter too.
"""

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODIFIERS = {"command", "control", "option", "shift", "fn", "caps_lock"}


def canonical(modifier):
    return modifier.removeprefix("left_").removeprefix("right_")


def match(manipulator, key, modifiers):
    source = manipulator["from"]
    required = set(source.get("modifiers", {}).get("mandatory", []))
    optional = set(source.get("modifiers", {}).get("optional", []))
    return (source["key_code"] == key and required <= modifiers
            and ("any" in optional or modifiers <= required | optional))


def emit(manipulator, modifiers):
    """Mandatory modifiers are consumed; optional ones pass through."""
    required = set(manipulator["from"].get("modifiers", {}).get("mandatory", []))
    event = manipulator["to"][0]
    output = modifiers - required | {canonical(m) for m in event.get("modifiers", [])}
    key = canonical(event["key_code"])
    if key in MODIFIERS - {"caps_lock"}:
        output.add(key)
        key = None
    return key, output


def first(rules, key, modifiers):
    return next((m for rule in rules for m in rule["manipulators"]
                 if match(m, key, modifiers)), None)


def check(config, tap):
    rules = config["rules"]
    assert config["title"] and len(rules) == 6
    for rule in rules:
        assert rule["description"] and rule["manipulators"]
        for m in rule["manipulators"]:
            assert m["type"] == "basic" and len(m["to"]) == 1
            assert m["from"]["key_code"] and m["to"][0]["key_code"]
    base, demo = rules[:5], rules[5:]
    expected = {
        "caps_lock": {"control", "option", "command"},
        "tab": {"shift", "control", "option", "command"},
        "right_control": {"option", "command"},
        "right_option": {"control", "command"},
        "right_command": {"control", "option"},
    }
    for key, output in expected.items():
        for extra in (set(), {"shift"}):
            m = first(base, key, extra)
            assert emit(m, extra) == (None, output | extra), (key, extra)
            # Letter shortcuts retain all modifiers while the demo is disabled.
            for letter in ("c", "v"):
                assert first(base, letter, output | extra) is None
    caps = first(base, "caps_lock", set())
    assert len(rules[0]["manipulators"]) == 2  # Fn exception, then general rule.
    assert caps["to_if_alone"] == [tap]
    assert first(base, "tab", set())["to_if_alone"] == [{"key_code": "tab"}]
    for key in ("right_control", "right_option", "right_command"):
        assert "to_if_alone" not in first(base, key, set())
    for extra in ({"fn"}, {"fn", "shift"}):
        fn = first(base, "caps_lock", extra)
        assert fn is rules[0]["manipulators"][0]
        assert emit(fn, extra) == ("caps_lock", extra - {"fn"})
        assert "to_if_alone" not in fn
    assert len(demo[0]["manipulators"]) == 2
    for letter in ("c", "v"):
        for extra in (set(), {"shift"}):
            held = expected["caps_lock"] | extra
            m = first(rules, letter, held)
            assert emit(m, held) == (letter, {"command"} | extra)
        for name in ("right_control", "right_option", "right_command"):
            for extra in (set(), {"shift"}):
                assert first(rules, letter, expected[name] | extra) is None
        assert first(rules, letter, set()) is None
        assert first(rules, letter, {"command"}) is None
        assert first(rules, letter, expected["caps_lock"] | {"fn"}) is None
    assert first(rules, "x", expected["caps_lock"]) is None


def main():
    variants = []
    for filename, tap in (
        ("megakey.json", {"key_code": "caps_lock", "hold_down_milliseconds": 200}),
        ("megakey-esc.json", {"key_code": "escape"}),
    ):
        config = json.loads((ROOT / filename).read_text())
        check(config, tap)
        normalized = copy.deepcopy(config)
        normalized.pop("title")
        normalized["rules"][0].pop("description")
        normalized["rules"][0]["manipulators"][1].pop("to_if_alone")
        variants.append(normalized)
        print(f"PASS {filename}: five combinations, Shift, Fn priority, taps, clipboard on/off")
    assert variants[0] == variants[1], "Variants differ beyond Caps Lock tap and labels"
    print("PASS variant parity (only Caps Lock tap and labels differ)")


if __name__ == "__main__":
    main()
