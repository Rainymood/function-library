# How to revert to previous commit

`git log` to view the history

```bash
commit 34669d7f7a067a58fdc2f6633c32876263de4be8 (HEAD -> feature/redis, origin/feature/redis)
Author: ...
Date:   Fri Dec 4 14:11:53 2020 +0530
```

## Hard delete unpublished commits

```bash
# This will destroy any local modifications.
# Don't do it if you have uncommitted work you want to keep.
git reset --hard 34669d
```

Or save it by stashing it first

```bash
# Alternatively, if there's work to keep:
git stash
git reset --hard 34669d
git stash pop
# This saves the modifications, then reapplies that patch after resetting.
# You could get merge conflicts, if you've modified things which were
# changed since the commit you reset to.
```

## Undo published commits with new commits

Git lore tells us that one should never rewrite history. So if you have already published the commits it might be better to create new commits that revert the commits instead of rewriting the history. 

For more info see this excellent StackOverflow post: 

* https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit
