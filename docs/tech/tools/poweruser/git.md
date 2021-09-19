# Git

## Tools

- git quick stats: <https://github.com/arzzen/git-quick-stats>

## Setup

Set global user name and email:
(remove --global flag for specific repo only)

```bash
git config --global user.name "0xfab1"
git config --global user.email "f@bi.an"
```

## Commands

Get all authors:

```ps1
git log | Where { $_ -match "Author" } | Select-Object -unique
```
