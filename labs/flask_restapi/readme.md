## RESTful CRUD Flask Application Exercise

In this exercise, you will create a RESTful CRUD application using Flask. The application will interact with a MySQL database. Follow the steps below to complete the exercise.

### Prerequisites

Before starting the exercise, ensure that you have the following:

- Python installed on your machine
- Flask and mysql-connector-python packages installed

### Step 1: Setting Up the Project

1. Create a new project folder on your machine.
2. Open a terminal or command prompt and navigate to the project folder.
3. Create a virtual environment by running the following command:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the necessary packages by running the following commands:
   ```
   pip install Flask
   pip install mysql-connector-python
   ```

### Step 2: Application Setup

1. Create a new Python file called `app.py`.
2. Import the required modules:
   ```python
   from flask import Flask, jsonify, request
   import mysql.connector
   ```
3. Create a Flask application:
   ```python
   app = Flask(__name__)
   db = mysql.connector.connect(
       host="localhost",
       user="root",
       password="your_password",
       database="your_database"
   )
   ```
   Replace `"your_password"` with your MySQL password and `"your_database"` with the name of your database. If you are using one of the standard lab environments, then the username is ```root``` and the password is ```c0nygre```. The database is called ```conygre```.

### Step 3: Implementing CRUD Functionality

1. Define the route for retrieving all items from the table:
   ```python
   @app.route('/items', methods=['GET'])
   def get_items():
       # Retrieve all items from the database
       # Return the items as JSON
   ```

2. Define the route for retrieving a specific item by ID:
   ```python
   @app.route('/items/<int:item_id>', methods=['GET'])
   def get_item(item_id):
       # Retrieve the item with the given ID from the database
       # Return the item as JSON
   ```

3. Define the route for creating a new item:
   ```python
   @app.route('/items', methods=['POST'])
   def create_item():
       # Retrieve the data from the request payload
       # Insert the new item into the database
       # Return a success message as JSON
   ```

4. Define the route for updating an existing item:
   ```python
   @app.route('/items/<int:item_id>', methods=['PUT'])
   def update_item(item_id):
       # Retrieve the updated data from the request payload
       # Update the corresponding item in the database
       # Return a success message as JSON
   ```

5. Define the route for deleting an item:
   ```python
   @app.route('/items/<int:item_id>', methods=['DELETE'])
   def delete_item(item_id):
       # Delete the item with the given ID from the database
       # Return a success message as JSON
   ```

### Step 4: Running the Application

1. In the terminal, ensure that the virtual environment is activated.
2. Run the Flask application by executing the following command:
   ```
   python -m flask run
   ```
3. The application will start running on a local server.

However, does it work? Let's find out using the REST Client Extension for VSCode.


## Creating Test .rest Files for REST Client Extension in VS Code

In this exercise, you will create a set of test `.rest` files using the REST Client extension in VS Code. These files will allow you to test the functionality of the RESTful CRUD Flask application you previously created. Follow the steps below to complete the exercise.

### Prerequisites

Before starting the exercise, ensure that you have the following:

- REST Client extension installed in VS Code.

### Step 1: Create a New Folder

1. Create a new folder in your project directory and name it `tests`.

### Step 2: Create Test .rest Files

1. In the `tests` folder, create a new file named `get_all_compact_discs.rest`.
2. Open the `get_all_compact_discs.rest` file and add the following content:
   ```
   GET http://localhost:5000/items
   ```
3. Save the file.

4. Repeat the steps above to create the following `.rest` files:

   - `get_compact_disc_by_id.rest`
   ```
   GET http://localhost:5000/items/1
   ```

   - `create_compact_disc.rest`
   ```
   POST http://localhost:5000/items
   Content-Type: application/json

   {
       "title": "New Album",
       "artist": "New Artist",
       "price": 9.99
   }
   ```

   - `update_compact_disc.rest`
   ```
   PUT http://localhost:5000/items/10
   Content-Type: application/json

   {
       "title": "Updated Album",
       "artist": "Updated Artist",
       "price": 11.99
   }
   ```

   - `delete_compact_disc.rest`
   ```
   DELETE http://localhost:5000/items/10
   ```

### Step 3: Run Test Requests

1. Open the `.rest` file you want to test (e.g., `get_all_compact_discs.rest`) in VS Code.
2. Click on the "Send Request" button next to the request URL.
3. Observe the response in the VS Code output panel.
4. Repeat the steps for the other `.rest` files you created.

---

Follow these steps to create test `.rest` files and use the REST Client extension in VS Code to test the functionality of your RESTful CRUD Flask application.

Note: Make sure the Flask application is running before sending the requests.

