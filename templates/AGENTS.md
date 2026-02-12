# AGENTS.md

## Project
- Name: <PROJECT_NAME>
- Primary branch: <PRIMARY_BRANCH>
- Default branch prefix: <DEFAULT_BRANCH_PREFIX>
- Repo URL: <REPO_URL>
- Issue tracker: <ISSUE_TRACKER_URL>
- Project board: <PROJECT_BOARD_URL>

## Contract
- Follow docs/PRINCIPLES.md and docs/ARCHITECTURE.md as source-of-truth constraints.
- Link work to issues or explicit milestones.
- Keep docs/HANDOFF.md and docs/NEXT_AGENT_PROMPT.md current.
- Avoid secrets and sensitive data in any files.

## Working style
- Prefer small, reviewable changes.
- Document non-obvious decisions.
- Use <DEFAULT_BRANCH_PREFIX>/short-description for branches.
- Use one Git worktree per agent when working concurrently. See docs/WORKTREES.md.

## Commit messages (50/72 rule)
- Subject line <= 50 characters, imperative mood, no period.
- Blank line between subject and body.
- Body lines <= 72 characters, hard-wrapped.
- Explain why and what; reference issues if available.

## Autonomy
Default autonomy: <AUTONOMY_DEFAULT>

## Security notes
<SECURITY_NOTES>
