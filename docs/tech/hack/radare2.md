# Radare2

|What|Where|
|-|-|
|Official Page|<https://www.radare.org>|
|Source|<https://github.com/radareorg/radare2>|
|Download|<https://github.com/radareorg/radare2/releases/>|
|Install|sys/install.sh|

## Example usage

Example from doing this tryhackme challenge <https://tryhackme.com/room/adventofcyber2> -> "[Day 17] Reverse Engineering ReverseELFneering"

```shell
r2 -d ./challenge1

b+1024
e anal.bb.maxsize=2048
aa

afl | grep main
pdf @main
db 0x00400b62
px @rbp-0xc
ds
dr
px @rbp-0x8
```
