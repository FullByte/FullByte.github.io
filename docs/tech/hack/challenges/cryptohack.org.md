# CryptoHack.org

Notes from challenges I did @ <https://cryptohack.org>.

## Gotta go fast

```python
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
