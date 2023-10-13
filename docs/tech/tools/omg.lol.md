# OMG.lol

| What          | Where |
|---------------|-------|
| Official Page |       |

## Add Note

curl --location --request POST --header 'Authorization: Bearer yourtoken' 'https://api.omg.lol/address/yolo/pastebin/' --data '{"title": "new-paste", "content": "This is a new paste."}'

## Add Post

curl --location --request POST --header 'Authorization: Bearer yourtoken' 'https://api.omg.lol/address/yolo/statuses/' --data '{"emoji": "ðŸ‘¨ðŸ»â€ðŸ’»", "content": "Testing!"}'

## Read Pastebin

curl --location --request GET --header 'Authorization: Bearer yourtoken' 'https://api.omg.lol/address/yolo/pastebin'

curl --location --request GET 'https://api.omg.lol/address/yolo/pastebin'

## Create Pastebin entry

curl --location --request POST --header 'Authorization: Bearer yourtoken' 'https://api.omg.lol/address/adam/pastebin/' --data '{"title": "new-paste", "content": "This is a new paste."}'
