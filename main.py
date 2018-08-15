
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi, fine web'
    # Rendering route for the test
@app.route('/novan')
def novan():
    return 'Test that Novan exists'
