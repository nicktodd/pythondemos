# Flask-MySQL Web App

This is a simple Flask based web app that displays data from a MySQL database. 

## Prerequisites

Before starting this exercise, you should have the following installed on your Windows machine:
- Python 3
- Visual Studio Code
- Flask (`pip install flask`)
- MySQL Connector (`pip install mysql-connector-python`)

## Set up the project

1. Open Visual Studio Code and create a new folder for your project.
2. Open a terminal window and navigate to the project folder.
3. Create a new Python file named `app.py`.
4. Create a new folder named `templates`.
5. Inside the `templates` folder, create a new HTML file named `index.html`.


## Set up the Flask app

1. Open `app.py` in Visual Studio Code.
2. Import the necessary modules:
    ```
    from flask import Flask, render_template
    import mysql.connector
    ```
3. Create a Flask app instance:
    ```
    app = Flask(__name__)
    ```
4. Create a function that connects to the database and retrieves the data from the `compact_discs` table:
    ```
    def get_albums():
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM compact_discs")
        albums = cursor.fetchall()
        conn.close()
        return albums
    ```
   Note: Replace `yourusername`, `yourpassword`, and `yourdatabase` with your MySQL credentials and database name.
   
5. Create a route that renders the `index.html` template and passes the album data to it:
    ```
    @app.route("/")
    def index():
        albums = get_albums()
        return render_template("index.html", albums=albums)
    ```

## Create the HTML template

1. Open `index.html` in Visual Studio Code.
2. Add the following code to the file:
    ```
    <!DOCTYPE html>
    <html>
    <head>
        <title>Albums</title>
    </head>
    <body>
        <h1>Albums</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Artist</th>
                <th>Title</th>
                <th>Price</th>
            </tr>
            {% for album in albums %}
            <tr>
                <td>{{ album[0] }}</td>
                <td>{{ album[1] }}</td>
                <td>{{ album[2] }}</td>
                <td>{{ album[3] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ```

## Run the Flask app

1. Open a terminal window and navigate to the project folder (or if in VSCode use the terminal in the VSCode environment).
2. Type `python -m flask run` and press Enter to start the Flask app.
3. Open a web browser and go to `http://localhost:5000`.
4. You should see a web page that displays the data from the `compact_discs` table.
