# John

John the ripper

**crack keyfile PW**

```sh
gzip -d /usr/share/wordlists/rockyou.txt.gz
/usr/share/john/ssh2john.py ssh-key-kay.txt > forjohn.txt
john forjohn.txt --wordlist /usr/share/wordlists/rockyou.txt
```
