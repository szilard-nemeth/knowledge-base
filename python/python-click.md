# Click

## Do not truncate help texts
https://stackoverflow.com/questions/44127978/helpformatter-in-click

> If you are trying to to avoid the truncation of the help string, this can be accomplished via the short_help 
> parameter. short_help is generally derived from help but truncated. If passed explicitly, the entire string will be 
> displayed.


## Mutually exclusive options
https://stackoverflow.com/questions/44247099/click-command-line-interfaces-make-options-required-if-other-optional-option-is


## Click testing
https://stackoverflow.com/questions/53203500/unittest-for-click-module

```python
import unittest
import sfind
from click.testing import CliRunner

class TestSfind(unittest.TestCase):

    def test_sfind(self):

        runner = CliRunner()
        result = runner.invoke(
            sfind.find, '--name url --filename good'.split(), input='2')
        self.assertEqual(0, result.exit_code)
        self.assertIn('Find: 3 sample', result.output)
```


### Passing Context object to CliRunner
https://stackoverflow.com/questions/40443368/how-can-i-pass-a-ctx-context-to-clirunner

Answer: https://stackoverflow.com/a/40443542

Code: 
```python
import click
from click.testing import CliRunner

class Config():
    def __init__(self):
        self.value = 651

@click.command()
@click.pass_obj
def print_numberinfo(obj):
    if not hasattr(obj, 'value'):
        obj = Config()
    click.echo(obj.value)

def test_print_numberinfo():
    obj = Config()
    obj.value = 777
    runner = CliRunner()
    # how do I pass ctx to runner.invoke?
    result = runner.invoke(print_numberinfo, obj=obj)
    assert result.output == str(obj.value) + '\n'
```


### ValueError: I/O operation on closed file in testing #824
https://github.com/pallets/click/issues/824
https://stackoverflow.com/questions/16039463/how-to-access-the-py-test-capsys-from-inside-a-test
https://github.com/pytest-dev/pytest/issues/2504#issuecomment-309475790
https://github.com/pytest-dev/pytest/issues/5289
https://discuss.python.org/t/best-practice-to-do-the-same-tests-in-pytest-with-different-classes/24267/17