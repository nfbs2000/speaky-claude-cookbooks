#!/usr/bin/env bash
# Merge upstream/main while keeping this fork free of CI workflows.
#
# This fork runs no CI. The only Actions workflow we want is
# pages-build-deployment, which GitHub generates itself for the legacy
# Pages deploy and which has no file in .github/workflows/. Upstream ships
# nine workflow files; if any of them land here they start running against
# our notebooks, including the *_kr.ipynb translations.
#
# So: merge everything upstream has, then drop .github/workflows/ back out
# before the merge commit is written.
#
# Usage:  scripts/sync_upstream.sh [upstream-ref]     (default: upstream/main)

set -euo pipefail

REF="${1:-upstream/main}"
REMOTE="${REF%%/*}"
WORKFLOWS=".github/workflows"

cd "$(git rev-parse --show-toplevel)"

# Refuse to run on a dirty tree: a conflicted merge is hard enough to reason
# about without unrelated edits mixed in.
if [[ -n "$(git status --porcelain)" ]]; then
    echo "error: working tree is not clean. Commit or stash first." >&2
    exit 1
fi

echo "==> Fetching $REMOTE"
git fetch "$REMOTE"

BEFORE="$(git rev-parse HEAD)"

echo "==> Merging $REF"
# A modify/delete conflict on .github/workflows/ is expected and fine: we
# deleted those files, upstream keeps changing them. Let the merge stop, we
# resolve by deleting, then commit.
if git merge --no-commit --no-ff "$REF"; then
    MERGE_CLEAN=1
else
    MERGE_CLEAN=0
    echo "==> Merge paused (conflicts). Checking whether they are all in $WORKFLOWS"
    OTHER="$(git diff --name-only --diff-filter=U | grep -v "^$WORKFLOWS/" || true)"
    if [[ -n "$OTHER" ]]; then
        echo "error: conflicts outside $WORKFLOWS — resolve these by hand:" >&2
        echo "$OTHER" >&2
        echo "Then run: git rm -rf --ignore-unmatch $WORKFLOWS && git commit" >&2
        exit 1
    fi
fi

echo "==> Dropping $WORKFLOWS"
git rm -rf --ignore-unmatch --quiet "$WORKFLOWS" 2>/dev/null || true

if git diff --cached --quiet && [[ "$MERGE_CLEAN" == "1" ]] && [[ "$BEFORE" == "$(git rev-parse HEAD)" ]]; then
    echo "==> Already up to date, nothing to commit"
    git merge --abort 2>/dev/null || true
    exit 0
fi

git commit --no-edit --quiet
echo "==> Merged $REF (workflows excluded)"

# The whole point of this script is that no CI file sneaks in. Say so out loud.
if [[ -d "$WORKFLOWS" ]] && [[ -n "$(ls -A "$WORKFLOWS" 2>/dev/null)" ]]; then
    echo "error: $WORKFLOWS still has files after the merge:" >&2
    ls -1 "$WORKFLOWS" >&2
    exit 1
fi
echo "==> Verified: $WORKFLOWS is empty"

echo
echo "Next: confirm GitHub agrees that only the Pages workflow is live —"
echo "  gh workflow list --all | grep -v pages-build-deployment"
echo "Anything printed there is a workflow that can still run; disable it with"
echo "  gh workflow disable \"<name>\""
