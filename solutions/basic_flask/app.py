from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_albums():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="c0nygre1",
        database="conygre"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compact_discs")
    albums = cursor.fetchall()
    conn.close()
    return albums

@app.route("/")
def index():
    albums = get_albums()
    return render_template("index.html", albums=albums)