from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello():
    f = open("outFile.txt", "r")
    return  f.read()
