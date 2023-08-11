from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c0nygre1",
    database="conygre"
)

# Endpoint to get all compact discs
@app.route('/compact_discs', methods=['GET'])
def get_compact_discs():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM compact_discs")
    compact_discs = cursor.fetchall()
    cursor.close()
    return jsonify(compact_discs)

# Endpoint to get a specific compact disc by ID
@app.route('/compact_discs/<int:cd_id>', methods=['GET'])
def get_compact_disc(cd_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM compact_discs WHERE id = %s", (cd_id,))
    compact_disc = cursor.fetchone()
    cursor.close()
    if compact_disc:
        return jsonify(compact_disc)
    else:
        return jsonify({'error': 'Compact disc not found'}), 404

# Endpoint to create a new compact disc
@app.route('/compact_discs', methods=['POST'])
def create_compact_disc():
    title = request.json['title']
    artist = request.json['artist']
    track_count = request.json['track_count']
    price = request.json['price']

    cursor = db.cursor()
    cursor.execute("INSERT INTO compact_discs (title, artist, track_count, price) VALUES (%s, %s, %s, %s)",
                   (title, artist, track_count, price))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Compact disc created successfully'})

# Endpoint to update an existing compact disc
@app.route('/compact_discs/<int:cd_id>', methods=['PUT'])
def update_compact_disc(cd_id):
    title = request.json['title']
    artist = request.json['artist']
    track_count = request.json['track_count']
    price = request.json['price']

    cursor = db.cursor()
    cursor.execute("UPDATE compact_discs SET title = %s, artist = %s, track_count = %s, price = %s WHERE id = %s",
                   (title, artist, track_count, price, cd_id))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Compact disc updated successfully'})

# Endpoint to delete a compact disc
@app.route('/compact_discs/<int:cd_id>', methods=['DELETE'])
def delete_compact_disc(cd_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM compact_discs WHERE id = %s", (cd_id,))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Compact disc deleted successfully'})

if __name__ == '__main__':
    app.run()
