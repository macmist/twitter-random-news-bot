#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
from flask import Flask, request, send_from_directory, jsonify
from rss_reader import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({'result': randomize()})


@app.route('/view/<path:path>')
def send_view(path):
    return send_from_directory('view', path)


if __name__ == '__main__':
    app.run(debug=True, port=4242, host='0.0.0.0')
