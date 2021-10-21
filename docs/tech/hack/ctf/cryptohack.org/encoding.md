# Encoding

Notes from challenges I did @ <https://cryptohack.org>.

Encoding Challenge

## Server

```python
#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener
import base64
import codecs
import random

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
with open('/usr/share/dict/words') as f:
    WORDS = [line.strip().replace("'", "") for line in f.readlines()]


class Challenge():
    def __init__(self):
        self.challenge_words = ""
        self.stage = 0

    def create_level(self):
        self.stage += 1
        self.challenge_words = "_".join(random.choices(WORDS, k=3))
        encoding = random.choice(ENCODINGS)

        if encoding == "base64":
            encoded = base64.b64encode(self.challenge_words.encode()).decode() # wow so encode
        elif encoding == "hex":
            encoded = self.challenge_words.encode().hex()
        elif encoding == "rot13":
            encoded = codecs.encode(self.challenge_words, 'rot_13')
        elif encoding == "bigint":
            encoded = hex(bytes_to_long(self.challenge_words.encode()))
        elif encoding == "utf-8":
            encoded = [ord(b) for b in self.challenge_words]

        return {"type": encoding, "encoded": encoded}

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self, your_input):
        if self.stage == 0:
            return self.create_level()
        elif self.stage == 100:
            self.exit = True
            return {"flag": FLAG}

        if self.challenge_words == your_input["decoded"]:
            return self.create_level()

        return {"error": "Decoding fail"}


listener.start_server(port=13377)
```

## Client

```python
from pwn import * # pip3 install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random

r = remote('socket.cryptohack.org', 13377, level = 'debug') 

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(jsonstring):
    request = json.dumps(jsonstring).encode()
    r.sendline(request)

count = 0
while (count < 100):     
    count = count + 1
    print("--------------" + str(count) + "--------------") 

    received = json_recv()

    receivedtype = received["type"]
    encoded = received["encoded"]

    if receivedtype == "base64":
        decoded = base64.b64decode(encoded)
    elif receivedtype == "hex":
        decoded =  bytearray.fromhex(encoded).decode()
    elif receivedtype == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif receivedtype == "bigint":
        decoded = bytearray.fromhex(encoded[2:]).decode()
    elif receivedtype == "utf-8":
        decoded_temp = [chr(b) for b in encoded]
        decoded = ''.join([str(elem) for elem in decoded_temp]) 

    to_send = {
        "decoded": str(decoded)
    }

    print(to_send)

    json_send(to_send)    

else: 
    print("We are done here")
    json_recv()
```