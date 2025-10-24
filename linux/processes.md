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

## Get environment of process

https://unix.stackexchange.com/questions/29128/how-to-read-environment-variables-of-a-process
Good answer: https://unix.stackexchange.com/a/70636

> You can read the initial environment of a process from /proc/<pid>/environ. If a process changes its environment, then in order to read the environment you must have the symbol table for the process and use the ptrace system call (for example by using gdb) to read the environment from the global char **__environ variable.


### Splitting outpuf of /proc/<pid>/environ
https://askubuntu.com/questions/978711/how-do-i-split-a-proc-environ-file-in-separate-lines

```
xargs -0 -L1 -a /proc/self/environ
```