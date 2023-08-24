from flask import Flask


app = Flask(__name__)


@app.route('/greeting')
def greeting():
    return {'greetingMessage': 'Hello user!'}
