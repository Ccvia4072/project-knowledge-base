#!/usr/bin/env python3
"""Audit the structure and initialization state of project knowledge."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


BEGIN = "<!-- project-knowledge-base:start -->"
END = "<!-- project-knowledge-base:end -->"
REQUIRED_FILES = (
    "README.md",
    "current-state.md",
    "deferred-work.md",
    "debugging-pitfalls.md",
    "open-questions.md",
    "workflows.md",
    "terminology.md",
    "decisions/README.md",
    "diagnostics/README.md",
    "archive/README.md",
)
PLACEHOLDER_SIGNALS = (
    "not yet initialized",
    "No verified project facts recorded yet",
    "Replace with a verified",
    "DW-001 Initialize project-specific deferred work",
    "PIT-001 Knowledge base not yet mined",
)


def project_relative(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        raise argparse.ArgumentTypeError("knowledge directory must be a non-empty project-relative path")
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--knowledge-dir", default=Path("knowledge-base"), type=project_relative)
    parser.add_argument("--structure-only", action="store_true")
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    knowledge = root / args.knowledge_dir
    errors: list[str] = []
    warnings: list[str] = []

    required = [root / "PROJECT_MEMORY.md", root / "AGENTS.md"]
    required.extend(knowledge / item for item in REQUIRED_FILES)
    for path in required:
        if not path.is_file():
            errors.append(f"missing required file: {path}")

    skill_file = root / ".agents" / "skills" / "project-knowledge-base" / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"installed Skill missing: {skill_file}")

    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        agents = agents_path.read_text(encoding="utf-8")
        if agents.count(BEGIN) != 1 or agents.count(END) != 1:
            errors.append("AGENTS.md must contain exactly one managed knowledge-base block")

    heading_requirements = {
        knowledge / "deferred-work.md": ("## Open items", "## Resolved items"),
        knowledge / "debugging-pitfalls.md": ("## Active pitfalls", "## Mitigated or obsolete pitfalls"),
        knowledge / "current-state.md": ("## Verified present state", "## Immediate next safe action"),
    }
    for path, headings in heading_requirements.items():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                errors.append(f"missing required heading {heading!r} in {path}")

    if not args.structure_only:
        content_targets = [
            root / "PROJECT_MEMORY.md",
            knowledge / "current-state.md",
            knowledge / "deferred-work.md",
            knowledge / "debugging-pitfalls.md",
        ]
        for path in content_targets:
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for signal in PLACEHOLDER_SIGNALS:
                if signal.casefold() in text.casefold():
                    warnings.append(f"initialization placeholder remains in {path}: {signal}")

    if errors:
        status = "invalid"
        exit_code = 1
    elif warnings:
        status = "needs_content"
        exit_code = 2
    else:
        status = "ready"
        exit_code = 0

    print(
        json.dumps(
            {
                "status": status,
                "projectRoot": str(root),
                "knowledgePath": str(knowledge),
                "errors": errors,
                "warnings": warnings,
            },
            ensure_ascii=False,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
