# curl

| What          | Where                                                                |
|---------------|----------------------------------------------------------------------|
| Official Page | <https://curl.se/>                                                   |
| Source        | <https://github.com/curl/curl>                                       |
| Download      | <https://github.com/curl/curl/releases>                              |
| Docs          | <https://everything.curl.dev> or <https://curl.se/docs/manpage.html> |
| Book          | <https://curl.se/docs/>                                              |
| Windows       | `scoop install curl`                                                 |
| Ubuntu        | `sudo apt -y install curl`                                           |

## Random Examples

Example to check /24 range in abuseipdb.com for the last 3 days

``` sh
curl -s -G https://api.abuseipdb.com/api/v2/check-block --data-urlencode "network=123.123.123.1/24" -d maxAgeInDays=$DAYS -H "Key: apikeyfromabuseipdb.com" -H "Accept: application/json" |jq '.data.reportedAddress'
```

If you want to inspect the headers of a response from some endpoint include the `-I` flag and `curl` will
return just the headers.

``` sh
curl -I localhost:3000/posts
```

Example of using curl with basic auth credentials

``` sh
curl -u username:password staging.example.com
```

Query a website e.g. request a json response from cloudflare-dns.com on TXT records of the domain 0xfab1.net

``` sh
curl -s -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=0xfab1.net&type=TXT'
```

## Send Mail

``` sh
curl --ssl-reqd --url 'smtps://smtp.gmail.com:465' --user 'username@gmail.com:password' --mail-from 'username@gmail.com' --mail-rcpt 'john@example.com' --upload-file mail.txt
```

mail.txt file contents:

``` txt
From: "User Name" <username@gmail.com>
To: "John Smith" <john@example.com>
Subject: This is a test

Hi John,
I’m sending this mail with curl thru my gmail account.
Bye!
```

Some more information:

- [gmail: turn on access for less secure apps](https://myaccount.google.com/lesssecureapps)
- Use [--netrc-file](https://everything.curl.dev/usingcurl/netrc) instead of credentials in curl command
- [Use curl with ssl](https://curl.se/docs/sslcerts.html)

## WebDAV

Create Folders

``` sh
curl -X MKCOL 'http://your.server/uploads/nested_folder1' --user 'name:pwd'
```

Copy Files

``` sh
curl -T <filename> -u <username>:<password> <url> -o /dev/stdout
```

Copy all files in a Folder (and subfolder). Folders must already exist.

``` sh
cd local_folder_to_upload && find . -exec curl -T {} 'http://your.server/uploads/{}' --user 'name:pwd' \;
```
