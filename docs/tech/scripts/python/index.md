# Python

``` txt
               =========
            ===============
           =================
          ===  ==============
          ===================
                   ==========
   ========================== =======
 ============================ ========
============================= =========
============================ ==========
========================== ============
============ ==========================
========== ============================
========= =============================
 ======== ============================
  ======= ==========================
          ==========
          ===================
          ==============  ===
           =================
            ===============
               =========
```

![python_environment](https://imgs.xkcd.com/comics/python_environment.png)

IDE

- pydev <https://www.pydev.org>
- pycharm <https://www.jetbrains.com/pycharm/>
- spyder <https://github.com/spyder-ide/spyder>

## PIP

PIP is a package manager for Python packages/modules.

- Activate PIP: ```py -m ensurepip --upgrade```
- Update PIP: ```pip install --upgrade pip``` and see the version: ```pip --version```

Packages

- Install a package: ```pip install yourpackage```. You can now use```import yourpackage``` in your python script to include this package and call it's functions.
- List all packages installed: ```pip list```
- Uninstall all package: ```pip uninstall yourpackage```

Delete all packages

- Linux (bash): ```pip freeze | xargs sudo pip uninstall -y```
- Windows (psh): ```pip freeze | ForEach-Object { pip uninstall -y $_ }```

Update all packages

- Linux (bash): ```pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U```
- Windows (psh): ```for /F "delims= " %i in ('pip list --outdated') do pip install -U %i```
  - Or ```pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}```
  - Or use [pipupgrade](https://github.com/achillesrasquinha/pipupgrade) (Install: ```pip install pipupgrade```): ```pipupgrade --verbose --latest --yes```

Update virtual environment of "project"

```py
import pkg_resources
from subprocess import callfor dist in pkg_resources.working_set:
    call("python -m pip install --upgrade " + dist.project, shell=True)
```

## Using multiple python versions

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

## Requirements

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

Create requirements list and use this for upgrades

```py
pip list --format=freeze > requirements.txt
sed -i 's/==.*//g' requirements.txt
pip install --upgrade -r requirements.txt
```
