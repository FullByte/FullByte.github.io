# John

John the ripper

**crack keyfile PW**

```sh
gzip -d /usr/share/wordlists/rockyou.txt.gz
/usr/share/john/ssh2john.py ssh-key-kay.txt > forjohn.txt
john forjohn.txt --wordlist /usr/share/wordlists/rockyou.txt
```

## jwt2john

Convert a JWT to a format John the Ripper can understand.

Source: <https://github.com/Sjord/jwtcrack>

 ```sh
wget --quiet -O /usr/local/bin/jwt2john.py "https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py"
sed -i '1s;^;#!/usr/bin/env python\n;' /usr/local/bin/jwt2john.py
chmod +x /usr/local/bin/jwt2john.py
```
