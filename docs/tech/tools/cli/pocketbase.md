# Pocketbase

Config File is here:

.config/code-server/config.yaml

## API

### Curl

Example Curl Commands

Auth with Token

```sh
curl -H 'Authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSasdasdasdYzNTgyMyIdasdasdsImV4cCI6MTc4NDYyNzAyMywiaWQiOiJLVDQ1YnpOQTM0MFhhN0wiLCJyZWZyZXNoYWJsZSI6ZmFsc2UsInR5cGUiOiJhdXRoIn0.3OC9656-JIB4LlscVasdasdasFC6PTqbNzaM-Y' 'https://pocketbase.io/api/collections/_superusers/records?perPage=50'
```

Auth with Username and Password

```sh
curl -X POST -H 'Content-Type:application/json' -d '{ "identity":"test@example.com", "password":"123456" }' 'https://pocketbase.io/api/collections/_superusers/auth-with-password'
```
