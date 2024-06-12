# Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/install) are a great way to teach python and demonstrate exampes. You can view `ipynb` files online e.g. with [nextjournal](https://github.nextjournal.com) and [deepnote](https://deepnote.com/viewer) or install locally: ```pip install notebook```. To launch jupyter locally run```jupyter notebook```. There is a great extension for [vscode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

``` txt
                                 +%%%+
                                $$$$$$$
  +%+                           $$$$$$$
 $$$$$           ******          *%%%*
  *%*       ****************
        ************************
     ********              ********
   ***                            ***
  *                       _          *
  _  _   _  _ __   _   _ | |_  ___  _ _
 | || | | || '_ \ | | | || __|/ _ \| '_|
 | || |_| || |_) || |_| || |_ | __/| |
 | | \__,_|| .__/  \__, | \__|\___||_|
/_/        |_|     |___/
  *                                  *
   ***                            ***
     ********              ********
        ************************
            ****************
    +%%%+        ******
   $$$$$$$
   $$$$$$$
    *%%%*
```

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
