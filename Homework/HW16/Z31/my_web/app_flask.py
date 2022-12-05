from flask import flask

app = flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World'


@app.route('/my_web')
def hello():
    return 'My name is Yaroslav'
