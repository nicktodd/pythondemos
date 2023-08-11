import mysql.connector

from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="c0nygre1",
    ) as connection:
        print(connection)
        with connection.cursor() as cursor:
            cursor.execute("use conygre")
            # Execute a simple query
            cursor.execute("select * from compact_discs")
            result = cursor.fetchall()
            for row in result:
                print(row[1] + " " + row[2])

            # Execute a stored procedure
            result = cursor.callproc("find_artist", ["Echo Park", "Feeder"])
            print(result)
except Error as e:
    print(e)

