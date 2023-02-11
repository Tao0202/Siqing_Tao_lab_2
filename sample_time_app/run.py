from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def get_time():
    # ct stores current time
    ct = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return ct


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
