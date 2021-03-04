# TryHackMe.com

Notes from challenges I did @ <https://tryhackme.com>.

## [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2)

### [Day 16] Scripting Help! Where is Santa?

Address is localhost because I port-forwarded the tryhackme machine over kali to my host.

```python
import requests 
for number in range (1,100,2): print(f'{number} --> ' + requests.get(f'http://localhost:8080/api/{number}').text)
```
