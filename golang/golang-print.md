## Print or log an array
```go
package main

import "fmt"

func main() {
	myArray := [3]int{1, 2, 3}
	mySlice := []string{"apple", "banana", "cherry"}

	fmt.Println("Logging an array:", myArray)
	fmt.Println("Logging a slice:", mySlice)

	// Using Printf with different format verbs
	fmt.Printf("Array with %%v: %v\n", myArray)   // Default format
	fmt.Printf("Slice with %%#v: %#v\n", mySlice) // Go-syntax representation
	fmt.Printf("Slice with %%+v: %+v\n", mySlice) // Includes field names for structs (if applicable)
}
```