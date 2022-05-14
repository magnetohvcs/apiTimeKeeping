from flask import Flask, request, jsonify, send_from_directory
import db, os

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
        response = db.addEmployee(request.json['firstName'], request.json['lastName'])
        return jsonify({"message" : str(response)})
    except Exception as e:
        return jsonify({"message" : e})

@app.route('/employee/editEmployee', methods=['POST'])
def editEmployee():
    try:
        return jsonify({"message" : db.editEmployee(request.json)})
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

       
@app.route('/timekeeping/getTimekeeping')
def getTimekeeping():
  data = db.getTimeKeeping()
  return data

@app.route('/timekeeping/addTimekeeping', methods=['POST'])
def addTimekeeping():
    try:
        db.addTimekeeping(request.json['idEmployee'], request.json['dateTimeKeeping'])
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False})

@app.route('/timekeeping/delTimekeeping', methods=['POST'])
def delTimeKeeping():
    return jsonify({"message": db.delTimeKeeping(request.json)})
    
@app.route('/infotimekeeping/getInfoTimeKeeping')
def getInfoTimeKeeping():
  data = db.getInfoTimeKeeping()
  return data

@app.route('/infotimekeeping/addInfoTimekeeping', methods=['POST'])
def addInfoTimekeeping():
    try:
        db.addInfoTimekeeping(request.json['idEmployee'], request.json['dateTimeKeeping'])
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False})

@app.route('/infotimekeeping/delInfoTimeKeeping', methods=['POST'])
def delInfoTimeKeeping():
    return jsonify({"message": db.delInfoTimeKeeping(request.json)})

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"message" : db.login(request.json)})

@app.route('/profile', methods=['POST'])
def profile():
    return db.getProfile(request.json)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    dir_file = f"static/{os.urandom(50).hex()}.{file.filename.split('.')[-1]}"
    file.save(os.path.join(f"/app/{dir_file}"))
    db.saveFile(dir_file)
    return jsonify({"message":"Success"}) 

@app.route('/getFile', methods=['POST'])
def getFile():
    return jsonify({'message': f"/{db.getFile(request.json['username'])}"})


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/updateProfile', methods=['POST'])
def update_profile():
    try:
        db.update_profile(request.json)
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False}) 

@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    try:
        db.update_password(request.json)
        return jsonify({"message" : True})
    except:
        return jsonify({"message" : False})     

if __name__=="__main__":
    db.init()
    app.run("0.0.0.0",8080,True)

