# Python

Some nice tools to use for python

VSCode + Extensions

- TODO

Other IDE

- pydev <https://www.pydev.org>
- pycharm <https://www.jetbrains.com/pycharm/>
- spyder <https://github.com/spyder-ide/spyder>

## PIP

PIP is a package manager for Python packages/modules.

- Update PIP: ```pip install --upgrade pip``` and see the version: ```pip --version```
- Install a package: ```pip install yourpackage```. You can now use ```import yourpackage``` in your python script to include this package and call it's functions.
- List all packages installed: ```pip list```
- Uninstall all package: ```pip uninstall yourpackage```

Update all packages

- Linux (bash): ```pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U```
- Windows (cmd): ```for /F "delims= " %i in ('pip list --outdated') do pip install -U %i```
- Or use [pipupgrade](https://github.com/achillesrasquinha/pipupgrade) (Install: ```pip install pipupgrade```): ```pipupgrade --verbose --latest --yes```

## Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/install) are a great way to teach python and demonstrate exampes. You can view `ipynb` files online e.g. with [nextjournal](https://github.nextjournal.com) and [deepnote](https://deepnote.com/viewer) or install locally: ```pip install notebook```. To launch jupyter locally run ```jupyter notebook```. There is a great extension for [vscode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

It is possible to create a jupyter notebook using python ([source](https://gist.github.com/fperez/9716279))

``` py
import nbformat as nbf
nb = nbf.v4.new_notebook()
text = """# My first automatic Jupyter Notebook"""
code = """print("hello world")"""
nb['cells'] = [nbf.v4.new_markdown_cell(text), nbf.v4.new_code_cell(code)]
fname = 'helloworld.ipynb'
with open(fname, 'w') as f:
    nbf.write(nb, f)
```

This example is a python script to create a jupyter notebook that shows how to create a jupyter notebook shwowing an example on how to use [itertools](https://docs.python.org/3/library/itertools.html) [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations).

``` py
import nbformat as nbf

nb = nbf.v4.new_notebook()
text = """\
# My first automatic Jupyter Notebook
This is an auto-generated notebook."""

code = """\

import nbformat as nbf

nb = nbf.v4.new_notebook()
text = \"""\ Function for Finding Factorial\"""

code = \"""\
from itertools import combinations
print([' '.join(i) for i in combinations("0xfab1", 2) ])
\"""\
    
nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code)]
fname = 'FindingFactorial.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)
"""

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(code)]
fname = 'AutomaticallyCreateAJupyterNotebook.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)
```

## Use multiple versions

The code you want to run may not support the latest python version which you installed locally. To solve the problem, [download](https://www.python.org/downloads/) and install the latest supported python version e.g. 3.8.x. for this example.

In case you have multiple python versions installed (like me) you need to explicitly mention to use 3.8.x! Run ``` py –list``` to get your 3.8.x version. Mine is -3.8-64; your version may vary.

In this example we are installing `MkDocs` dependencies using python version 3.8-64:

 ``` sh
py -3.8-64 -m pip install --upgrade pip --user
py -3.8-64 -m pip install MkDocs
py -3.8-64 -m pip install --upgrade MkDocs-material
```

In this example we are running `MkDocs` using python version 3.8-64:

 ``` sh
py -3.8-64 -m MkDocs serve
```

## Cool Stuff

## Web

- Webserver on Python 2: ``` python -m SimpleHTTPServer 8008```
- Webserver on Python 3: ``` python -m http.server 8008 --bind 127.0.0.1```

## String manipulation

- Remove Duplicates from a List: ```L = list(set(L))```
- Input space separated integers in a list: ```lis = list(map(int, input().split()))```
- Get Integers from a String (space seperated): ```ints = [int(x) for x in S.split()]```
- Swap two numbers a and b: ```a, b = b, a```

## Functions

- Finding Factorial ```fac=lambda(n):reduce(int.__mul__,range(1,n+1),1)``` or ```print(math.factorial(n))```
- Get even numbers: ```evenNumbers =[x for x in range(11) if x % 2 == 0]```
- Finding all subsets of a set: ```print(list(combinations([1, 2, 3, 4, 5, 6], 3)))```
- Finding greatest common divisor:

``` py
def gcd(a,b):
    while(b):a,b=b,a%b
        return a
```

- lambda function example using square root:

``` py
sqr = lambda x: x * x
print(sqr(5))
```

Create a random string

``` py
import random
import string

def getpassword(pwlength, extrachars):
    password = []
    for i in range(pwlength):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation + extrachars))
    return "".join(password)

print("English password: " + getpassword(22, ""))
print("German password:  " + getpassword(22, "äöüßÄÖÜẞ"))
print("Italian password: " + getpassword(22, "ÀÈÉÌÒÙàèéìòù"))
print("French password:  " + getpassword(22, "ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçrèéêëîïôœùûü"))
print("Spanish password: " + getpassword(22, "¡¿ÁÉÍÑÓÚÜáéíñóúü"))
```

## Art

- One liner code for half pyramid pattern: ```print('\n'.join('* ' * i for i in range(1, n + 1)))```

## Modules

- [itertools](https://docs.python.org/3/library/itertools.html)

## Cool Libraries

A list of cool libraries and examples on how to use them.

### Borb

[borb](https://github.com/jorisschellekens/borb) is a library for reading, creating and manipulating PDF files in python.

Install borb: `pip install borb`

Example:

``` py
from pathlib import Path

from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF

# create an empty Document
pdf = Document()

# add an empty Page
page = Page()
pdf.append_page(page)

# use a PageLayout (SingleColumnLayout in this case)
layout = SingleColumnLayout(page)

# add a Paragraph object
layout.add(Paragraph("Hello World!"))
    
# store the PDF
with open(Path("output.pdf"), "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)
```
