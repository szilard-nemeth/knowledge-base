# Python sorting


## TODO
[] https://realpython.com/python-sort/


## Sort a list of lists with a custom compare function
https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function

Answer: https://stackoverflow.com/a/57003713

```
from functools import cmp_to_key
sorted(mylist, key=cmp_to_key(lambda item1, item2: fitness(item1) - fitness(item2)))
```