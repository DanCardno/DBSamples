## DB Sample

1) install python
1)  install [ODBC Driver](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017 "link title")
2) pip install pyodbc



```python

  1 import pyodbc
  2 cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=passwod')
  3 cursor = cnxn.cursor()
  4
  5 print ("select")
  6 cursor.execute("select @@version;")
  7 for row in cursor:
  8     print(f'row = {row}')
```
