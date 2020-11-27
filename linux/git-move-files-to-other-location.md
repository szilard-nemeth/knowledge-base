Move files to other location
============

1. Save all commits to patch files
Warning: THIS WON'T INCLUDE INITIAL COMMIT!
```
git format-patch $(git rev-list --max-parents=0 HEAD)..HEAD -o /tmp/patches
```

2. PROPER WAY:
https://stackoverflow.com/a/40884093/1106893 
Explanation: '4b825dc642cb6eb9a060e54bf8d69288fbee4904' is the id of the "empty tree"

```
git format-patch 4b825dc642cb6eb9a060e54bf8d69288fbee4904..HEAD -o /tmp/patches
```

3. Rewrite file paths to conform with the new path in the repo: 
```
#ls -1 /tmp/patches | sort | xargs git am --directory=sbin/python
ls -d /tmp/patches/* | sort | xargs git am --directory=sbin/python
```
