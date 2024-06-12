# Boogeyman 1

These notes are from a challenge I did @[tryhackme](https://tryhackme.com) called [Boogeyman 1](https://tryhackme.com/room/boogeyman1).

## Task 4 Network Traffic Analysis

Find the password in ```capture.pcapng```:

```sh
tshark -r capture.pcapng -Y "http.request.method == POST" -T fields -e http.request.uri -e http.request.method -e http.file_data | perl -ne 'while (m/\b(\d{2,3})\b/g) { print chr($1) } END { print "\n" }' | grep -i -A 1 "password"
```

Extract the kdbx file from the ```capture.pcapng```:

```sh
tshark -r capture.pcapng -Y "dns.qry.type == 1 && dns.qry.name contains bpakcaging.xyz" | grep -v response | grep -oE '[^.]+.bpakcaging.xyz' | sed -E 's/.* //;s/.bpakcaging.xyz$//' | uniq | grep -v cdn | grep -v files | tr -d '\n' |  xxd -p -r > pwd.kdbx
```
