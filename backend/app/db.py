import pymongo, os
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

def generateUsername():
  return "NV{0:04d}".format(count(mycolEmployee.find()))  
  
def Id4Product():
  return "SP{0:09d}".format(count(mycolProduct.find()))  

def Id4TimeKeeping():
    return "TP{0:10d}".format(count(mycolTimeKeeping.find()))

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
  mycolProduct.delete_one(query)

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


def addTimekeeping(idEmployee, dateTimeKeeping):
    mydict = {"id": Id4TimeKeeping(), "idEmployee": idEmployee, "dateTimeKeeping": dateTimeKeeping}
    mycolTimeKeeping.insert_one(mydict)

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

def login(query ):
  x = mycolEmployee.find_one(query)
  if x != None:
    return True
  return False

def updatePassword(query):
  newvalues = { "$set": {  "password" : query['password'] } }
  mycolEmployee.update_one({"username": query['username']}, newvalues)

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
  newvalues = { "$set": {  "firstName" : query['firstName'], 'lastName':query['lastName'] } }
  mycolEmployee.update_one({"username": query['username']}, newvalues)

def update_password(query):
  newvalues = { "$set": {  "password" : query['password'] } }
  mycolEmployee.update_one({"username": query['username']}, newvalues)