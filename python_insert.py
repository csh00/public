import logging
import psycopg2 

logging.basicConfig(filename='app.log', 
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Records inserted')

try:
    conn = psycopg2.connect(
            host='host',
            port= '5432',
            database="***",
            user='user',
            password='pass')
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.

sql=('''INSERT INTO test_tab (test)
        (select 1 as test) 
        ON conflict (test) do nothing''')
try:
    cursor.execute(sql)
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

# Commit your changes in the database
conn.commit()
print("done")

# Closing the connection
conn.close() 