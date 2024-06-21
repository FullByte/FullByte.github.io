# Fabric

| What          | Where                                  |
| ------------- | -------------------------------------- |
| Source        | <https://github.com/danielmiessler/fabric> |

## Examples

Pass text to fabric

``` sh
echo "Give me a list Of alt ice cream flavors" | fabric -sp ai
```

Pass video subtitles to fabric

``` sh
yt --transcript https://www.youtube.com/watch?v=UbDyjIIGaxQ | fabric -sp extract_wisdom
```

Pass web content to fabric:

``` sh
w3m -dump https://huggingface.co/blog/mlabonne/abliteration | fabric -sp extract_wisdom
```
