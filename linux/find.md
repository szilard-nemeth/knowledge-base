# File operations (find / ls)

## Extract files from jar file to console, print with separator

```find . -iname "*<somename>.jar" -exec sh -c "echo file: {}; unzip -p {} META-INF/services/javax.ws.rs.ext.MessageBodyWriter; echo '$\n\n'" \;```

## List recursive, show depth: 

```ls /export/apps -R | grep ":$" | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'```


## Remove multiple files: 

```find . -iname *versionsBackup -print0 | xargs -0 rm```

## Find for specific file types, grep in them:

```find / -regex ".*\.\(xml\|txt\|ini\|cfg\)" 2>/dev/null | xargs grep <string>```

## Find multiple files, with exclusion of filenames:

```find /opt/hadoop/share/hadoop/yarn/ -iname 'hadoop-yarn-server*nodemanager*' ! -iname "*test*.jar" ! -iname "*sources*jar" -printf "unzip -c %p | grep -q '' && echo %p\n" | sh```

## Find and do something with results:
```
find . -type d -name venv -print0 | xargs -0 <command>
```

## Cat a file, then invoke xargs per line:
Related SO answer: https://stackoverflow.com/a/65708689/1106893
```
cat ~/Downloads/tmp | xargs -n1 -I{} md5 {}
```

Example: 
```
find . -type d -name venv -print0 | xargs -0 -I % find % -type d | grep ".*pythoncommons\|python_commons.*"
```

## Find + xargs, use special replacement character
```
find . -type d -name venv -print0 | xargs -0 -I % sh -c 'find % -type d'
```
