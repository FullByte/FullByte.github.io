---
date: 2023-12-22
modified: 2023-12-22
description: 'Remove each source file after creating a successful copy (Basically "Move"):'
tags:
- Tech
- Tools
---

# rsync

| What          | Where                                        |
|---------------|----------------------------------------------|
| Official Page | <https://rsync.samba.org/>                   |
| Documentation | <https://rsync.samba.org/documentation.html> |

Remove each source file after creating a successful copy (Basically "Move"):

``` sh
rsync --remove-source-files /path/to/source/folder /path/to/destination/folder
```
