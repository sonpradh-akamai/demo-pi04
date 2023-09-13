import pyodbc

server = 'tcp:db-billing-sql-server.database.windows.net'
database = 'demo-sql-db'
username = 'azureuser'
password = 'Azur3us3r123'
driver = '{ODBC Driver 18 for SQL Server}'

def create_table(cursor):
    create_table_query = '''
    CREATE TABLE sometable(
                [Key] NVARCHAR(50),
                    [Value] INT
                    )
    '''

    cursor.execute(create_table_query)
    cursor.commit()

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = conn.cursor()
#create_table(cursor)

insert_query = '''
INSERT INTO sometable ([Key], [Value])
VALUES (?, ?)
'''

data = [('A', 10), ('B', 20), ('C', 30)]

cursor.executemany(insert_query, data)
cursor.commit() 

cursor.execute("SELECT TOP(1000) * FROM sometable")

for row in cursor:
        print(row)


cursor.close()
conn.close() 