---
date: 2024-06-21
modified: 2024-06-21
description: Pass text to fabric
tags:
- Tech
- Tools
---

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
