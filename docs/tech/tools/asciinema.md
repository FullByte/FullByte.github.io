# asciinema

Install

``` sh
sudo pip3 install asciinema
```

Record a session

``` sh
asciinema rec
echo "hello world"
exit
```

Play existing recordings (local/online):

``` sh
asciinema play /path/to/asciicast.cast
asciinema play https://asciinema.org/a/237459
```
