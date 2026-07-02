---
date: 2023-12-22
modified: 2023-12-22
description: 'Simple curl test to check if the API key and connection works:'
tags:
- Tech
- Tools
---

# OpenAI

Simple curl test to check if the API key and connection works:

```sh
curl https://api.openai.com/v1/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer sk-key-here" \
-d '{"model": "text-davinci-003", "prompt": "Hi AI", "temperature": 0, "max_tokens": 7}'
```
