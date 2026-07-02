---
date: 2023-12-22
modified: 2024-05-29
description: Install form source
tags:
- Tech
- Tools
---

# Nmap

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Documentation |       |

Install form source

``` sh
wget https://nmap.org/dist/nmap-7.93.tar.bz2
bzip2 -cd nmap-7.93.tar.bz2 | tar xvf -
cd nmap-7.93
./configure
make
sudo make install
```
