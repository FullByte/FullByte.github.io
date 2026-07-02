---
date: 2023-12-22
modified: 2023-12-22
description: Technical information on screens in movies often is just made up random stuff.
tags:
- Tech
- Art
---

# Movies

Technical information on screens in movies often is just made up random stuff.

Here are some exaples on how to create some nice visuals with no deeper meaning:

## Hex Editor

Use a hexeditor like [hexyl](https://github.com/sharkdp/hexyl) to show random information.

Install

```sh
sudo apt install hexyl
```

Run this

```sh
for n in $(seq 1 1000) ; do hexyl -n 512 /dev/urandom && sleep 0.1 && clear ; done
```
