from flask import Flask, request, jsonify
import db

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message":"Hello world"})

@app.route('/employee/getEmployee')
def getEmployee():
    data = db.getEmployee()
    return data

if __name__=="__main__":
    app.run("0.0.0.0",8080,True)