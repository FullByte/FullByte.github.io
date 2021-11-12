# asciinema

Install

```shell
sudo apt-get install python3 pip
sudo pip3 install asciinema
```

Record a session

```shell
asciinema rec
echo "hello world"
exit
```

Play existing recordings (local/online):

```shell
asciinema play /path/to/asciicast.cast
asciinema play https://asciinema.org/a/237459
```
