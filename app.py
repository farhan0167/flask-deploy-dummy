from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return jsonify({'message': 'Hello World Farhan'})


@app.route("/wow")
def hello_world2():
    return jsonify({'message': 'This is the wow endpoint!'})