---
date: 2023-12-22
modified: 2024-05-29
description: Disable registration, after which only admin can create accounts for users.
tags:
- Tech
- Tools
---

# Gitea

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Setup

Disable registration, after which only admin can create accounts for users.

modify `app.ini`

```ini
[service]
DISABLE_REGISTRATION = true
```
