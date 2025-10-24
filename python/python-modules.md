## Modules

### Install modules from program
https://stackoverflow.com/questions/4527554/check-if-module-exists-if-not-install-it

```
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])    
```


### List all modules from a package
https://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package

```
import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
import email

package = email
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print "Found submodule %s (is a package: %s)" % (modname, ispkg)
    
```


### Get file path of a module
https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
```
import os
path = os.path.abspath(a_module.__file__)

...
...

path = os.path.dirname(a_module.__file__)
```


### Import modules by name
https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string

```
>>> moduleNames = ['sys', 'os', 're', 'unittest'] 
>>> moduleNames
['sys', 'os', 're', 'unittest']
>>> modules = map(__import__, moduleNames)
```