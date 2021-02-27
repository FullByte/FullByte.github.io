# Python Snippets

## Cool Stuff

**Simple Webserver**
Python 2

```python
python -m SimpleHTTPServer 8008
```

Python 3

```python
python -m http.server
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
>>> def gcd(a,b):
...     while(b):a,b=b,a%b
...     return a
```
