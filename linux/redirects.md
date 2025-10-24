# Shell redirects

## Capturing STDERR and STDOUT to file using tee
```
find . 2>&1 | tee /tmp/output.txt
```

## Redirecting python / unbuffered mode
https://stackoverflow.com/questions/31345861/run-programs-in-background-and-redirect-their-outputs-to-file-in-real-time

The `-u` switch and the equivalent `PYTHONUNBUFFERED` environment variable forces stdout to be unbuffered. Try this:

```bash
#!/bin/bash
python -u 1.py > 1.output &
python -u 2.py > 2.output &
python -u 3.py > 3.output &
or
```

```bash
#!/bin/bash
export PYTHONUNBUFFERED=yes
python 1.py > 1.output &
python 2.py > 2.output &
python 3.py > 3.output &
```
Note that `-u` has side effects: read the doc to learn more.

Reference:
https://docs.python.org/2/using/cmdline.html#cmdoption-u
https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED
https://stackoverflow.com/questions/107705/disable-output-buffering
https://stackoverflow.com/questions/881696/unbuffered-stdout-in-python-as-in-python-u-from-within-the-program


## Echo to stderr
https://stackoverflow.com/questions/2990414/echo-that-outputs-to-stderr

```
>&2 echo "error"
```