# py2ai: Python compiler for MIT App Inventor
This is a library that compiles Python code to App Inventor .aia projects.

This library uses `ast` to parse Python code into a syntax tree and attempts to processes each statement and convert it into an App Inventor block. It also inserts a standard Blocks library into each screen to use many Python features (e.g. `__getitem__`).

## Command line tool
```
$ python3 -m py2ai --help
usage: py2ai [-h] SUBCOMMAND ...

compile and modify .aia projects with Python code

positional arguments:
  SUBCOMMAND  subcommand to execute
    ls        view contents of an .aia project
    create    create an .aia project
    modify    modify an .aia file

options:
  -h, --help  show this help message and exit
```

## Usage
The Python program below creates a counter with a button that updates the label and a button that closes the application.

```python
import random
from py2ai.components import *
from py2ai.magic import *

# Create components
Screen1 = Form(BigDefaultText=True)  # Screens are called Forms in code
Label1 = Label(FontBold=True, Text='0')  # These are builder properties
Button1 = Button(Text='Click me!')
Button2 = Button(Text="Don't click me!")

# This compiles into a "procedure with returns" block
def onclick():
    # This compiles into a "initialize local in ..." block
    text = Label1.Text  # This compiles into a "get Label1.Text" block
    # This compiles into a lot of blocks
    text = text + str(random.randrange(10))
    # This compiles into a "set Label1.Text to (get variable 'text')" block
    Label1.Text = text

def onclose():
    # This compiles into a "close application" block
    raise CloseApplication

# This compiles into a "on Button1.Click" block
Button1.on_Click(onclick)
Button2.on_Click(onclose)
```

The code is not directly executable, but you can compile it with this library (or the command line tool) to generate an .aia project.

## Supported Python statements
* Constants (`123.45`, `[1, 2, 3]`, `{4: 5}`, `'string'`, `None`)
* Variables, both global and local
* `global var_name`
* `+`, `-`, `*`, `/`, `//`
* `+=`, `-=`, `*=`, `/=`, `//=`
* `==`, `!=`, `<`, `<=`, `>`, `>=`
* `and`, `or`
* `in`
* `__getitem__`
  * `{1: 2}[1]`
  * `[0, 1, 2][1]`
  * `[0, 1, 2][0:1]`
* `__setitem__`
  * `some_dict[1] = 2`
  * `some_list[2] = 3`
* Functions (procedures)
  * `def some_func(arg): return arg + 1`
* Component creation
  * `Button1 = Button(Text='Hello World')`
  * `Button1 = CreateComponent(Button, Text='Hello World')`
* Component retrieval (component defined elsewhere)
  * `Button1: Button = GetComponent`
* Component properties
  * `text = Button1.Text`
  * `Button1.Text = 'Hello there'`
* Component methods
  * `Notifier1.ShowAlert('Hello World')`
* Component events
  * `Button1.on_Click(some_func)`
* Any Component events
  * `Button1.on_any_Click(some_func)`
* Explicit schema override
  * `__py2ai__schema__ = {"Source": "Form", "Properties": {...}, ...}`
* Close screen/application
  * `raise CloseScreen`
  * `raise CloseApplication`
* `if`/`elif`/`else` statements
* `for` statements
  * Special-cased `for var in range(...)`
* `break`
* Selected methods (see below)
* Selected functions (see below)

## Supported methods
* `list`
  * `list.append(x)`
  * `list.clear()`
  * `list.copy()`
  * `list.count(x)`
  * `list.extend(x)`
  * `list.index(x, [start, [stop]])`
  * `list.insert(i, x)`
  * `list.pop(x)`
  * `list.remove(x)`
  * `list.reverse()`

## Supported functions
* Builtin: `int`, `str`, `len`, `range`, `min`, `max`
* Extended: `web_get`, `web_post`, `web_delete`, `obfs_text`
* `random`: `random`, `randrange`, `randint`, `choice`
* `json`: `dumps`, `loads`
