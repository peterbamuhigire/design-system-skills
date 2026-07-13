"""Check that representative prompts retrieve the expected skill in the top three."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


STOP = {"a", "an", "and", "any", "for", "in", "of", "on", "or", "the", "to", "use", "when", "with"}


def tokens(value: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9]+", value.lower()) if len(word) > 2 and word not in STOP}


def descriptions(root: Path) -> dict[str, str]:
    found: dict[str, str] = {}
    for path in root.glob("skills/**/SKILL.md"):
        if "_TEMPLATE" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        if not match:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        if data.get("name") and data.get("description"):
            found[str(data["name"])] = str(data["description"])
    return found


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    fixtures = yaml.safe_load((root / "tests" / "routing-fixtures.yml").read_text(encoding="utf-8"))
    catalog = descriptions(root)
    failures = []
    top1 = 0
    for item in fixtures:
        query = tokens(item["prompt"])
        ranked = sorted(
            catalog,
            key=lambda name: (len(query & tokens(name + " " + catalog[name])), name == item["expected"]),
            reverse=True,
        )
        top = ranked[:3]
        if top and top[0] == item["expected"]:
            top1 += 1
        if item["expected"] not in top:
            failures.append((item["prompt"], item["expected"], top))
    print(f"routing fixtures={len(fixtures)} precision@1={top1/len(fixtures):.0%} precision@3={(len(fixtures)-len(failures))/len(fixtures):.0%}")
    for prompt, expected, actual in failures:
        print(f"FAIL expected={expected} actual={actual} prompt={prompt}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
