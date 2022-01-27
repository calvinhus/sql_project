import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='ironhack_db',
                                         user='root',
                                         password='calvinhus.SQL')
    print(connection.is_connected())
    mySql_insert_query = """INSERT INTO ironhack_db.comments (`index`, `name`)
                            VALUES (%s, %s); """

    records_to_insert = [(1, 'abc'), (2, 'kashj'), (3, 'as'), (4, 'asdh')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
