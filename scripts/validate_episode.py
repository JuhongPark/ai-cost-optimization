#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_file(schema: dict, path: Path) -> tuple[bool, str]:
    try:
        payload = load_json(path)
        jsonschema.validate(payload, schema)
    except jsonschema.ValidationError as exc:
        location = ".".join(str(part) for part in exc.absolute_path) or "<root>"
        return False, f"{path}: invalid at {location}: {exc.message}"
    except Exception as exc:  # pragma: no cover - defensive reporting
        return False, f"{path}: failed to load: {exc}"
    return True, f"{path}: valid"


def collect_targets(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(candidate for candidate in path.rglob("*.json") if candidate.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate episode JSON files against the episode schema.")
    parser.add_argument("target", help="Path to a JSON file or directory of JSON files.")
    parser.add_argument(
        "--schema",
        default="schemas/episode.schema.json",
        help="Path to the JSON schema file.",
    )
    args = parser.parse_args()

    schema_path = Path(args.schema)
    target_path = Path(args.target)
    schema = load_json(schema_path)

    targets = collect_targets(target_path)
    if not targets:
        print(f"No JSON files found under {target_path}")
        return 1

    all_valid = True
    for file_path in targets:
        valid, message = validate_file(schema, file_path)
        print(message)
        all_valid = all_valid and valid
    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
