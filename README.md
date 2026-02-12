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
- Use one Git worktree per agent to avoid collisions.
- Update HANDOFF and NEXT_AGENT_PROMPT as work progresses.
- Enforce 50/72 commit message rule (subject <= 50 chars, body <= 72 chars).
- Never put secrets in repo or prompts.
- Keep principles/architecture separate from roadmap and handoff status.

## Parallel agents with Git worktrees
Git worktrees let you attach multiple working directories to the same repo, each
on its own branch. This avoids stashing/switching and keeps concurrent agents
from colliding.

Example:
```bash
# From repo root

git worktree add ../<PROJECT_SLUG>-agent-1 -b <DEFAULT_BRANCH_PREFIX>/agent-1

git worktree add ../<PROJECT_SLUG>-agent-2 -b <DEFAULT_BRANCH_PREFIX>/agent-2
```

Now you have:
- <PROJECT_SLUG> (main)
- <PROJECT_SLUG>-agent-1 (agent-1 branch)
- <PROJECT_SLUG>-agent-2 (agent-2 branch)

Each agent works in its own worktree and opens its own PR.

## Common mistakes
- Stale HANDOFF or NEXT_AGENT_PROMPT after significant changes.
- Mixing principles with roadmap or sprint tasks.
- Committing secrets or credentials.
- Skipping issue linkage for work items.
- Multiple agents working in the same worktree.
