# curl

| What          | Where                                                                |
|---------------|----------------------------------------------------------------------|
| Official Page | <https://curl.se/>                                                   |
| Source        | <https://github.com/curl/curl>                                       |
| Download      | <https://github.com/curl/curl/releases>                              |
| Docker        | <https://hub.docker.com/r/curlimages/curl>                           |
| Docs          | <https://everything.curl.dev> or <https://curl.se/docs/manpage.html> |
| Book          | <https://curl.se/docs/>                                              |
| Windows       | `scoop install curl`                                                 |
| Ubuntu        | `sudo apt -y install curl`                                           |

## Downloading Files

Simple download

```sh
curl -O https://example.com/file.zip
```

Download with output filename

```sh
curl -o myfile.zip https://example.com/file.zip
```

Use -L to follow redirects:

```sh
curl -L https://example.com
```

## Authentication

Example of using curl with basic auth credentials

``` sh
curl -u username:password staging.example.com
```

## Send Mail

Please note: Gmail no longer supports "less secure apps." Use [App Passwords](https://support.google.com/accounts/answer/185833) instead.

``` sh
curl --ssl-reqd --url 'smtps://smtp.gmail.com:465' \
--user 'username@gmail.com:app_password' \
--mail-from 'username@gmail.com' \
--mail-rcpt 'john@example.com' \
--upload-file mail.txt
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

Use [--netrc-file](https://everything.curl.dev/usingcurl/netrc) instead of credentials in curl command for better security.

Example:

``` sh
curl --netrc-file ~/.netrc staging.example.com
```

``` txt
machine staging.example.com
login username
password password
```

## WebDAV

Create directories on WebDAV:

``` sh
curl -X MKCOL 'http://your.server/uploads/nested_folder1' --user 'name:pwd'
```

Upload a file via WebDAV:

``` sh
curl -T file.txt 'http://your.server/uploads/file.txt' --user 'username:password'
```

Upload all files in folder (directories must exist):

``` sh
cd local_folder_to_upload && find . -type f -exec curl -T {} 'http://your.server/uploads/{}' --user 'username:password' \;
```

## Random Examples

### check netowrk range

Example to check /24 range in "abuseipdb.com" for the last 3 days

``` sh
DAYS=3
curl -s -G "https://api.abuseipdb.com/api/v2/check-block" \
  --data-urlencode "network=123.123.123.1/24" \
  -d "maxAgeInDays=$DAYS" \
  -H "Key: apikeyfromabuseipdb.com" \
  -H "Accept: application/json" \
  | jq '.data.reportedAddress'
```

If you dont have jq installed:

- ubuntu: ```sudo apt install jq```
- windows: ```scoop install jq```

### Inspect headers

If you want to inspect the headers of a response from some endpoint include the `-I` flag and `curl` will return just the headers.

``` sh
curl -I localhost:3000/posts
```

or a verbose setting:

``` sh
curl -v localhost:3000/posts
```

### Request JSON

Query a website e.g. request a json response from cloudflare-dns.com on TXT records of the domain 0xfab1.net

``` sh
curl -s -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=0xfab1.net&type=TXT'
```

### Send JSON

This command sends a POST request with JSON data.

``` sh
curl -X POST https://api.example.com/posts \
-H 'Content-Type: application/json' \
-d '{"title":"Hello","body":"Curl"}'
```

### Timing

This command measures the performance of a request.

It shows:

- DNS lookup time (time_namelookup)
- TCP connection time (time_connect)
- total request duration (time_total)

The response body is ignored (-o /dev/null).

``` sh
curl -w "@-" -o /dev/null -s "https://example.com" <<'EOF'
time_namelookup: %{time_namelookup}\n
time_connect: %{time_connect}\n
time_total: %{time_total}\n
EOF
```

### Using a proxy

Route the request through a proxy server (http://proxyserver:port).
This is useful for debugging, bypassing restrictions, or accessing internal networks.

``` sh
curl -x http://proxyserver:port https://example.com
```

### More

- [Use curl with ssl](https://curl.se/docs/sslcerts.html)

Absolutely! Here’s the technical blog section in **Markdown**:

## Is curl in PowerShell an Alias or the Real Deal?

On Windows, running `curl` in PowerShell might not always do what you expect. That’s because older versions of PowerShell define `curl` as an alias for `Invoke-WebRequest`, while modern Windows also ships with the real cURL executable. To avoid confusion, here’s a simple PowerShell snippet to check exactly what `curl` points to in your session:

```powershell
$curlCmd = Get-Command curl -ErrorAction SilentlyContinue

if ($null -eq $curlCmd) {
    Write-Output "'curl' is not available in your PATH."
}
elseif ($curlCmd.CommandType -eq 'Alias') {
    Write-Output "'curl' is a PowerShell alias for '$($curlCmd.Definition)'."
}
elseif ($curlCmd.CommandType -eq 'Application') {
    Write-Output "'curl' is the real executable located at: $($curlCmd.Source)"
}
else {
    Write-Output "Unexpected command type: $($curlCmd.CommandType)"
}
```

Just run this script in your PowerShell window, and you’ll immediately know whether `curl` is an alias or the real command-line tool. If it’s an alias and you need the actual cURL, you can always remove the alias for your session with:

```powershell
Remove-Item alias:curl
```
