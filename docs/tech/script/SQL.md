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


# Check If Table And Column Exist

Query

```SQL
DECLARE @table nvarchar(max)
DECLARE @column nvarchar(max)

SET @table = 'Categories'
SET @column = 'CategoryID'

IF ((SELECT COALESCE(COL_LENGTH(@table,@column),0)) = 0)
BEGIN
	PRINT 'Table and/or column does not exist'
END
ELSE
BEGIN
	PRINT 'Table and column exist'
END
```

Function

```SQL
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[IsTableAndColumn]
(
	-- Add the parameters for the function here
	@table nvarchar(max),
	@column nvarchar(max)
)
RETURNS bit
AS
BEGIN
	IF ((SELECT COALESCE(COL_LENGTH(@table,@column),0)) = 0)
	BEGIN
		RETURN 1
	END
	ELSE
	BEGIN
		RETURN 0
	END
END
```


## Delete all DB infos

```SQL
DECLARE @name VARCHAR(255)
DECLARE @type VARCHAR(10)
DECLARE @prefix VARCHAR(255)
DECLARE @sql VARCHAR(255)

DECLARE curs CURSOR FOR
    SELECT [name], xtype  
    FROM sysobjects  
    WHERE xtype IN ('U', 'P', 'FN', 'IF', 'TF', 'V', 'TR') 
    ORDER BY name

OPEN curs
FETCH NEXT FROM curs INTO @name, @type

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @prefix = CASE @type  
        WHEN 'U' THEN 'DROP TABLE'
        WHEN 'P' THEN 'DROP PROCEDURE'
        WHEN 'FN' THEN 'DROP FUNCTION'
        WHEN 'IF' THEN 'DROP FUNCTION'
        WHEN 'TF' THEN 'DROP FUNCTION'
        WHEN 'V' THEN 'DROP VIEW'
        WHEN 'TR' THEN 'DROP TRIGGER'
    END

    SET @sql = @prefix + ' ' + @name
    PRINT @sql
    EXEC(@sql)
    FETCH NEXT FROM curs INTO @name, @type
END

CLOSE curs
DEALLOCATE curs
```

## Array Procedure

```SQL
BEGIN TRY
BEGIN TRANSACTION

  DECLARE @tmp TABLE (id int)

  DECLARE @id NVARCHAR(36)
  DECLARE @pos INT
  DECLARE @list NVARCHAR(MAX)
  SET @list ='1,123,12,312,3,2,34,23,23,4,234,23,42,34,23,4,23,4'

  SET @list = LTRIM(RTRIM(@list))+ ','
  SET @Pos = CHARINDEX(',', @list, 1)

  IF REPLACE(@list, ',', '') <> ''
  BEGIN
    WHILE (@pos > 0)
    BEGIN
      SET @id = LTRIM(RTRIM(LEFT(@list, @pos - 1)))
      IF (@id <> '')
      BEGIN
        INSERT INTO @tmp (id)
        VALUES (@id)
      END
      SET @list = RIGHT(@list, LEN(@list) - @pos)
      SET @pos = CHARINDEX(',', @list, 1)
    END
  END

  SELECT * FROM @tmp


    COMMIT TRANSACTION
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION
END CATCH
```

## Check DB Cluster Mirror State

```SQL
USE [master]
 
DECLARE @DBName nvarchar(max) SET @DBName = 'dbname'
DECLARE @MirrorState nvarchar(max)
 
SET @MirrorState= (SELECT TOP 1 [M].[mirroring_role_desc] FROM sys.database_mirroring [M]
INNER JOIN sys.databases [DB] ON [M].[database_id] = [DB].[database_id]
WHERE [M].[mirroring_role_desc] IS NOT NULL AND [DB].[name] = @DBName)
 
IF (@MirrorState = 'PRINCIPAL')
BEGIN
        PRINT 'Principal'
END
ELSE IF (@MirrorState = 'MIRROR')
BEGIN
        PRINT 'Mirror'
END
ELSE
BEGIN
        PRINT 'Not a mirrored DB or DB not found.'
END
```

## Delete DB

```SQL
DECLARE @DBtoKill nvarchar(128) SET @DBtoKill = 'dbname'
 
USE [master]
 
-- Kill all process running on DB to Kill
DECLARE @CMD varchar(50)
DECLARE @SPIDtoKill INT
DECLARE @ProcessTable TABLE([SPID] INT, [Status] VARCHAR(MAX), [LOGIN] VARCHAR(MAX), [HostName] VARCHAR(MAX),
        [BlkBy] VARCHAR(MAX), [DBName] VARCHAR(MAX), [Command] VARCHAR(MAX), [CPUTime] INT,
        [DiskIO] INT, [LastBatch] VARCHAR(MAX), [ProgramName] VARCHAR(MAX), [SPID_1] INT,
        [REQUESTID] INT)
 
INSERT INTO @ProcessTable EXEC sp_who2
 
DECLARE ProjectsToKill CURSOR FORWARD_ONLY FOR         
SELECT SPID AS [SPIDtoKill] FROM @ProcessTable WHERE [DBName] = @DBtoKill
OPEN ProjectsToKill 
        FETCH NEXT FROM ProjectsToKill INTO @SPIDtoKill
        WHILE @@FETCH_STATUS = 0
        BEGIN   
                SELECT @CMD = 'KILL ' + CAST(@SPIDtoKill AS varchar(5))
                EXEC (@CMD)
               
                FETCH NEXT FROM ProjectsToKill INTO @SPIDtoKill
        END
CLOSE ProjectsToKill
DEALLOCATE ProjectsToKill
 
-- Drop Table
EXEC('ALTER DATABASE ' + @DBtoKill + ' SET SINGLE_USER WITH ROLLBACK IMMEDIATE')
EXEC('ALTER DATABASE ' + @DBtoKill + ' SET OFFLINE')
EXEC msdb.dbo.sp_delete_database_backuphistory @database_name = @DBtoKill
EXEC('DROP DATABASE ' + @DBtoKill)
 
-- DELETE file if still there
EXEC sp_configure 'show advanced options', 1
EXEC sp_configure 'xp_cmdshell', 1
GO
reconfigure
GO
 
DECLARE @DeleteCommand nvarchar(250)
DECLARE @FileName nvarchar(250)
 
SET @FileName = (SELECT filename From master..sysdatabases WHERE Name = 'DBname')
SET @DeleteCommand = 'del ' + @FileName EXEC xp_cmdshell @DeleteCommand
 
SET @DBtoKill = 'DBname' + '_log'
SET @FileName = (SELECT filename From master..sysdatabases WHERE Name = 'DBname')
SET @DeleteCommand = 'del ' + @FileName EXEC xp_cmdshell @DeleteCommand
 
GO
```

