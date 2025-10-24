## pytest

### Pytest logging
https://stackoverflow.com/questions/68290858/in-pycharm-using-pytest-integration-can-print-output-be-suppressed-for-passed

1. create a `pytest.ini` in your project and add this

```
[pytest]
log_cli = true
```

2. Inside your debug settings (clicking in edit settings at the left of run in the IDE), in additional arguments add
```
-s  --capture=no --log-cli-level=10 
```

### Capture stdout in testing
https://stackoverflow.com/questions/5136611/capture-stdout-from-a-script
https://stackoverflow.com/questions/56045623/how-to-capture-the-stdout-stderr-of-a-unittest-in-a-variable

--> contextlib.redirect_stdout: https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout

```
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    help(pow)
s = f.getvalue()
```


### Capture stdout in testing to a variable 2, with metaclass
Q: https://stackoverflow.com/questions/7472863/pydev-unittesting-how-to-capture-text-logged-to-a-logging-logger-in-captured-o/15969985#15969985
A: https://stackoverflow.com/a/15969985


### Pytest live logging
Great answer: https://stackoverflow.com/questions/4673373/logging-within-pytest-tests/51633600#51633600



### Get current test case name
https://stackoverflow.com/questions/17726954/py-test-how-to-get-the-current-tests-name-from-the-setup-method
```
os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
```

### Run specific file
https://stackoverflow.com/questions/36456920/specify-which-pytest-tests-to-run-from-a-file

```
py.test tests_directory/foo.py tests_directory/bar.py -k 'test_001 or test_some_other_test'
```


### How to implement xunit-style set-up / setup / teardown
https://docs.pytest.org/en/latest/how-to/xunit_setup.html#xunitsetup
https://stackoverflow.com/questions/26405380/how-do-i-correctly-setup-and-teardown-for-my-pytest-class-with-tests
https://pytest-with-eric.com/pytest-best-practices/pytest-setup-teardown/


## Unittest

### Disable individual test case execution
https://stackoverflow.com/questions/2066508/disable-individual-python-unit-tests-temporarily

```
@unittest.skip("reason for skipping")
def test_foo():
    print('This is foo test case.')


@unittest.skip  # no reason needed
def test_bar():
    print('This is bar test case.')
```