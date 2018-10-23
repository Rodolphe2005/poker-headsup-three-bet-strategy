from flask import Flask, json

app = Flask(__name__)


@app.route("/")
def hello():
    return json.dumps([{"position": 30}])


app.run()
