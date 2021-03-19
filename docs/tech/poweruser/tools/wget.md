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

```shell
wget -e robots=off -r -np --page-requisites --convert-links --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" http://example.com/dir/
```

Alternative:

```shell
wget -e robots=off --verbose --debug --adjust-extension --backup-converted --base=http://example.com/dir/ --no-http-keep-alive --no-parent --mirror http://example.com/dir/
```

## Download specific files types

```shell
wget -e robots=off -r -A ogg,mp3 http://example.com/dir/ # Specific audio files
wget -e robots=off -r -A png,jpeg,jpg,gif http://example.com/dir/ # Specific Image Files
wget -e robots=off -r -l 3 -np -p  http://example.com/dir/ # All pictures
```
