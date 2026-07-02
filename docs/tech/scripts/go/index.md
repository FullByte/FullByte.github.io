---
date: 2023-12-22
modified: 2024-06-12
description: 'If there is no go.mod file create one:'
tags:
- Tech
- Scripting
---

# Go

## Dependencies

If there is no go.mod file create one:

``` go
go mod init project
```

now run the following command to install all dependencies

``` go
go mod tidy
```

The program should now run:

``` go
go run main.go
```
