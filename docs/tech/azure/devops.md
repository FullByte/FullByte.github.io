# DevOps

## Artifacts

Upload and Download files example

``` ps11
$devopsorg = "yourorg"
$devopsproject = "project"
$feedname = "feed-name"
$packagename = "package-name"

az artifacts universal publish --organization "https://dev.azure.com/$devopsorg" --project="$devopsproject" --scope project --feed "$feedname" --name "$packagename" --version 0.0.1 --description "Test" --path .

az artifacts universal download --organization "https://dev.azure.com/$devopsorg" --project "$devopsproject" --scope project --feed "$feedname" --name "$packagename" --version "0.0.1" --path .
```

## Wiki

This script **deletes unwanted internal wiki** in DevOps that cant be deleted via GUI.

Requires Azure CLI and Powershell and the DevOps PAT requires right to delete wiki repo.

``` ps11
Param(
    [Parameter(Mandatory=$true,
    HelpMessage="DevOps Organization Name aka the name in the URL when you open DevOps.")]
    [String]
    $OrganizationName,

    [Parameter(Mandatory=$true,
    HelpMessage="DevOps Project Name within the given DevOps Organization. This should be the project of which you want to delete the internal wiki.")]
    [String]
    $ProjectName,
    
    [Parameter(Mandatory=$true,
    HelpMessage="DevOps PAT Token requires right to delete wiki repo. Example: 7dth7i7e4Apzy4aasd...")]
    [String]
    $AzureDevOpsPAT
)

Begin {
    # get authentication header for REST
    $AzureDevOpsAuthenicationHeader = @{Authorization = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$($AzureDevOpsPAT)")) }
}

Process {
    # Info
    Write-Host("Attempting to delete project Wiki for Project: $ProjectName in DevOps Organization $OrganizationName.") -ForegroundColor Green -BackgroundColor DarkGray

    # get project ID based on project name
    $ProjectID = (az devops project list --query "value[].{name:name, id:id}[?name=='$ProjectName']" -o tsv) | ForEach-Object { $_.Split("`t")[1] }
    
    # show wiki repo info
    (Invoke-RestMethod -Uri "https://dev.azure.com/$($OrganizationName)/$($ProjectID)/_apis/wiki/wikis?api-version=6.0" -Method get -Headers $AzureDevOpsAuthenicationHeader).value
    
    # get repositoryId
    $RepositoryId = (Invoke-RestMethod -Uri "https://dev.azure.com/$($OrganizationName)/$($ProjectID)/_apis/wiki/wikis?api-version=6.0" -Method get -Headers $AzureDevOpsAuthenicationHeader).value | Where-Object type -eq 'projectWiki' | Select-Object -ExpandProperty repositoryId

    # Check if wiki exists and delete it
    if (-not ([string]::IsNullOrEmpty($RepositoryId)))
    {
        Write-Host("Deleting RepositoryId: $RepositoryId") -ForegroundColor Green -BackgroundColor DarkGray
        $DeleteConfirmation = $(Write-Host "Press 'y' to proceed or 'n' to abort." -ForegroundColor Green -BackgroundColor DarkGray -NoNewLine; Read-Host) 

        if ($DeleteConfirmation -eq 'y'){
            # delete internal wiki repo
            Invoke-RestMethod -Uri "https://dev.azure.com/$($OrganizationName)/$($ProjectID)/_apis/git/repositories/$($RepositoryId)?api-version=6.0" -Method delete -Headers $AzureDevOpsAuthenicationHeader
            Write-Host("Repository successfully deleted.") -ForegroundColor Green -BackgroundColor DarkGray
        }
        else {
            Write-Host("Abort successfull.") -ForegroundColor Green -BackgroundColor DarkGray
        }
    }
    else {
        Write-Host("Could not find project Wiki for Project: $ProjectName") -ForegroundColor red -BackgroundColor White
    }
}
```
