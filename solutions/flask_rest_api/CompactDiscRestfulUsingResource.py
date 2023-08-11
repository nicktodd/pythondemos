from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector

app = Flask(__name__)
api = Api(app)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="c0nygre1",
    database="conygre"
)

class CompactDiscsResource(Resource):
    def get(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM compact_discs")
        compact_discs = cursor.fetchall()
        cursor.close()
        return jsonify(compact_discs)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('artist', required=True)
        parser.add_argument('track_count', required=True, type=int)
        parser.add_argument('price', required=True, type=float)
        args = parser.parse_args()

        title = args['title']
        artist = args['artist']
        track_count = args['track_count']
        price = args['price']

        cursor = db.cursor()
        cursor.execute("INSERT INTO compact_discs (title, artist, track_count, price) VALUES (%s, %s, %s, %s)",
                       (title, artist, track_count, price))
        db.commit()
        cursor.close()

        return {'message': 'Compact disc created successfully'}, 201

class CompactDiscResource(Resource):
    def get(self, cd_id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM compact_discs WHERE id = %s", (cd_id,))
        compact_disc = cursor.fetchone()
        cursor.close()
        if compact_disc:
            return jsonify(compact_disc)
        else:
            return {'error': 'Compact disc not found'}, 404

    def put(self, cd_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('artist', required=True)
        parser.add_argument('track_count', required=True, type=int)
        parser.add_argument('price', required=True, type=float)
        args = parser.parse_args()

        title = args['title']
        artist = args['artist']
        track_count = args['track_count']
        price = args['price']

        cursor = db.cursor()
        cursor.execute("UPDATE compact_discs SET title = %s, artist = %s, track_count = %s, price = %s WHERE id = %s",
                       (title, artist, track_count, price, cd_id))
        db.commit()
        cursor.close()

        return {'message': 'Compact disc updated successfully'}, 200

    def delete(self, cd_id):
        cursor = db.cursor()
        cursor.execute("DELETE FROM compact_discs WHERE id = %s", (cd_id,))
        db.commit()
        cursor.close()

        return {'message': 'Compact disc deleted successfully'}, 200

api.add_resource(CompactDiscsResource, '/compact_discs')
api.add_resource(CompactDiscResource, '/compact_discs/<int:cd_id>')

if __name__ == '__main__':
    app.run()
