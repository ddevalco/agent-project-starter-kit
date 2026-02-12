#!/usr/bin/env python3
import os
import re
from pathlib import Path


def prompt(label, default=None, optional=False):
    if default:
        q = f"{label} [{default}]: "
    else:
        q = f"{label}: "
    val = input(q).strip()
    if not val and default is not None:
        return default
    if not val and optional:
        return ""
    return val


def slugify(name):
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "project"


def load_and_replace(path, variables):
    text = path.read_text(encoding="utf-8")
    for key, value in variables.items():
        text = text.replace(f"<{key}>", value)
    return text


def write_from_dir(src_dir, dest_dir, variables):
    for path in src_dir.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(src_dir)
        out_path = dest_dir / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(load_and_replace(path, variables), encoding="utf-8")


def main():
    base = Path(__file__).resolve().parent.parent
    templates_dir = base / "templates"
    prompts_dir = base / "prompts"
    out_root = base / "out"

    project_name = prompt("PROJECT_NAME")
    repo_url = prompt("REPO_URL (optional)", optional=True)
    primary_branch = prompt("PRIMARY_BRANCH", default="main")
    issue_tracker_url = prompt("ISSUE_TRACKER_URL (optional)", optional=True)
    project_board_url = prompt("PROJECT_BOARD_URL (optional)", optional=True)
    default_branch_prefix = prompt("DEFAULT_BRANCH_PREFIX", default="agent")
    security_notes = prompt("SECURITY_NOTES (optional)", optional=True)
    autonomy_default = prompt("AUTONOMY_DEFAULT", default="enabled")

    slug = slugify(project_name)
    out_dir = out_root / slug

    variables = {
        "PROJECT_NAME": project_name,
        "PROJECT_SLUG": slug,
        "REPO_URL": repo_url,
        "PRIMARY_BRANCH": primary_branch,
        "ISSUE_TRACKER_URL": issue_tracker_url,
        "PROJECT_BOARD_URL": project_board_url,
        "DEFAULT_BRANCH_PREFIX": default_branch_prefix,
        "SECURITY_NOTES": security_notes,
        "AUTONOMY_DEFAULT": autonomy_default,
    }

    if out_dir.exists() and any(out_dir.iterdir()):
        raise SystemExit(f"Output directory not empty: {out_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)

    write_from_dir(templates_dir, out_dir, variables)
    write_from_dir(prompts_dir, out_dir / "prompts", variables)

    print("\nNext steps:")
    print(f"1) cd {out_dir}")
    print("2) git init")
    print("3) gh repo create <OWNER>/<REPO> --public --source . --remote origin --push  (optional)")
    print("4) Paste prompts/NEW_PROJECT_INIT_PROMPT.txt into a fresh Codex thread")


if __name__ == "__main__":
    main()