## Distance between two locations

```SQL
CREATE FUNCTION dbo.Distance 
( 
    @zip1 CHAR(5), 
    @zip2 CHAR(5) 
) 
RETURNS DECIMAL(12,3) 
AS 
BEGIN 
    DECLARE 
        @lat1 DECIMAL(10,6), 
        @lon1 DECIMAL(10,6), 
        @lat2 DECIMAL(10,6), 
        @lon2 DECIMAL(10,6), 
        @rads DECIMAL(10,8), 
        @dist DECIMAL(12,3), 
        @calc DECIMAL(10,8) 
 
    SELECT 
        @rads = 57.29577951, 
        @lat1 = lat, 
        @lon1 = long 
        FROM Zips 
        WHERE Zip = @zip1 
 
    SELECT  
        @lat2 = lat, 
        @lon2 = long 
        FROM Zips 
        WHERE Zip = @zip2 
 
    SELECT 
        @lat1 = @lat1 / @rads, 
        @lon1 = @lon1 / @rads, 
        @lat2 = @lat2 / @rads, 
        @lon2 = @lon2 / @rads 
 
    IF @lat1 = @lat2 AND @lon1 = @lon2 
        SET @dist = 0.00 
    ELSE 
    BEGIN 
        SET @calc = SIN(@lat1) * SIN(@lat2) + COS(@lat1) 
            * COS(@lat2) * COS(@lon1 - @lon2) 
        IF (@calc) > 1.0 
            SET @calc = 1.0 
        SET @dist = 3963.1 * ACOS(@calc) 
    END 
 
    RETURN (@dist) 
END 
GO
```

## Return part of a string

```SQL
BEGIN TRY
BEGIN TRANSACTION

  DECLARE @TextString nvarchar(max) SET @TextString = 'This is a test example'
  DECLARE @SearchString nvarchar(250) SET @SearchString = 'test'
  DECLARE @Answer nvarchar(max) SET @Answer =
		(SELECT SUBSTRING(@TextString, CONVERT(int,
			(SELECT CHARINDEX(@SearchString, @TextString))),CONVERT(int,(
				SELECT LEN(@TextString)))-CONVERT(int,(
					SELECT CHARINDEX(@SearchString, @TextString)))+1))
 
  PRINT @Answer
  COMMIT TRANSACTION 
END TRY
BEGIN CATCH
        ROLLBACK TRANSACTION
END CATCH 
```

## Split Function

```SQL
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE FUNCTION [dbo].[ufnSplit] (@sep char(1), @s nvarchar(128))
RETURNS table
AS
RETURN (
    WITH Pieces(pn, start, stop) AS (
      SELECT 1, 1, CHARINDEX(@sep, @s)
      UNION ALL
      SELECT pn + 1, stop + 1, CHARINDEX(@sep, @s, stop + 1)
      FROM Pieces
      WHERE stop > 0
    )
    SELECT pn,
      SUBSTRING(@s, start, CASE WHEN stop > 0 THEN stop-start ELSE 128 END) AS s
    FROM Pieces
  )
GO
```

## Tic Tac Toe

```SQL
with recursive rnd_move(move) as (
        select *, random() rnd from generate_series(1, 9) move
), winning_positions(a, b, c) as (
    values (1, 2, 3), (4, 5, 6), (7, 8, 9), -- rows
           (1, 4, 7), (2, 5, 8), (3, 6, 9), -- cols
           (1, 5, 9), (3, 5, 7)             -- diagonals
), game as (
    select 'O' as who_next, ARRAY['.', '.', '.', '.', '.', '.', '.', '.', '.'] as board
    union 
    (
        select case when who_next = 'X' then 'O' else 'X' end as who_next,
               board[:move-1] || who_next || board[move+1:]
        from game, rnd_move where board[move] = '.' order by rnd limit 1
    )
), game_with_winner as (
    select *, lag(a is not null) over () as finished, lag(who_next) over () as who
    from game left join winning_positions on
        board[a] != '.' and board[a] = board[b] and board[a] = board[c]
)
select array_to_string(board[1:3] || chr(10) || board[4:6] || chr(10) || board[7:9] || chr(10), '') board,
       case when a is not null then who || ' wins' end as winner
from game_with_winner where not finished;
```