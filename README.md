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
