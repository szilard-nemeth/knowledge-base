

## Define a test struct, run all testcases [TEMPLATE]
```go
tests := []struct {
		name                string
		description         string
		//more fields if required
	}{
		{
			name:              "test name",
			description:       "test description",
			
		},
	}



// invoke
for _, test := range tests {
	t.Run(test.name, func(t *testing.T) {

	//invoke function under test	
	})
}
```


## Asserting errors
```go
import (
    "errors"
    "testing"
    "github.com/stretchr/testify/assert"
)

func TestSomeFunction(t *testing.T) {
    err := someFunc()
    assert.Error(t, err, "Expected an error")
    assert.ErrorIs(t, err, ErrNotFound, "Expected ErrNotFound")
    assert.EqualError(t, err, "something failed: not found", "Expected specific error message")
    assert.Contains(t, err.Error(), "failed", "Expected substring in error message")
}
```



## Run tests with `go test`
https://www.brandongreeley.com/selectively-running-tests-in-go/
[cloudera] https://gemini.google.com/app/a60a0f42383f1e3d

### Run a specific test
`go test -v -run "TestBackupRestoreAirflowJobWithAirflowFileMountsAndRename" ./pkg/runtime/service/`


### Run all tests in package
`go test -count=1 -v ./pkg/runtime/service/`


### Run tests in a file
`go test -count=1 -v ./pkg/runtime/service/v1archive_test.go`


## Run all tests from a file, individually
`grep -o "func Test[^ (]*" pkg/runtime/service/v1archive_test.go | sed 's/func //' | xargs -I {} sh -c 'go test -count=1 -v -run "{}" ./pkg/runtime/service/'`


## All in one
```bash
cd /Users/snemeth/development/cloudera/cde/dex
go test -count=1 -v -run "TestBackupRestoreAirflowJobWithAirflowFileMountsAndRename" ./pkg/runtime/service/ &> /tmp/go_test_output_TestBackupRestoreAirflowJobWithAirflowFileMountsAndRename.log
go test -count=1 -v ./pkg/runtime/service/ &> /tmp/go_test_output_pkg-runtime-service.log
go test -count=1 -v ./pkg/runtime/service/v1archive_test.go &> /tmp/go_test_output_pkg-runtime-service-v1archive_test.log
```


## Forcing a test to run, without cache
`go clean -testcache`

or Use a non-cacheable flag: Certain flags, like `-count=1`, are not considered "cacheable" and will force the tests to run. This is the idiomatic way to disable caching for a single run.