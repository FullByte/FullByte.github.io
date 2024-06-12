# SQLite

## Creating Excel report

```SQL
import pandas as pd
import sqlite3

# Get data from SQLite db
con = sqlite3.connect("your.db")
sql = "select * from yourtable; "
df = pd.read_sql_query(sql, con)
con.close()

# write to Excel
df.to_excel ("report.xlsx", index=False, header=True)
```
