# Wget

## Download all files from website

Generally, this can be blocked but works in most cases. To avoid a few things:

- Ignore **robots.txt** blocking the download by using ```-e robots=off```
- Add **user-agent**; either one that guarantees a math e.g. ```--user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"``` or just the one you are using atm e.g. ```Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0``` (Firefox: about:config --> devtools.responsive.userAgent)
- **Random service blocks**: Try removing some options as they may the reason access is blocked e.g. ```-N``` blocked by AWS S3.
- Adding a **referrer** may help. Figure out what you need by checking why it works in the browser e.g. ```wget --referer='http://example.net' http://example.com/```
- Checking the details of the **HTTP status code** you get as an error may help resolve the issue too: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>
- A required **cookie** or missing **authorization** can be further reasons why the download doesn't work or run though fully.

Example:

```sh
wget -e robots=off -r -np --page-requisites --convert-links --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" http://example.com/dir/
```

Alternative:

```sh
wget -e robots=off --verbose --debug --adjust-extension --backup-converted --base=http://example.com/dir/ --no-http-keep-alive --no-parent --mirror http://example.com/dir/
```

## Download specific files types

```sh
wget -e robots=off -r -A ogg,mp3 http://example.com/dir/ # Specific audio files
wget -e robots=off -r -A png,jpeg,jpg,gif http://example.com/dir/ # Specific Image Files
wget -e robots=off -r -l 3 -np -p  http://example.com/dir/ # All pictures
```

## Download features

In case you are downloading clear text files it may come in handy to preview the download:

```sh
wget http://0xfab1.net/todo.txt --output-document - | head -n4
```

Continue a partially downloaded file where the download was interrupted with `-c` for continue:

```sh
wget -c https://0xfab1.net/best-distro2.iso
```

You can copy an entire web page with `--mirror` which is the same as adding parameters `--recursive --level inf --timestamping --no-remove-listing`. When using mirror consider using `--no-cookies --page-requisites --convert-links` as additional parameters:

```sh
wget --mirror --no-cookies --page-requisites --convert-links http://0xfab1.net
```

Use `--debug` to view HTTP header information of your download request.

```sh
wget --debug https://0xfab1.net
```

If you want to deal with redirects as error set `--max-redirect 0`. This is also handy if you don't want to follow URL-shorter links:

```sh
wget --max-redirect 0 "https://bit.ly/0xfab1"
```
