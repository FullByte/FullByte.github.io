# SQL Basics

## JOINs

Inner Join --> Es wird angezeigt, was auf beiden Seiten existiert
Left Join --> Auch wenn rechts keine Werte zu links stehen wird links angezeigt.
Right Join --> Auch wenn links keine Werte zu rechts stehen wird links angezeigt.

## CASE Anweisung

This example translates ```[Table].[statusID]``` into a given text value.

```SQL
SELECT [Table] =
CASE [Table].[statusID]
    WHEN 0 THEN 'Created'
    WHEN 200 THEN 'Running'
    WHEN 300 THEN 'HALTED'
    WHEN 400 THEN 'Canceled'
    WHEN 500 THEN 'Finished'
    ELSE '-undefined-'
END
FROM [dbo].[BusinessProcessInstances]
```

## COALESCE

```SQL
COALESCE((SELECT [...] option1), (SELECT [...] option2), (SELECT [...] option3))
```

## Recieve XML as query result

```SQL
FOR XML AUTO, TYPE, XMLSCHEMA, ELEMENTS XSINIL
```

## Enter Ids manually (bad!)

```SQL
SET IDENTITY_INSERT [dbo].[Table] ON
\-- DO STUFF
SET IDENTITY_INSERT [dbo].[Table] OFF
```

## Builtin functions

```SQL
SELECT HOST_NAME() -- GET Local System Name
SELECT GETUTCDATE() -- GET Local Time (UTC - Zone)
SELECT SUSER_NAME() -- GET SuperUser Name of DB
```

## Get Current User

```SQL
\--Functions returning login
SELECT original_login() -- original login name not impersonated one
UNION
SELECT suser_name()
UNION
SELECT suser_sname()
UNION
SELECT system_user
```

```SQL
\--Functions returning database user
SELECT session_user
UNION
SELECT current_user
UNION
SELECT user_name()
UNION
SELECT user
```

## Cursor

```SQL
DECLARE @ServerID int

DECLARE AllServers CURSOR FORWARD_ONLY FOR
		SELECT [Servers].ServerID FROM [dbo].[Servers] WHERE ProjectID = 1
OPEN AllServers
FETCH NEXT FROM AllServers INTO @ServerID

    WHILE @@FETCH_STATUS = 0
    BEGIN
    	PRINT 'Server: ' + CONVERT(nvarchar(50),@ServerID)
    	FETCH NEXT FROM AllServers INTO @ServerID  
    END

CLOSE AllServers
DEALLOCATE AllServers
```

## Check if file exists

```SQL
USE master

DECLARE @FileName nvarchar(250) SET @FileName = 'C:\\TEMP\\test.ps1'
DECLARE @FileExists int

EXEC xp_FileExist @FileName, @FileExists out

IF @FileExists =1
    BEGIN
        PRINT 'File exists'
    END
ELSE
    BEGIN
        PRINT 'No File'
    END
```
