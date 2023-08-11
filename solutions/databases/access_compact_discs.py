import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c0nygre1",
    database="conygre"
)

query = "SELECT * FROM compact_discs"

cursor = db.cursor()
cursor.execute(query)

result = cursor.fetchall()

print("Retrieved Compact Discs:")
for cd in result:
    print(cd)

query = "UPDATE compact_discs SET title = 'New Title' WHERE id = 10"

cursor = db.cursor()
cursor.execute(query)
db.commit()

query = "DELETE FROM compact_discs WHERE id = 10"

cursor = db.cursor()
cursor.execute(query)
db.commit()

query = "INSERT INTO compact_discs (title, artist, price, tracks) VALUES ('New Disc', 'New Artist', 12.99, 10)"

cursor = db.cursor()
cursor.execute(query)
db.commit()