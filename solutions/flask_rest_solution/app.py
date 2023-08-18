from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

# Create the application instance and set the static folder so i don't have to put the path to the static folder in the URL
app = Flask(__name__, static_url_path='', static_folder='static')

# add cors support so i can use this with a frontend
CORS(app, crossorigin=True, resources="*")


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c0nygre1",
    database="conygre"
)

# Endpoint to get all compact discs
@app.route('/items', methods=['GET'])
def get_items():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM compact_discs")
    compact_discs = cursor.fetchall()
    cursor.close()
    return jsonify(compact_discs)


# Endpoint to get a specific compact disc by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM compact_discs WHERE id = %s", (item_id,))
    compact_disc = cursor.fetchone()
    cursor.close()
    if compact_disc:
        return jsonify(compact_disc)
    else:
        return jsonify({'error': 'Compact disc not found'}), 404

# Endpoint to create a new compact disc
@app.route('/items', methods=['POST'])
def create_item():
    title = request.json['title']
    artist = request.json['artist']
    price = request.json['price']

    cursor = db.cursor()
    cursor.execute("INSERT INTO compact_discs (title, artist, price) VALUES (%s, %s, %s)",
                   (title, artist, price))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Compact disc created successfully'})

# Endpoint to update an existing compact disc
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    title = request.json['title']
    artist = request.json['artist']
    price = request.json['price']
    cursor = db.cursor()
    cursor.execute("UPDATE compact_discs SET title = %s, artist = %s, price = %s WHERE id = %s",
                   (title, artist, price, item_id))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Compact disc updated successfully'})

# Endpoint to delete a compact disc
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM compact_discs WHERE id = %s", (item_id,))
    db.commit()
    cursor.close()

    return jsonify({'message': 'Compact disc deleted successfully'})

if __name__ == '__main__':
    app.run()
