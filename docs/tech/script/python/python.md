# Python

## Links and Tools

Some nice tools to use for python

VSCode + Extensions

- TODO

Other IDE

- pydev <https://www.pydev.org>
- pycharm <https://www.jetbrains.com/pycharm/>
- spyder <https://github.com/spyder-ide/spyder>

## Code Snippets

### Requirements

Install requirements of a project: ```pip install -r requirements.txt```

Example

``` txt
###### Requirements without Version Specifiers ######
numpy
pynput
beautifulsoup4

###### Requirements with Version Specifiers ######
docopt == 0.6.2             # Version Matching. Must be version 0.6.2
keyring >= 4.2.1            # Minimum version 4.2.1
coverage != 3.6             # Version Exclusion. Anything except version 3.6
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*
```

### Web

- Webserver on Python 2: ```python -m SimpleHTTPServer 8008```
- Webserver on Python 3: ```python -m http.server 8008 --bind 127.0.0.1```

### String manipulation

- Convert Binary to String: ```b'a string'.decode('ascii')```
- Convet String to Integer: ```int(string)```
- Convert Int to String: ```str(integer)```
- Remove Duplicates from a List: ```L = list(set(L))```
- Input space separated integers in a list: ```lis = list(map(int, input().split()))```
- Get Integers from a String (space seperated): ```ints = [int(x) for x in S.split()]```
- Swap two numbers a and b: ```a, b = b, a```

### Functions

- Finding Factorial: ```fac=lambda(n):reduce(int.__mul__,range(1,n+1),1)``` or ```print(math.factorial(n))```
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
    ``` py title="randomstring.py"
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

- Execute Shell Commands

    ``` py title="execute-shell-command.py"
    import subprocess
    cmd = subprocess.Popen(
    ['ls', '-l', '.'],
    cwd='/',
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
    )
    stdout, stderr = cmd.communicate()
    print(stdout)
    print(stderr)
    ```

### Network

HTTP JSON request

``` py title="HTTP-JSON-request.py"
import json, urllib.request

req = urllib.request.Request("https://example.com")
req.add_header("Accept", "application/json")

try:
    r = urllib.request.urlopen(req)
    data = json.loads(r.read())
    print(json.dumps(data))
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

HTTP Plain request

``` py title="HTTP-Plain-request.py"
import urllib.request

req = urllib.request.Request("https://example.com")

try:
    r = urllib.request.urlopen(req)
    data = r.read().decode("utf-8")
    print(data)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
```

### Colors

Print some colors

``` py title="colors.py"
class colors:
reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'
class fg:
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
class bg:
black='\033[40m'
red='\033[41m'
green='\033[42m'
orange='\033[43m'
blue='\033[44m'
purple='\033[45m'
cyan='\033[46m'
lightgrey='\033[47m'

print(f"{colors.bold}{colors.fg.green}Success!")
```

### Argument Parsing

``` py
import argparse

parser = argparse.ArgumentParser(description="description")
parser.add_argument("input", help="Input", nargs='?')
parser.add_argument("output", help="Output", nargs='?')
parser.add_argument("--optional", help="optional", action='append')

args = parser.parse_args()

if args.optional is not None:
    print("The optional input was provided.")

print(args.input)
print(args.output)
```

### File Operations

- `x` creates new file, returns error when it exists.
- `a` appends to file, creates it when it does not exist.
- `w` overwrites file, creates it when it does not exist.

Append "Append example" to file.txt:

``` py
f = open("file.txt", "a")
f.write("Append example")
f.close()
```

Skip First Couple of Lines

``` py
with open('file.txt') as f:
lines_after_2 = f.readlines()[2:]
```

### Iteration

Range

``` py
for i in range(10):
print(i)
```

Deduplicate List

``` py
for i in mylist:
if i not in newlist:
newlist.append(i)

from collections import OrderedDict
newlist = list(OrderedDict.fromkeys(mylist))
```

### Databases

#### TinyDB

Install: ```pip install tinydb```

Example usage

``` py
from tinydb import TinyDB, Query

# Create DB
db = TinyDB('db.json')
db.insert({ 'type': 'OSFY', 'count': 700 })
db.insert({ 'type': 'EFY', 'count': 800 })
db.all()

# Update DB
db.update({'count': 1000}, Magazine.type == 'OSFY')
db.all()

# Search and List
Magazine = Query()
db.search(Magazine.type == 'OSFY')
db.search(Magazine.count > 750)

# Remove / Purge
db.remove(Magazine.count < 900)
db.all()
db.purge()
db.all()

# In-Memory Use
from tinydb.storages import MemoryStorage
db = TinyDB(storage=MemoryStorage)
```

#### SQLite

Example usage

``` py
import sqlite3

# Create DB
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS exampletable (id integer PRIMARY KEY, login text, email text)")
conn.commit()

# Add entry
def sql_insert(data):
    login = data[0]
    cursor.execute(f'SELECT login FROM exampletable WHERE login = "{login}"')
    results = cursor.fetchall()
    if not results:
        cursor.execute('INSERT INTO exampletable (login, email) VALUES (?, ?)', data)
        conn.commit()
    else:
        print(f'User {login} already in database')

data = ('0xfab1', 'mail@example.com')
sql_insert(data)

# Read entry
def sql_fetch():
    cursor.execute('SELECT * FROM exampletable')
    rows = cursor.fetchall()
    return rows

print(sql_fetch())
```

## PIP

PIP is a package manager for Python packages/modules.

- Update PIP: ```pip install --upgrade pip``` and see the version: ```pip --version```
- Install a package: ```pip install yourpackage```. You can now use```import yourpackage``` in your python script to include this package and call it's functions.
- List all packages installed: ```pip list```
- Uninstall all package: ```pip uninstall yourpackage```

Update all packages

- Linux (bash): ```pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U```
- Windows (cmd): ```for /F "delims= " %i in ('pip list --outdated') do pip install -U %i```
- Or use [pipupgrade](https://github.com/achillesrasquinha/pipupgrade) (Install: ```pip install pipupgrade```): ```pipupgrade --verbose --latest --yes```

## Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/install) are a great way to teach python and demonstrate exampes. You can view `ipynb` files online e.g. with [nextjournal](https://github.nextjournal.com) and [deepnote](https://deepnote.com/viewer) or install locally: ```pip install notebook```. To launch jupyter locally run```jupyter notebook```. There is a great extension for [vscode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

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

In case you have multiple python versions installed (like me) you need to explicitly mention to use 3.8.x! Run``` py –list``` to get your 3.8.x version. Mine is -3.8-64; your version may vary.

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
