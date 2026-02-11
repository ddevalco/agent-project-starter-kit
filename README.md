# Agent Project Starter Kit

## What this is
A minimal, opinionated starter kit for consistent agent bootstrapping, handoffs, and autonomous execution across projects.

## Why it works
It separates stable project identity from ongoing work:
- Identity and contract: AGENTS.md defines how agents should collaborate with humans.
- Principles: docs/PRINCIPLES.md explains non-negotiables and decision boundaries.
- Architecture: docs/ARCHITECTURE.md captures system shape and key constraints.
- Roadmap: docs/ROADMAP.md provides near- and mid-term goals.
- Handoff snapshot: docs/HANDOFF.md captures current state, risks, and next actions.
- Next-agent prompt: docs/NEXT_AGENT_PROMPT.md provides a ready-to-paste baton pass.

This structure keeps agents aligned while allowing daily work to move independently.

## How to use (coworker quickstart)
1. Clone this repo.
2. Run the generator script.
3. Create/push your new project repo.
4. Paste the init prompt into a fresh Codex thread.
5. Codex reads the canonical files and operates consistently.

Quickstart:
```bash
python3 scripts/new_project.py
```

## What files matter
- templates/AGENTS.md: Contract for agent behavior, communication, and expectations.
- templates/docs/PRINCIPLES.md: Non-negotiable principles and guardrails.
- templates/docs/ARCHITECTURE.md: System overview and key technical constraints.
- templates/docs/SECURITY.md: Security posture, data handling, and red lines.
- templates/docs/ROADMAP.md: Planned milestones and delivery order.
- templates/docs/HANDOFF.md: Current snapshot for fast re-entry.
- templates/docs/NEXT_AGENT_PROMPT.md: Ready prompt for the next agent.
- prompts/NEW_PROJECT_INIT_PROMPT.txt: Instructions for a fresh Codex thread.
- prompts/AUTONOMOUS_MODE_PROMPT.txt: The autonomous operating contract.

## Operating rules
- Keep issues/board as source of truth; link work to issues.
- Use branch prefixes for agent work (see DEFAULT_BRANCH_PREFIX).
- Update HANDOFF and NEXT_AGENT_PROMPT as work progresses.
- Never put secrets in repo or prompts.
- Keep principles/architecture separate from roadmap and handoff status.

## Common mistakes
- Stale HANDOFF or NEXT_AGENT_PROMPT after significant changes.
- Mixing principles with roadmap or sprint tasks.
- Committing secrets or credentials.
- Skipping issue linkage for work items.
