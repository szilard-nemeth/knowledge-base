# Shell redirects

## Capturing STDERR and STDOUT to file using tee
```
find . 2>&1 | tee /tmp/output.txt
```