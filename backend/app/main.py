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

@app.route('/employee/delEmployee', methods=['POST'])
def delEmployee():
    return jsonify({"message" : db.delEmployee(request.json)})

@app.route('/employee/addEmployee', methods=['POST'])
def addEmployee():
    try:
        return jsonify({"message" : db.addEmployee(request.json['firstName'], request.json['lastName'])})
    except Exception as e:
        return jsonify({"message" : e})

@app.route('/employee/editEmployee', methods=['POST'])
def editEmployee():
    try:
        return jsonify({"message" : db.editEmployee(request.json['firstName'], request.json['lastName'])})
    except Exception as e:
        return jsonify({"message" : e})


@app.route('/product/getProduct')
def getProduct():
    data = db.getProduct()
    return data

@app.route('/product/addProduct', methods=['POST'])
def addProduct():
    try:
        db.addProduct(request.json['name'], request.json['price'])
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False})

@app.route('/product/delProduct', methods=['POST'])
def delProduct():
    return jsonify({"message" : db.delProduct(request.json)})

@app.route('/product/editProduct', methods=['POST'])
def editProduct():
    try:
        db.editProduct(request.json)
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False})


if __name__=="__main__":
    app.run("0.0.0.0",8080,True)