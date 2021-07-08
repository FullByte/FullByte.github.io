# GoBuster

Find dirs that work

- Source: <https://github.com/OJ/gobuster>
- Install: ```sudo apt-get install gobuster```

Example:

```sh
gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u 10.10.112.131
gobuster dir -w /usr/share/SecLists/Discovery/Web-Content/big.txt -u 10.10.225.77
gobuster dir -w /usr/share/wordlists/dirb/common.txt -u 10.10.225.77
```
