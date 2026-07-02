---
date: 2023-12-22
modified: 2023-12-22
description: Notes from challenges I did @ <https://cryptohack.org>.
tags:
- Tech
- Security
---

# FavByte

Notes from challenges I did @ <https://cryptohack.org>.

``` python
from pwn import xor

KEY1x = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

count = 0
while count < 55:
    count += 1
    try:
        possibleKey = (xor(KEY1x, count)).decode()
        if possibleKey.startswith("crypto"):
            print(possibleKey)
    except:
        print("An exception occurred wtih ", str(count)) 
```
