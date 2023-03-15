# File Recovery

Store: <https://www.microsoft.com/en-us/p/windows-file-recovery/9n26s50ln705?activetab=pivot:overviewtab>

Recover a specific file from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Documents\QuarterlyStatement.docx
```

Recover jpeg and png photos from your Pictures folder to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Pictures\*.JPEG /n \Users\<username>\Pictures\*.PNG
```

Recover your Documents folder from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /n \Users\<username>\Documents\ 
```

Recover PDF and Word files from your C: drive to the recovery folder on an E: drive.

``` ps1
winfr C: E: /r /n *.pdf /n *.docx
```

Recover any file with the string "invoice" in the filename by using wildcard characters.

``` ps1
winfr C: E: /r /n *invoice* 
```
