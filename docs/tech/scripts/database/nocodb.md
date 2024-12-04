# NOCODB

Add an API token in NOCODB: From the User (bottom left) click on "Account Settings" and navigate to "Audit Log". The URL Path should look like this: .../dashboard/#/account/tokens.

Once done, it is possible to add data to a given Datenbase using one-liners in the commandline. For this to work the view mode must be collaborative. For some examples go to a table and view Details and then API Snippets. Here are some of mine:

LINUX with CURL

```sh
curl --request POST --url 'https://data.0xfab1.net/api/v2/tables/yourtable/records?offset=0&limit=25&where=&viewId=abcdefg' --header 'xc-token: yourtoken' --header 'Content-Type: application/json' --data '{"Column1":"value1", "Column2":"value2"}' | jq '.'
```

WINDOWS with CURL

```ps1
curl --request POST --url "https://data.0xfab1.net/api/v2/tables/yourtable/records?offset=0&limit=25&where=&viewId=abcdefg" --header "xc-token: yourtoken" --header "Content-Type: application/json" --data "{\"Column1\":\"value1\", \"Column2\":\"value2\"}"
```

WINDOWS with POWERSHELL using Invoke-RestMethod

```ps1
Invoke-RestMethod -Uri "https://data.0xfab1.net/api/v2/tables/yourtable/records?offset=0&limit=25&where=&viewId=abcdefg" -Method POST -Headers @{"xc-token" = "yourtoken"; "Content-Type" = "application/json"} -Body '{"Column1":"value1","Column2":"value2"}'
```

WINDOWS with CMD with triggering POWERSHELL

```ps1
powershell -Command "Invoke-RestMethod -Uri 'https://data.0xfab1.net/api/v2/tables/yourtable/records?offset=0&limit=25&where=&viewId=abcdefg' -Method POST -Headers @{ 'xc-token' = 'yourtoken'; 'Content-Type' = 'application/json' } -Body '{\"Column1\":\"value1\",\"Column2\":\"value2\"}'"
```
