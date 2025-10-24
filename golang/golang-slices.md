## Move item to 0th place in slice
```go
package main

import (
	"fmt"
	"slices"
)

func moveItemToFront[T comparable](slice []T, item T) []T {
	index := slices.Index(slice, item)

	if index == -1 {
		return slice // Item not found, return original slice
	}

	if index == 0 {
		return slice // Item already at the front, return original slice
	}

    // Remove item from current index
	slice = slices.Delete(slice, index, index+1)

    // Insert item at index 0
	slice = append([]T{item}, slice...)

	return slice
}

func main() {
	mySlice := []int{1, 2, 3, 4, 5}
	itemToMove := 3

    mySlice = moveItemToFront(mySlice, itemToMove)

	fmt.Println(mySlice) // Output: [3 1 2 4 5]

	mySlice = moveItemToFront(mySlice, 3)

	fmt.Println(mySlice) // Output: [3 1 2 4 5]

	mySlice = moveItemToFront(mySlice, 6)

	fmt.Println(mySlice) // Output: [3 1 2 4 5]
}
```

## Add items from a slice to another slice
```go
package main

import "fmt"

func main() {
    slice1 := []int{1, 2, 3}
    slice2 := []int{4, 5, 6}

    // Append all elements of slice2 to slice1
    slice1 = append(slice1, slice2...)

    fmt.Println(slice1) // Output: [1 2 3 4 5 6]
}
```