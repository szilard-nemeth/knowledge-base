## Revert range of commits already pushed to master, create new PR from same commits but with different message


### 1. Identify range of commits
```
* ed26484 - (HEAD -> master, origin/master) DEX-15802. CI / set pytest testpaths=tests (10 hours ago) <Szilard Nemeth>
* ef54db9 - DEX-15802. CI / remove stale artifact upload (10 hours ago) <Szilard Nemeth>
* 6258013 - DEX-15802. CI / add comment (11 hours ago) <Szilard Nemeth>
* cbe42f3 - Fix tests (11 hours ago) <Szilard Nemeth>
* b6f9a2b - (tag: 1.0.3) update version of packages: google-api-wrapper2, python-common-lib (11 hours ago) <Szilard Nemeth>
* 249beec - DEX-15802. CI / remove linter (14 hours ago) <Szilard Nemeth>
* 1a9c806 - DEX-15802. poetry update quanta-client, continue-on-error (16 hours ago) <Szilard Nemeth>
* b16b3b9 - DEX-15802. poetry update quanta-client (16 hours ago) <Szilard Nemeth>
* 14ea4b7 - DEX-15802. Remove poetry localdev group (16 hours ago) <Szilard Nemeth>
* 2b9641f - DEX-15259. CI fixes (#14) (17 hours ago) <snemeth>
* cba8cb7 - update version of packages: google-api-wrapper2, python-common-lib (2 weeks ago) <Szilard Nemeth>
```

### 2. Define variables with range start + end
```
FIRST_COMMIT="cba8cb7"
LAST_COMMIT="ed26484"
```


### 3. Checkout new branch from the tip of the current master
```
git checkout -b DEX-15259-ci-fixes
```


### 4. Rebase interactively
```
git rebase $FIRST_COMMIT -i
```



### 5. Revert range of commits
https://stackoverflow.com/a/4992711

```
git checkout master
git revert $FIRST_COMMIT^..$LAST_COMMIT
```

#### Alternatively
Ancestry path: https://stackoverflow.com/a/44344164

```
for c in $(git rev-list --reverse --ancestry-path $FIRST_COMMIT^..$LAST_COMMIT); do
  echo "commit to revert: $c"
  git revert $c
done
```

### 6. Push changes to master
```
git co master; git push
```

### 7. Reword commits on feature branch + Create new PR
```
git checkout DEX-15259-ci-fixes
```
#### 7.1 Somehow, had to move back the branch manually
```
git co master; git br -f DEX-15259-ci-fixes $LAST_COMMIT; git co -
```

#### 7.2 Rebase + reword
```
git rebase -i $FIRST_COMMIT
```

#### 7.3 Check diff before pushing
```
git diff --name-only master..HEAD
git diff master..HEAD > /tmp/DEX-15259.diff && subl /tmp/DEX-15259.diff
```


#### 7.4 Push changes + Create new PR
```
git push --set-upstream origin DEX-15259-ci-fixes
```
