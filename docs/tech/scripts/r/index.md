---
date: 2023-12-22
modified: 2023-12-22
description: 'Console: start R inside a container with:'
tags:
- Tech
- Scripting
---

# R

## Docker

Console: start R inside a container with:

``` sh
docker run --rm -ti r-base
```

Run a browser based RStudio instance:

``` sh
docker run --rm -ti -e PASSWORD=yourpassword -p 8787:8787 rocker/rstudio
```
