# Curl

Example to check /24 range in abuseipdb.com for the last 3 days

```bash
curl -s -G https://api.abuseipdb.com/api/v2/check-block --data-urlencode "network=123.123.123.1/24" -d maxAgeInDays=$DAYS -H "Key: apikeyfromabuseipdb.com" -H "Accept: application/json" |jq '.data.reportedAddress'
```

If you want to inspect the headers of a response from some endpoint include the `-I` flag and `curl` will
return just the headers.

```bash
curl -I localhost:3000/posts
```

Example of using curl with basic auth credentials

```bash
curl -u username:password staging.example.com
```

