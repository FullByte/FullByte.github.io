# Sendgrid

<https://sendgrid.com/>

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
