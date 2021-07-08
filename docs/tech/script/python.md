# Python

Some nice tools to use for python

VSCode + Extensions

- TODO

Other IDE

- pydev <https://www.pydev.org>
- pycharm <https://www.jetbrains.com/pycharm/>
- spyder <https://github.com/spyder-ide/spyder>

Jupyter Notebooks

- Jupyter Notebook: <https://jupyter.org/install>
- ipynb viewer online: <https://github.nextjournal.com/>
- ipynb viewer online: <https://deepnote.com/viewer>

## Cool Stuff

**Simple Webserver**
Python 2

```python
python -m SimpleHTTPServer 8008
```

Python 3

```python
python3 -m http.server 8009
```

## String manipulation

**Removing Duplicates from a List**

```python
L = list(set(L))
```

**Getting Integers from a string (space seperated)**

```python
ints = [int(x) for x in S.split()]
```

## Functions

**Finding Factorial**

```python
fac=lambda(n):reduce(int.__mul__,range(1,n+1),1)
```

**Finding greatest common divisor**

```python
def gcd(a,b):
    while(b):a,b=b,a%b
        return a
```
