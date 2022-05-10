MONGODB_CONNSTRING="mongodb://root:root@localhost"
import pymongo

myclient = pymongo.MongoClient(MONGODB_CONNSTRING)

mydb = myclient["mydatabase"]

mycolEmployee = mydb["employee"]


def generateUsername():
  print(len(mycolEmployee.find()))

def getEmployee():
  pass
  
def addEmployee(firstName, lastName):
  mydict = { "firstName": firstName, "lastName": lastName, "username": "NV0001", "password": "NV0001" }
  mycolEmployee.insert_one(mydict)

generateUsername()