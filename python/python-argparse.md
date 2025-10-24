# Argparse


## Pass list of something as CLI argument?
https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse

```
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
```

or 
```
parser.add_argument('-l','--list', action='append', help='<Required> Set flag', required=True)
```