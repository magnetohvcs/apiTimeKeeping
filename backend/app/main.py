from flask import Flask, request, jsonify
from db import database

app = Flask(__name__)
db = database()


@app.route('/')
def index():
    return jsonify({"message":"Hello world"})

@app.route('/employee/getEmployee')
def getEmployee():
    data = db.getEmployees()
    return data

if __name__=="__main__":
    app.run("0.0.0.0",8080,True)