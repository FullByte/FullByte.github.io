# Helper

## Chat between two users with netcat

- User 1 (with IP 10.9.182.239) runs this command:```nc -l -p 3303```
- Other chat user then runs this command:```nc 10.9.182.239 3303```

## Wireshark

Wireshark

## seclists

seclists```sudo apt -y install seclists```

## wfuzz

<https://github.com/xmendez/wfuzz>

TODO

## Spiderfoot

<https://github.com/smicallef/spiderfoot>

TODO

## Hash-identifier

Identification of various hashes

### Hash-identifier

### Decodify

<https://github.com/s0md3v/Decodify>

TODO


## MacChanger

MacChanger

## Sleuthkit

<http://www.sleuthkit.org/>

TODO

## pwdumpstats

Generate statistics from a pwdump file

``` sh
sudo git clone https://github.com/Dionach/pwdumpstats /opt/pwdumpstats
sudo ln -s /opt/pwdumpstats/pwdumpstats.py /usr/local/bin/pwdumpstats.py
```

Run example:

``` sh
pwdumpstats.py /usr/share/wordlists/rockyou.txt
```

## CODA Pentest Scripts

``` sh
git clone https://github.com/codagroup/pentestscripts /opt/pentestscripts
ln -s /opt/pentestscripts/sourcescan.py /usr/local/bin/sourcescan.py
```

## DDosify

High-performance load testing tool, written in Golang.

| Content | Info                                      |
|---------|-------------------------------------------|
| Source  | <https://github.com/ddosify/ddosify>      |
| Docker  |```docker run -it --rm ddosify/ddosify``` |

Example:

``` sh
ddosify -t 0xfab1.net
```

## Eyewitness

Eyewitness (screenshot pws):```sudo apt install eyewitness```

## FreeIPMI

FreeIPMI:```sudo apt install freeipmi-tools```

## Frogger

``` sh
git clone https://github.com/commonexploits/vlan-hopping /opt/frogger
ln -s /opt/frogger/froggers.sh /usr/local/bin/froggers.sh
chmod +x /opt/frogger/froggers.sh
```

## hcxtools

hcxtools to convert packets:```sudo apt install hcxdumptool hcxtools```

## mimikatz

source: <https://github.com/gentilkiwi/mimikatz>

## YARA

[YARA](https://virustotal.github.io/yara/), is the "pattern matching swiss knife for malware researchers (and everyone else)". ([source](https://github.com/virustotal/yara))

Here are [some rules](https://github.com/Yara-Rules/rules) and [some usage examples](https://github.com/InQuest/awesome-yara).
