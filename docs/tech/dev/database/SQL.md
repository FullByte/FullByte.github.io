# MS SQL

## JOINs

Inner Join → Es wird angezeigt, was auf beiden Seiten existiert
Left Join → Auch wenn rechts keine Werte zu links stehen wird links angezeigt.
Right Join → Auch wenn links keine Werte zu rechts stehen wird links angezeigt.

## CASE Anweisung

This example translates```[table1].[statusID]``` into a given text value.

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
FROM [dbo].[table1]
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
