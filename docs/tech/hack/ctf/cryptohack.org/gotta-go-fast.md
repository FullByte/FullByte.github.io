# Gotta go fast

Notes from challenges I did @ <https://cryptohack.org>.

## Client

``` python
from pwn import * # pip3 install pwntools
import json
import time
from Crypto.Util.number import long_to_bytes
import hashlib

def GetChallenge(JSON):
    r.sendline(json.dumps(JSON).encode())
    return r.recvline()
    
def encrypt(b):
    key = hashlib.sha256(long_to_bytes(int(time.time()))).digest()
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()

# Connect
r = remote('socket.cryptohack.org', 13372) 
getFlagJSON = { "option": str("get_flag") } # JSON string to get flag
GetChallenge(getFlagJSON) # Say Hi

# Do This While there is no error
result = None
while result is None:
    try:
        receivedflag = json.loads(GetChallenge(getFlagJSON).decode())['encrypted_flag'] #63727970746f7b7430305f663473745f7430305f667572693075357d
        result = bytearray.fromhex(encrypt(bytes.fromhex(receivedflag))).decode()
        print(result)
    except:
         pass
```

## Server

``` python
#!/usr/bin/env python3

import time
from Crypto.Util.number import long_to_bytes
import hashlib
from utils import listener

FLAG = b'crypto{????????????????????}'


def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()


def encrypt(b):
    key = generate_key()
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()


class Challenge():
    def __init__(self):
        self.before_input = "Gotta go fast!\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_flag':
            return {"encrypted_flag": encrypt(FLAG)}

        elif your_input['option'] == 'encrypt_data':
            input_data = bytes.fromhex(your_input['input_data'])
            return {"encrypted_data": encrypt(input_data)}

        else:
            return {"error": "Invalid option"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13372)
```
