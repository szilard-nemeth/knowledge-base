# Slices, Arrays

## Initialize a slice, inline
```go
package main

import "fmt"

func main() {
    // Inline initialization of an integer slice
    numbers := []int{1, 2, 3, 4, 5}
    fmt.Println("Numbers:", numbers) // Output: Numbers: [1 2 3 4 5]

    // Inline initialization of a string slice
    names := []string{"Alice", "Bob", "Charlie"}
    fmt.Println("Names:", names) // Output: Names: [Alice Bob Charlie]

    // Inline initialization of a slice of structs
    type Person struct {
        Name string
        Age  int
    }
    people := []Person{
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35},
    }
    fmt.Println("People:", people) // Output: People: [{Alice 30} {Bob 25} {Charlie 35}]

    // Empty slice initialization
    emptySlice := []int{}
    fmt.Println("Empty Slice:", emptySlice) // Output: Empty Slice: []
}
```

## Inline slice / slice literal
In Go, an inline slice, also known as a slice literal, provides a concise way to create and initialize a slice in a single line of code. It's particularly useful when you know the values of the slice elements at compile time.

```go
slice := []DataType{value1, value2, value3, ...}
```

Example code: 
```go
package main

import "fmt"

func main() {
    // Integer slice
    numbers := []int{1, 2, 3, 4, 5}
    fmt.Println("Numbers:", numbers) // Output: Numbers: [1 2 3 4 5]

    // String slice
    names := []string{"Alice", "Bob", "Charlie"}
    fmt.Println("Names:", names) // Output: Names: [Alice Bob Charlie]

    // Boolean slice
    flags := []bool{true, false, true}
    fmt.Println("Flags:", flags) // Output: Flags: [true false true]

    // Struct slice
    type Person struct {
        Name string
        Age  int
    }
    people := []Person{
        {"Alice", 30},
        {"Bob", 25},
        {"Charlie", 35},
    }
    fmt.Println("People:", people) // Output: People: [{Alice 30} {Bob 25} {Charlie 35}]
}
```

# Structs

## Anonymous structs
In Go, an anonymous struct is a struct type defined without a name. It is useful for creating data structures on the fly without the need for a formal type declaration. 

```go
package main

import "fmt"

func main() {
    // Anonymous struct declaration and initialization
    person := struct {
        Name string
        Age  int
    }{
        Name: "John Doe",
        Age:  30,
    }

    fmt.Printf("%+v\n", person) // Output: {Name:John Doe Age:30}
}
```

### Anonymous struct with embedding
Anonymous structs can be embedded within other structs, both named and anonymous.

Limitations
- Anonymous structs cannot have methods directly associated with them.
- They cannot be referenced by name elsewhere in the code.
- When used in composite literals, the full type definition must be repeated.


```go
package main

import "fmt"

func main() {
    // Anonymous struct embedded in a named struct
    type Employee struct {
        ID     int
        Info struct {
            Name string
            Age  int
        }
    }

    emp := Employee{
        ID: 123,
        Info: struct {
            Name string
            Age  int
        }{
            Name: "Jane Smith",
            Age:  25,
        },
    }

  fmt.Printf("%+v\n", emp)  // Output: {ID:123 Info:{Name:Jane Smith Age:25}}
}
```


## Fixed size array
```go
// Declare an array of 5 integers, initialized to default values (0 for int)
var numbers [5]int

// Declare and initialize an array with specific values
names := [3]string{"Alice", "Bob", "Charlie"}

// Use the ellipsis (...) to let the compiler infer the size
// The array will have the exact number of elements provided
flags := [...]bool{true, false, true}

// Access elements using index (0-based)
firstNumber := numbers[0] // Access the first element
names[1] = "David"       // Modify the second element

// Get the length of the array using the len() function
length := len(numbers) // length will be 5
```

