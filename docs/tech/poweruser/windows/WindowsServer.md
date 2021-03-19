# Windows Server

## KMS

To set a KMS Server into Windows Managed Server’s configuration you need to execute the following command:

```powershell
slmgr /skms <KMS-FQDN>:1688
```

To trigger Windows activation you need to execute the following command:

```powershell
slmgr /ato
```

## IIS

**IIS Passwords**

```powershell
foreach ($site in Get-ChildItem IIS:\Sites) { "Site: " + $site.name + " - " + "User: " + $site.userName + "PW: " + $site.password }
```
