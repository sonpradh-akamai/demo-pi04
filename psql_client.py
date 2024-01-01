import psycopg2
from psycopg2 import pool
import json

host = "c-testcosmospsqldb.upwmcf5c7b2veu.postgres.cosmos.azure.com"
dbname = "citus"
user = "citus"
password = "Azure123"
sslmode = "require"
try:
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,conn_string)
    if (postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to get a connection from the connection pool
    conn = postgreSQL_pool.getconn()
    cursor = conn.cursor()
except Exception as err:
    #return "error :" + str(serr)
    print("error: " + err)

#CREATE TABLE
# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS testtable")
cursor.execute("CREATE TABLE testtable (id SERIAL,day VARCHAR, info JSONB);")
print("Finished creating table")
conn.commit()

# WRITE DATA
# try:
#     data_to_insert = [
#         ("day1", {"key": "key1","value":{"nes_key":"nes_value1"}}),
#         ("day2", {"key": "key2","value":{"nes_key":"nes_value2"}}),
#         ("day3", {"key": "key3","value":{"nes_key":"nes_value3"}})
#     ]
#     # data_to_insert = [
#     #     ("day4", {"key": "key4","value":{"nes_key":["nes_value4.1", "nes_value4.2"]}})
#     # ]
#     insert_query = "INSERT INTO testtable (day, info) VALUES (%s, %s)"    
#     for item in data_to_insert:
#         day, info = item
#         cursor.execute(insert_query, (day, json.dumps(info)))

#     #insert_query = """INSERT INTO testtable (day, info) VALUES ('Monday', '{"key": "value1"}');"""   
#     #cursor.execute(insert_query)
#     conn.commit()
#     print("done")
# except Exception as err:
#     print("error: ")
#     print(err)

i = 0
while i<10: 
    try:
        # select_query = """SELECT 
        # info -> 'key'
        # FROM
        # testtable;"""
        select_query = """SELECT * FROM testtable"""

        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            #print((row[2]))
            # id_, day, info = row
            # #info_dict = json.loads(info)
            # print(f"ID: {id_}, Day: {day}, Info: {info}")
    except Exception as err:
        print("error: ")
        print(err)
    i+=1

# Clean up
conn.commit()
cursor.close()
conn.close()
print("done")