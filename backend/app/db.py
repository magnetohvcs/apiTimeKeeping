import pymongo, os

myclient = pymongo.MongoClient(os.getenv('MONGODB_CONNSTRING'))

mydb = myclient["mydatabase"]

mycolEmployee = mydb["employee"]

def count(result):
  count = 1
  for _ in result:
    count += 1
  return count

def generateUsername():
  return "NV{0:04d}".format(count(mycolEmployee.find()))  
  
def getEmployee():
  list = [element for element in mycolEmployee.find({},{"_id":0, "password":0})]
  dict = {}
  for index, element in zip(range(0,len(list)), list ):
    dict[index] = element
  return dict
  
def addEmployee(firstName, lastName):
  username = generateUsername()
  mydict = { "firstName": firstName, "lastName": lastName, "username": username, "password": username }
  mycolEmployee.insert_one(mydict)

