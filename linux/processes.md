# Process commands


## Kill process based on grep expression:
```kill $(ps aux | grep 'mapreduce-examples' | awk '{print $2}')```

## Wait for process to complete by its pid:
```tail --pid=$pid -f /dev/null```
Details: https://unix.stackexchange.com/a/427133/189441


## Print all process names that are connected to the internet: 
```sudo lsof -nPi | cut -f 1 -d " " | uniq | tail -n  +2```


## Run process in background (Python)
DETAILS: https://askubuntu.com/a/396655

> Use no hangup to run the program in the background even if you close your terminal,
```
nohup /path/to/test.py &
```

> or simply (without making any change in your program)

```
nohup python /path/to/test.py &
```
> Do not forget to use & to put it in the background.


