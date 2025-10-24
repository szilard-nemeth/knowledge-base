# Maps

## Check for key is in map? 
https://stackoverflow.com/questions/2050391/how-to-check-if-a-map-contains-a-key-in-go

```go
val, ok := myMap["foo"]
// If the key exists
if ok {
    // Do something
}
```

This initializes two variables. val is the value of "foo" from the map if it exists, or a "zero value" if it doesn't (in this case the empty string). ok is a bool that will be set to true if the key existed.

If you want, you can shorten this to a one-liner.
```go
if val, ok := myMap["foo"]; ok {
    //do something here
}
```
Go allows you to put an initializing statement before the condition (notice the semicolon) in the if statement. The consequence of this is that the scope ofval and ok will be limited to the body of the if statement, which is helpful if you only need to access them there.


### Complete code snippet
```go
myMap := map[string]int{
    "apple":  1,
    "banana": 2,
}

key := "apple"
value, ok := myMap[key]
if ok {
    // Key exists, and value is available
    println("Value:", value)
} else {
    // Key does not exist in the map
    println("Key not found")
}

key = "orange"
value, ok = myMap[key]
if ok {
    // Key exists, and value is available
    println("Value:", value)
} else {
    // Key does not exist in the map
    println("Key not found")
}
```


## How to copy a map? 
```go
package main

import "fmt"

func main() {
	originalMap := map[string]int{
		"a": 1,
		"b": 2,
		"c": 3,
	}

	copiedMap := make(map[string]int)

	for key, value := range originalMap {
		copiedMap[key] = value
	}

	fmt.Println("Original Map:", originalMap)
	fmt.Println("Copied Map:", copiedMap)
}
```

or by using: 
- https://pkg.go.dev/maps#Clone
- https://pkg.go.dev/golang.org/x/exp/maps#Copy


## Getting a slice of keys
https://stackoverflow.com/questions/21362950/getting-a-slice-of-keys-from-a-map

Code:
```go
keys := make([]int, len(mymap))

i := 0
for k := range mymap {
    keys[i] = k
    i++
}
```


## Create map from slice
```go
package main

import "fmt"

func main() {
    slice := []string{"apple", "banana", "cherry"}
    myMap := make(map[string]string)

    for _, item := range slice {
        myMap[item] = item
    }

    fmt.Println(myMap) // Output: map[apple:apple banana:banana cherry:cherry]
}
```