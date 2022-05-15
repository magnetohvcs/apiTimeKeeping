import pymongo, os
import pandas as pd
from datetime import date

myclient = pymongo.MongoClient(os.getenv('MONGODB_CONNSTRING'))

mydb = myclient["mydatabase"]


mycolEmployee = mydb["employee"]
mycolProduct = mydb["product"]
mycolTimeKeeping = mydb["timekeeping"]
mycolInfoTimeKeeping = mydb["infotimekeeping"]

def count(result):
  count = 1
  for _ in result:
    count += 1
  return count

def init():
  try:
    x = mycolEmployee.find_one()
    if x == None:
      mydict = { "firstName": 'admin', "lastName": 'admin', "username": 'admin', "password": 'admin' }
      x = mycolEmployee.insert_one(mydict)
  except:
    pass

def generateUsername():
  return "NV{0:04d}".format(count(mycolEmployee.find()))  
  
def Id4Product():
  return "SP{0:04d}".format(count(mycolProduct.find()))  

def Id4TimeKeeping():
    return "TP{0:4d}".format(count(mycolTimeKeeping.find()))

def getEmployee():
  list = [element for element in mycolEmployee.find({},{"_id":0})]
  dict = {}
  for index, element in zip(range(0,len(list)), list ):
    dict[index] = element
  return dict
  
def addEmployee(firstName, lastName):
  username = generateUsername()
  mydict = { "firstName": firstName, "lastName": lastName, "username": username, "password": username }
  x = mycolEmployee.insert_one(mydict)
  return x.inserted_id

def delEmployee(query : dict):
  if query['id'] == 'admin':
    return False
  mycolEmployee.delete_one({"username" : query['id']})
  return True

def editEmployee(value):
  myquery = { "username": value["username"] }
  newvalues = { "$set": { "firstName": value["firstName"], "lastName" : value["lastName"] } }
  mycolEmployee.update_one(myquery, newvalues)

def addProduct( name, price=0):
  mydict = { "id": Id4Product(), "name": name, "price": price}
  mycolProduct.insert_one(mydict)

def delProduct(query : dict):
  mycolProduct.delete_one({'id':query['id']})

def getProduct():
  list = [element for element in mycolProduct.find({},{"_id":0})]
  dict = {}
  for index, element in zip(range(0,len(list)), list ):
    dict[index] = element
  return dict

def editProduct(value):
  myquery = { "id": value["id"] }
  newvalues = { "$set": { "name": value["name"], "price" : value["price"] } }
  mycolProduct.update_one(myquery, newvalues)


def delTimeKeeping(query: dict):
    mycolTimeKeeping.delete_one(query)

def getTimeKeeping():
    list = [element for element in mycolTimeKeeping.find({},{"_id":0})]
    dict = {}
    for index, element in zip(range(0,len(list)), list ):
        dict[index] = element
    return dict

def addInfoTimekeeping(idTime , idProduct , num1Pro , num0Pro ):
    mydict = {"idTime ": idTime, "idProduct": idProduct , "num1Pro": num1Pro, "num0Pro": num0Pro }
    mycolInfoTimeKeeping.insert_one(mydict)

def delInfoTimeKeeping(query: dict):
    mycolInfoTimeKeeping.delete_one(query)

def getInfoTimeKeeping():
    list = [element for element in mycolInfoTimeKeeping.find({},{"_id":0})]
    dict = {}
    for index, element in zip(range(0,len(list)), list ):
        dict[index] = element
    return dict

def login(query):
  x = mycolEmployee.find_one({'username': query['username'], 'password': query['password']})
  if x != None:
    return True
  return False

def updatePassword(username, password):
  newvalues = { "$set": {  "password" : password} }
  mycolEmployee.update_one({"username": username}, newvalues)

def getProfile(query):
  x = mycolEmployee.find_one(query, {"_id":0 , "password":0})
  return x

def saveFile(dir_file):
  newvalues = { "$set": {  "file_image" : dir_file } }
  mycolEmployee.update_one({"username": "admin"}, newvalues)

def getFile(username):
  try:
    x = mycolEmployee.find_one({"username": username}, {"_id":0 , "password":0})
    return x['file_image']
  except:
    return None

def update_profile(query):
  newvalues = { "$set": {  "firstName" : query['firstName'], 'lastName':query['lastName'], 'email': query['email'], 'sdt':query['sdt'] } }
  mycolEmployee.update_one({"username": query['username']}, newvalues)

def update_password(query):
  newvalues = { "$set": {  "password" : query['password'] } }
  mycolEmployee.update_one({"username": query['username']}, newvalues)

def exportEmployee():
  id, first, last = [],[],[]
  
  for element in mycolEmployee.find({},{"_id":0, "password":0}):
    id.append(element['username'])
    first.append(element['firstName'])
    last.append(element['lastName'])

  data = {'Ma Cong Nhan': id,
        'Ho': first,
        'Ten': last
        }

  df = pd.DataFrame(data, columns = ['Ma Cong Nhan', 'Ho', 'Ten'])
  dir_file = f'/app/static/employee{os.urandom(10).hex()}.xlsx'
  df.to_excel(dir_file, index = False, header=True)
  return dir_file

def findTimeKeeping(query):
  x = mycolTimeKeeping.find_one(query)
  return x

def checkIn(id):
  current_date = date.today()
  try:
    x = mycolTimeKeeping.find_one({"idEmployee": id, "dateTimeKeeping": current_date})
    if x['checkIN']:
      return "Hom nay ban da check in"
  except:
    mydict = {"id": Id4TimeKeeping(), "idEmployee": id, "dateTimeKeeping": current_date, "checkIn": True}
    mycolTimeKeeping.insert_one(mydict)
    return "Ban da check in thanh cong"

def checkOut(query):
  current_date = date.today()
  try:
    x = mycolTimeKeeping.find_one({"idEmployee": query['id'], "dateTimeKeeping": current_date})
    if x['checkIn']:
      newvalues = { "$set": {  "checkOut" : True } }
      mycolTimeKeeping.update_one({"idEmployee": id, "dateTimeKeeping": current_date}, newvalues)
      
    x = mycolTimeKeeping.find_one({"idEmployee": query['id'], "dateTimeKeeping": current_date})  
    if x['checkOut']:
      addInfoTimekeeping(x['id'],query['idProduct'], query['num1'], query['num0'] )
  except:
    return "Ban da check out thanh cong"
  
    