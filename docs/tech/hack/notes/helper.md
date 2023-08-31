# Helper

## Chat between two users with netcat

- User 1 (with IP 10.9.182.239) runs this command: ```nc -l -p 3303```
- Other chat user then runs this command: ```nc 10.9.182.239 3303```

## guake

Install

``` sh
sudo apt-get update
sudo apt-get install guake -y
sudo cp /usr/share/applications/guake.desktop /etc/xdg/autostart/
```

- open: `F12`
- new tab: `CTRL`+`SHIFT`+`T`

## Wireshark

Wireshark

## seclists

seclists ```sudo apt -y install seclists```

## wfuzz

<https://github.com/xmendez/wfuzz>

## Spiderfoot

<https://github.com/smicallef/spiderfoot>

## Hash-identifier

Identification of various hashes

### Decodify

<https://github.com/s0md3v/Decodify>

## MacChanger

MacChanger

## Sleuthkit

<http://www.sleuthkit.org/>

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

Eyewitness (screenshot pws): ```sudo apt install eyewitness```

## FreeIPMI

FreeIPMI: ```sudo apt install freeipmi-tools```

## Frogger

``` sh
git clone https://github.com/commonexploits/vlan-hopping /opt/frogger
ln -s /opt/frogger/froggers.sh /usr/local/bin/froggers.sh
chmod +x /opt/frogger/froggers.sh
```

## hcxtools

hcxtools to convert packets: ```sudo apt install hcxdumptool hcxtools```

## mimikatz

source: <https://github.com/gentilkiwi/mimikatz>

## YARA

[YARA](https://virustotal.github.io/yara/), is the "pattern matching swiss knife for malware researchers (and everyone else)". ([source](https://github.com/virustotal/yara))

Here are [some rules](https://github.com/Yara-Rules/rules) and [some usage examples](https://github.com/InQuest/awesome-yara).

Simple example to find the EICAR testfile:

```yml "yara-EICAR-rule.yar"
rule eicaryara   {
    meta:
      author="0xfab1"
      description="EICAR example"
    strings:
      $a="X5O"
      $b="EICAR"
      $c="ANTIVIRUS"
      $d="TEST"
    condition:
      $a and $b and $c and $d
  }
```

Then run ```yara yara-EICAR-rule.yar targetfile```

## oledump-py

[oledump.py](https://blog.didierstevens.com/programs/oledump-py/) is a program by [Didier](http://didierstevens.com/) [Stevens](https://twitter.com/DidierStevens) to analyze OLE files. oledump requires Python module [OleFileIO_PL](http://www.decalage.info/python/olefileio). [Olefile](https://olefile.readthedocs.io/en/latest/OLE_Overview.html) is a Python package to parse, read and write [Microsoft OLE2 files](https://en.wikipedia.org/wiki/Compound_File_Binary_Format) (also called Structured Storage, Compound File Binary Format or Compound Document File Format), such as Microsoft Office 97-2003 documents, vbaProject.bin in MS Office 2007+ files, Image Composer and FlashPix files, Outlook messages, StickyNotes, several Microscopy file formats, McAfee antivirus quarantine files, etc.

- Run oledump on an supported file and it will show you the available streams
- The letter M next to stream indicate that the stream contains VBA macros
- Use -s to select a stream; Use -v to decompress the VBA macro source code, use -d to dump the output
- You can scan the streams with [YARA rules](#yara) and write python plugins
