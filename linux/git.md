Git commands
============
1. Change commit message all at once (remove some part of it)

```git filter-branch -f --msg-filter 'sed "s/<strtoreplace>//g"' -- --all```

2. Print list of changed files (name only)
`git diff --name-only`

3. Selective add (by patches)

`git add -p`

More info: https://gist.github.com/mattlewissf/9958704

4. Selective add (entire file, line granurality)

`git add -e`

More info: https://content.pivotal.io/blog/git-add-e

5. Diff changes in staged area

`git diff --cached`

6. List remote branches

`git ls-remote --heads <remote-name>`

7. Get repo root directory
`git rev-parse --show-toplevel`

8. Remove accidentally added files
```
git st --porcelain | grep AD | cut -d " " -f2 | xargs git co --
git st --porcelain | grep ".*.class" | cut -d ' ' -f3 | xargs git reset HEAD
```


### Clone and checkout in single command
https://stackoverflow.com/questions/18525152/git-clone-and-checkout-in-a-single-command

```
git clone u://r/l --branch x
```


### Check if a specific file or directory has changed
https://stackoverflow.com/questions/17797740/check-if-specific-file-in-git-repository-has-changed

```
git diff --exit-code test
```


### View a file on different branch, without checkout
https://stackoverflow.com/questions/7856416/view-a-file-in-a-different-git-branch-without-changing-branches

```
git show branch:file
```


### Check if branch exists
https://stackoverflow.com/questions/5167957/is-there-a-better-way-to-find-out-if-a-local-git-branch-exists

```
git rev-parse --verify <branch_name>
```

### List commits between 2 commit hashes in git
https://stackoverflow.com/questions/18679870/list-commits-between-2-commit-hashes-in-git
```
git rev-list --ancestry-path 7b4a07a..ecf5891
```


### Generate diff file of a specific commit in Git
https://stackoverflow.com/questions/42357521/generate-diff-file-of-a-specific-commit-in-git

```
git diff <commit-sha>^!
```


# Git log

## Show non-merge differences for two commits in git

https://stackoverflow.com/questions/4549157/show-non-merge-differences-for-two-commits-in-git
```
git log --no-merges -p branch-start..branch-end
```
