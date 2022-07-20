from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/submit', methods=['POST'])
def handle_submit():
    name_from_form = request.form["name"]
    return render_template("hello.html", name=name_from_form)


if __name__ == '__main__':
    app.run()
