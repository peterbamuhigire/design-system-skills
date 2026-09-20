"""Validate the independent offline design catalog contract."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.design_engine.catalog import Catalog


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args()
    try:
        catalog = Catalog.from_file(args.catalog)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1
    print("design-catalog-validator:")
    print(f"- source: {catalog.source}")
    print(f"- revision: {catalog.revision}")
    print(f"- records: {len(catalog.records)}")
    print(f"- stack guidance: {len(catalog.stack_guidance)}")
    print("PASS: schema, domain coverage, stack coverage, evidence and lifecycle checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
