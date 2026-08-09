#!/usr/bin/env python3
"""Install this Skill and non-destructively bootstrap durable project memory."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


BEGIN = "<!-- project-knowledge-base:start -->"
END = "<!-- project-knowledge-base:end -->"
RUNTIME_ENTRIES = ("SKILL.md", "agents", "assets", "references", "scripts")


def project_relative(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or not candidate.parts or ".." in candidate.parts:
        raise argparse.ArgumentTypeError("knowledge directory must be a non-empty project-relative path")
    return candidate


def write_if_missing(source: Path, destination: Path, replacements: dict[str, str] | None = None) -> bool:
    if destination.exists():
        return False
    text = source.read_text(encoding="utf-8")
    for old, new in (replacements or {}).items():
        text = text.replace(old, new)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8", newline="\n")
    return True


def copy_runtime(skill_root: Path, destination: Path) -> None:
    if skill_root == destination:
        return
    destination.mkdir(parents=True, exist_ok=True)
    for name in RUNTIME_ENTRIES:
        source = skill_root / name
        target = destination / name
        if source.is_dir():
            shutil.copytree(
                source,
                target,
                dirs_exist_ok=True,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
        else:
            shutil.copy2(source, target)


def update_agents(project_root: Path, snippet: str) -> Path:
    agents_path = project_root / "AGENTS.md"
    existing = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
    if pattern.search(existing):
        updated = pattern.sub(lambda _: snippet, existing)
    elif existing.strip():
        updated = existing.rstrip() + "\n\n" + snippet + "\n"
    else:
        updated = snippet + "\n"
    agents_path.write_text(updated, encoding="utf-8", newline="\n")
    return agents_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--knowledge-dir", default=Path("knowledge-base"), type=project_relative)
    args = parser.parse_args()

    project_root = args.project_root.expanduser().resolve()
    if not project_root.is_dir():
        parser.error(f"project root does not exist: {project_root}")

    skill_root = Path(__file__).resolve().parent.parent
    runtime_destination = project_root / ".agents" / "skills" / "project-knowledge-base"
    if runtime_destination != skill_root and skill_root in runtime_destination.parents:
        parser.error(
            "refusing to install the Skill into one of its own child directories; "
            "place the downloaded SOP inside a parent project and pass that project root"
        )
    copy_runtime(skill_root, runtime_destination)

    knowledge_dir = args.knowledge_dir
    knowledge_root = project_root / knowledge_dir
    assets = skill_root / "assets"
    created: list[str] = []

    memory_replacements = {"knowledge-base/": knowledge_dir.as_posix().rstrip("/") + "/"}
    if write_if_missing(
        assets / "PROJECT_MEMORY.md",
        project_root / "PROJECT_MEMORY.md",
        memory_replacements,
    ):
        created.append("PROJECT_MEMORY.md")

    template_root = assets / "knowledge-base"
    for source in sorted(template_root.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(template_root)
        destination = knowledge_root / relative
        if write_if_missing(source, destination):
            created.append((knowledge_dir / relative).as_posix())

    snippet = (assets / "AGENTS.snippet.md").read_text(encoding="utf-8")
    snippet = snippet.replace("{{KNOWLEDGE_DIR}}", knowledge_dir.as_posix().rstrip("/"))
    agents_path = update_agents(project_root, snippet.strip())

    result = {
        "status": "initialized" if created else "already_initialized",
        "projectRoot": str(project_root),
        "skillPath": str(runtime_destination),
        "knowledgePath": str(knowledge_root),
        "agentsPath": str(agents_path),
        "createdFiles": created,
        "nextAction": "Inspect the project, replace scaffold placeholders with verified content, then run the audit script.",
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
