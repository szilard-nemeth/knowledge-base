## Switch-case

```go
package main

import "fmt"

func main() {
    day := 4

    switch day {
    case 1:
        fmt.Println("Monday")
    case 2:
        fmt.Println("Tuesday")
    case 3:
        fmt.Println("Wednesday")
    case 4:
        fmt.Println("Thursday")
    case 5:
        fmt.Println("Friday")
    default:
        fmt.Println("Weekend")
    }
}
```


## Variadic functions
https://gobyexample.com/variadic-functions

```go
package main

import "fmt"

func sum(nums ...int) {
    fmt.Print(nums, " ")
    total := 0

    for _, num := range nums {
        total += num
    }
    fmt.Println(total)
}

func main() {

    sum(1, 2)
    sum(1, 2, 3)

    nums := []int{1, 2, 3, 4}
    sum(nums...)
}
```

## Check if value is in set of values
```go
set := map[string]bool{
    "apple":  true,
    "banana": true,
    "cherry": true,
}

valueToCheck := "banana"
  exists := set[valueToCheck]
  if exists {
      // Value exists in the set
  } else {
      // Value does not exist in the set
  }
```


Alternative Method Using the "Comma Ok" Idiom:

```go
valueToCheck := "grape"
_, exists := set[valueToCheck]
if exists {
    // Value exists in the set
} else {
    // Value does not exist in the set
}
```

## Loops

Invoke function while condition is true: 
```go
    package main

    import "fmt"

    func myRepeatingFunction() {
        fmt.Println("Function invoked!")
    }

    func main() {
        count := 0
        for count < 3 { // The loop continues as long as count is less than 3
            myRepeatingFunction()
            count++ // Increment count to eventually make the condition false
        }
        fmt.Println("Loop finished.")
    }
```


## Looping with ticker
```go
// Init and start a goroutine to periodically update the service ticket.
tktUpdateTicker := time.NewTicker(serviceTktUpdateInterval)
done := make(chan bool)

go func() {
    for {
        select {
        case <-tktUpdateTicker.C:
            updateErrors := idBrokerClient.updateServiceTickets()
            if len(updateErrors) != 0 {
                for _, err := range updateErrors {
                    dexlog.Error(err.Error())
                }
            }
        case <-done:
            return
        }
    }
}()
```



## Looping with ticker 2
```go
package main

import (
    "fmt"
    "time"
)

func main() {
    // Create a new ticker that ticks every 1 second
    ticker := time.NewTicker(1 * time.Second)
    defer ticker.Stop() // Ensure the ticker is stopped when main exits

    // Create a channel to signal when to stop the periodic execution
    done := make(chan bool)

    // Start a goroutine to handle the periodic function invocation
    go func() {
        for {
            select {
            case <-ticker.C: // Receive a tick from the ticker channel
                myFunction() // Invoke the desired function
            case <-done: // Receive a signal to stop
                return // Exit the goroutine
            }
        }
    }()

    // Simulate some other work in the main goroutine
    fmt.Println("Main program running...")
    time.Sleep(5 * time.Second) // Let the periodic function run for 5 seconds

    // Signal the goroutine to stop
    done <- true
    fmt.Println("Main program finished.")
}

// myFunction is the function to be invoked every second
func myFunction() {
    fmt.Println("Function invoked at:", time.Now().Format("15:04:05"))
}

```