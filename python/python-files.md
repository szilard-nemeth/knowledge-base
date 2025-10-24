## How can I read a text file into a string variable and strip newlines?
https://stackoverflow.com/questions/8369219/how-can-i-read-a-text-file-into-a-string-variable-and-strip-newlines

```
from pathlib import Path
txt = Path('data.txt').read_text()
```