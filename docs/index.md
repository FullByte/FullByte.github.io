# Welcome

Publishing my notes in a wiki format has been great exercise for me to to keep a certain level of quality and stay organized. As longs as this works well for me I will continue doing so :)

The content may appear random as it is basically anything I find interesting and noteworthy. ¯\(ツ)/¯
I hope you appreciate the lack of adds, pop-ups and 3rd party dependencies (frames, javascript,..).
Use the navigation on the left to find the topics of interest or use the search bar and a keyword.
The content of this site is mainly written in english aside of some very few german posts.

Query a DNS for TXT records of [0xfab1.net](https://0xfab1.net) to get some contact details:

Linux

```bash
curl -s -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=0xfab1.net&type=TXT'  | jq -r .Answer[].data
```

Windows

```powershell
(Resolve-DnsName 0xfab1.net -Type TXT | Select-Object -ExcludeProperty Strings).Text | Format-Table
```

and you will receive this result:

```shell
"v=me; github=https://github.com/FullByte"
"v=me; twitter=https://twitter.com/ZeroGdoubleD"
"v=me; about=https://0xfab1.net/about/"
"v=me; gravatar=https://de.gravatar.com/0xfab1"
```

I hope you enjoy the content and found your visit worthwhile :)

Regards,
0xfab1
