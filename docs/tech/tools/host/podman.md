---
date: 2023-12-22
modified: 2025-09-05
description: .---. / \ | / o o \.----.
tags:
- Tech
- Tools
---

# Podman

| What        | Where                                  |
|-------------|----------------------------------------|
| Source      | <https://github.com/containers/podman> |
| Website     | <https://podman.io>                    |
| Documents   | <https://docs.podman.io>               |
| Desktop GUI | <https://podman-desktop.io/>           |

``` txt
         .--"--.
       / -     - \
      / (O)   (O) \
   ~~~| -=(,Y,)=- |
    .---. /`  \   |~~
 ~/  o  o \~~~~.----. ~~
  | =(X)= |~  / (O (O) \
   ~~~~~~~  ~| =(Y_)=-  |
  ~~~~    ~~~|   U      |~~
```

## Examples

Run the hello world example:

``` sh
podman run quay.io/podman/hello
```

Pull, then run 0xfab1.net

``` sh
podman pull docker.io/0xfab1/0xfab1.net
podman run 0xfab1.net
```
