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