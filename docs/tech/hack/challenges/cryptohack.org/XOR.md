# XOR

Notes from challenges I did @ <https://cryptohack.org>.

## XOR starter

```python
text = "label"

number1= []
for c in text:
  number1.append(int.from_bytes(c.encode(), 'big')) 
print(number1)

number2 = 13

solution1 = []
for element in number1:
    solution1.append(element ^ number2)
print(solution1)

solution2 = []
for element in solution1:
    solution2.append(chr(element))
print(solution2)
```

## XORProperties

```python
from pwn import xor

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2x = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY3x = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGx = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY2 = (xor(bytes.fromhex(KEY1), bytes.fromhex(key2x))) # XOR for KEY2
KEY3 = (xor(KEY2, bytes.fromhex(KEY3x))) # XOR for KEY3
FLAG = (xor(bytes.fromhex(KEY1), KEY2, KEY3, bytes.fromhex(FLAGx))) # XOR for FLAG

print(FLAG)
```

## XOR you dont

```python
from pwn import xor

key = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# Alt 1
print((xor(key, "crypto{")).decode())
print((xor(key, "myXORkey")).decode())

# Alt 2
print(xor(flag, 'crypto{'.encode()))
print(xor(flag, 'myXORkey'.encode()))

```