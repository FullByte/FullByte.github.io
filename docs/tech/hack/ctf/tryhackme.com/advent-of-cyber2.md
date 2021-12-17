# Advent of Cyber 2

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [Advent of Cyber 2](https://tryhackme.com/room/adventofcyber2).

## [Day 16] Scripting Help! Where is Santa?

Python One-Liner to query the API :)

``` python
import requests 
for number in range (1,100,2): print(f'{number} --> ' + requests.get(f'http://localhost:8080/api/{number}').text)
```
