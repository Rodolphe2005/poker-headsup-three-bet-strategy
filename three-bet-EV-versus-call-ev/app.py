from flask import Flask, json, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def hello():
    response = jsonify([{"position": request.json['position']}])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == 'main':
    app.run()
