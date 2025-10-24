# implement dry-run
https://unix.stackexchange.com/questions/433801/add-some-dry-run-option-to-script


# Head and tail from pipe at the same time
https://stackoverflow.com/questions/8624669/unix-head-and-tail-of-file
--> This does not work as expected


This works well: https://stackoverflow.com/questions/53885704/using-head-and-tail-command-in-unix-to-extract-items-from-a-file
`(head -3; tail -2) < emp.lst`


## Better way: Pipe to function
https://www.baeldung.com/linux/pipe-output-to-function


### Read stdin to variable
https://stackoverflow.com/questions/212965/how-to-read-mutliline-input-from-stdin-into-variable-and-how-to-print-one-out-in


### Split string into array
https://stackoverflow.com/questions/10586153/how-to-split-a-string-into-an-array-in-bash
```
IFS=', ' read -r -a array <<< "$string"
```

### Loop through an array of strings in Bash?
https://stackoverflow.com/questions/8880603/loop-through-an-array-of-strings-in-bash

```
## declare an array variable
declare -a arr=("element1" "element2" "element3")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"
   # or do whatever with individual element of the array
done
```


### Print array elements on separate lines in Bash?

Answer: https://stackoverflow.com/a/15692004
```
printf '%s\n' "${my_array[@]}"
```


### Check number of passed arguments to a script
https://stackoverflow.com/questions/18568706/check-number-of-arguments-passed-to-a-bash-script

```
if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
fi
```


### Get second from the last field with cut
https://stackoverflow.com/questions/17644000/how-to-get-second-last-field-from-a-cut-command

```
cat datafile | rev | cut -d '/' -f 2 | rev
```


### Check if bash array contains a value
https://stackoverflow.com/questions/3685970/check-if-a-bash-array-contains-a-value

#### One liner solution
https://stackoverflow.com/a/47541882
```
printf '%s\0' "${myarray[@]}" | grep -F -x -z -- 'myvalue'
```


### Check if variable a multi line string

This code snippet checks if the variable $variable contains a newline character (\n). The * symbols are wildcards, meaning "any number of characters". If a newline character is found anywhere within the variable's content, the condition is true, and the script will output "Variable is multiline". Otherwise, it will output "Variable is not multiline".
```
if [[ "$variable" == *$'\n'* ]]; then
  echo "Variable is multiline"
else
  echo "Variable is not multiline"
fi
```


### Launch new shell and inherit function
When executing a command with bash -c, the invoked shell starts as a non-interactive, non-login shell. By default, such shells do not inherit function definitions from the parent shell. This behavior is designed for security and isolation, ensuring that commands run in a controlled environment, unaffected by potentially unwanted functions defined in the parent shell.
To make functions available to bash -c, they must be explicitly exported using the export -f command before calling bash -c. Exporting a function makes it part of the environment, which is inherited by child processes, including those started with bash -c.

```
my_function() {
  echo "Hello from my_function"
}

export -f my_function

bash -c 'my_function'
```
In this example, my_function is defined and then exported. The subsequent call to bash -c executes the command within a new shell environment that includes the exported function, allowing it to be called successfully.

Or simply: 
```
git_script=$(find $HOME_LINUXENV_DIR/scripts -iname git.sh)
bash -c "source $git_script; _gh-list-branches"
```


### How do I get the directory where a Bash script is located from within the script itself?
https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script

Answer: https://stackoverflow.com/a/246128
```
#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
```
