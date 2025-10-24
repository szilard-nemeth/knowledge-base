## Type hinting

### Type hint, class as type
https://stackoverflow.com/questions/33387042/type-hinting-argument-of-type-class

```
from typing import Type

class X:
    """some class"""

def foo_my_class(my_class: Type[X], bar: str) -> None:
    """ Operate on my_class """
```


## String operations

### Remove prefix from string
https://stackoverflow.com/questions/16891340/remove-a-prefix-from-a-string

```
text.removeprefix(prefix)
```

or for older Python: 
```
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
```

## Dict operations

### Concatenate two or more dictionaries
https://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one


### Filter dict by set of keys
https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys

```
dict_you_want = {key: old_dict[key] for key in your_keys}
```