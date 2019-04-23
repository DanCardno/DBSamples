  1 import pyodbc
  2 cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=Galaxy3D4d')
  3 cursor = cnxn.cursor()
  4
  5 print ("select")
  6 cursor.execute("select @@version;")
  7 for row in cursor:
  8     print(f'row = {row}')
