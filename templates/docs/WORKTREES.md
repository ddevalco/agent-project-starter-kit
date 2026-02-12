# Git Worktrees

## Why worktrees
Worktrees allow multiple working directories attached to one repo, each on its
own branch. This enables parallel agent work without file collisions or constant
branch switching.

## Standard workflow
- One worktree per agent
- One branch per agent (prefix with <DEFAULT_BRANCH_PREFIX>/)
- Each agent opens its own PR

## Example
```bash
# From repo root

git worktree add ../<PROJECT_SLUG>-agent-1 -b <DEFAULT_BRANCH_PREFIX>/agent-1

git worktree add ../<PROJECT_SLUG>-agent-2 -b <DEFAULT_BRANCH_PREFIX>/agent-2
```

## Cleanup
```bash
# Remove a worktree when done

git worktree remove ../<PROJECT_SLUG>-agent-1
```
