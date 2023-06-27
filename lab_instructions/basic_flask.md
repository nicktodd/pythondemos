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

## Set up the database

1. Install MySQL server on your machine if it is not already installed.
2. Create a new database in MySQL for this project.
3. Create a new table in the database named `compact_discs`. The `compact_discs` table should have columns for `id`, `artist`, `title`, `year`, and `genre`.
4. Add some sample data to the `compact_discs` table.

You can use the following SQL script to complete this task:

```
CREATE DATABASE IF NOT EXISTS conygre;
use conygre;
create table compact_discs (id int primary key auto_increment,title varchar (50),artist varchar(30),tracks int,price double);

CREATE TABLE tracks (id int primary key auto_increment,
		     cd_id int not null,
                    title varchar(50),
                    FOREIGN KEY (cd_id) REFERENCES compact_discs(id)
                    
);


insert into compact_discs values(9,'Is This It','The Strokes',11,13.99);
insert into compact_discs values(10,'Just Enough Education to Perform','Stereophonics',11,10.99);
insert into compact_discs values(11,'Parachutes','Coldplay',10,11.99);
insert into compact_discs values(12,'White Ladder','David Gray',10,9.99);
insert into compact_discs values(13,'Greatest Hits','Penelope',14,14.99);
insert into compact_discs values(14,'Echo Park','Feeder',12,13.99);
insert into compact_discs values(15,'Mezzanine','Massive Attack',11,12.99);
insert into compact_discs values(16,'Spice World','Spice Girls',11,4.99);


use conygre; 


insert into tracks values (1, 16, 'Mama');
insert into tracks values (2, 16, 'Wannabe');
insert into tracks values (3, 16, 'Spice up your life');

```

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
4. Create a function that connects to the database and retrieves the data from the `albums` table:
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
                <th>Year</th>
                <th>Genre</th>
            </tr>
            {% for album in albums %}
            <tr>
                <td>{{ album[0] }}</td>
                <td>{{ album[1] }}</td>
                <td>{{ album[2] }}</td>
                <td>{{ album[3] }}</td>
                <td>{{ album[4] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ```

## Run the Flask app

1. Open a terminal window and navigate to the project folder (or if in VSCode use the terminal in the VSCode environment).
2. Type `python -m flask app.py` and press Enter to start the Flask app.
3. Open a web browser and go to `http://localhost:5000`.
4. You should see a web page that displays the data from the `compact_discs` table.

![WebSite Showing Data from Database(images/)]