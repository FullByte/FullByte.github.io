# Sendgrid

<https://sendgrid.com/>

## powershell

```powershell
$From = "email@address"
$To = "email@address"
$Cc = ""
$Bcc = ""
$APIKEY = "MY_API_KEY"
$Subject = "TEST"
$Body ="SENDGRID 123"

$headers = @{}
$headers.Add("Authorization","Bearer $apiKey")
$headers.Add("Content-Type", "application/json")

$jsonRequest = [ordered]@{
	personalizations= @(@{ to = @(@{email = "$To"}) subject = "$SubJect" })
	from = @{email = "$From"}
	content = @( @{ type = "text/plain"
	value = "$Body" })
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri "https://api.sendgrid.com/v3/mail/send" -Method Post -Headers $headers -Body $jsonRequest 
```

## curl

```sh
export SENDGRID_API_KEY='something'

curl --request POST --url https://api.sendgrid.com/v3/mail/send --header "Authorization: Bearer $SENDGRID_API_KEY" --header 'Content-Type: application/json' --data '{"personalizations": [{"to": [{"email": "mail@to.you"}]}],"from": {"email": "bot@0xfab1.net"},"subject": "Hello world","content": [{"type": "text/plain", "value": "Nice, mailing with cURL :D"}]}'
```
