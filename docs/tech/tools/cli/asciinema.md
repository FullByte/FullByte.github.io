# asciinema

| What    | Where                                     |
|---------|-------------------------------------------|
| Docs    | <https://asciinema.org/docs/how-it-works> |
| Install | `sudo pip3 install asciinema`             |

## Examples

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