## Pass fixed size array as parameter
It's important to note that in Go, arrays are value types, meaning that when you pass an array to a function, a copy of the array is created. If you want to modify the original array within the function, you should pass a pointer to the array instead. Also, the size of the array is part of its type, so the function will only accept arrays of that specific size. If you need to work with arrays of varying sizes, it is better to use slices.

```go
package main

import "fmt"

func processStrings(strArray [3]string) {
    for _, str := range strArray {
        fmt.Println(str)
    }
}

func main() {
    stringArray := [3]string{"apple", "banana", "cherry"}
    processStrings(stringArray)
}
```


# Loops
## Unindexed for loop
```go
package main

import "fmt"

func main() {
    numbers := []int{10, 20, 30, 40, 50}

    // Iterate over the slice without using the index
    for _, num := range numbers {
        fmt.Println("Number:", num)
    }

    // Iterating over a map
    ages := map[string]int{"Alice": 30, "Bob": 25, "Charlie": 35}
    for name, age := range ages {
        fmt.Printf("%s is %d years old\n", name, age)
    }

    // Iterating over a string (runes)
    message := "Hello, Go!"
    for _, char := range message {
        fmt.Printf("Character: %c\n", char)
    }
}
```

## Iterate over map
```go
package main

import "fmt"

func main() {
    myMap := map[string]int{
        "apple": 1,
        "banana": 2,
        "cherry": 3,
    }

    // Iterate over keys and values
    fmt.Println("Iterating over keys and values:")
    for key, value := range myMap {
        fmt.Printf("Key: %s, Value: %d\n", key, value)
    }

    // Iterate over keys only
    fmt.Println("\nIterating over keys only:")
    for key := range myMap {
        fmt.Printf("Key: %s\n", key)
    }

    // Iterate over values only (less common)
    fmt.Println("\nIterating over values only:")
    for _, value := range myMap {
        fmt.Printf("Value: %d\n", value)
    }
}

```


# Errors

## How to return a new error? 
```go
import "errors"

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	result, err := divide(10, 2)
	if err != nil {
		// Handle the error
		println("Error:", err.Error())
		return
	}
	println("Result:", result)

	result, err = divide(10, 0)
	if err != nil {
		// Handle the error
		println("Error:", err.Error())
		return
	}
	println("Result:", result)
}

```

# Passing parameters


## Inline map parameter
```go
func processMap(data map[string]int) {
    for key, value := range data {
        // Process the key-value pairs
        fmt.Println("Key:", key, "Value:", value)
    }
}

func main() {
    myMap := map[string]int{"apple": 1, "banana": 2, "cherry": 3}
    processMap(myMap)
}
```

More details: https://docs.google.com/document/d/13AAWj91ahbkOPVUBGAdU7rIibaIZpxtcN8RuLgGrMVY/edit?tab=t.0

# Testing

## Testify

### Assert that a value is among a set of expected values
```go
import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestValueAmong(t *testing.T) {
	expectedValues := []int{1, 2, 3, 4, 5}
	valueToCheck := 3

	assert.Contains(t, expectedValues, valueToCheck, "The value should be among the expected values")

	valueToCheck = 6
	assert.NotContains(t, expectedValues, valueToCheck, "The value should not be among the expected values")
}
```


# Type assertions

```go
var i interface{} = "hello"

s, ok := i.(string)
if ok {
    // i is of type string
    fmt.Println("Type is string, value:", s)
} else {
  // i is not of type string
    fmt.Println("Type is not string")
}

f, ok := i.(float64)
if ok {
    // i is of type float64
    fmt.Println("Type is float64, value:", f)
} else {
    // i is not of type float64
    fmt.Println("Type is not float64")
}
```

More details: https://docs.google.com/document/d/16mvIgVg78emF-FaeENedVo5U14r3rvahWYcQXbjR_a0/edit?tab=t.0

# Discussions
https://stackoverflow.com/questions/34018908/golang-why-dont-we-have-a-set-datastructure