import pymongo, os
myclient = pymongo.MongoClient(os.getenv('MONGODB_CONNSTRING'))

mydb = myclient["mydatabase"]
mycolEmployee = mydb["employee"]
mycolProduct = mydb["product"]

def count(result):
  count = 1
  for _ in result:
    count += 1
  return count

def generateUsername():
  return "NV{0:04d}".format(count(mycolEmployee.find()))  
  
def Id4Product():
  return "SP{0:09d}".format(count(mycolProduct.find()))  

def getEmployee():
  list = [element for element in mycolEmployee.find({},{"_id":0})]
  dict = {}
  for index, element in zip(range(0,len(list)), list ):
    dict[index] = element
  return dict
  
def addEmployee(firstName, lastName):
  username = generateUsername()
  mydict = { "firstName": firstName, "lastName": lastName, "username": username, "password": username }
  mycolEmployee.insert_one(mydict)

def delEmployee(query : dict):
  if query['id'] == 'NV0001':
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

