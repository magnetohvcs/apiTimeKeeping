import mysql.connector, os

hostdb =  os.getenv('hostdb')
password =  os.getenv('passworddb')


mydb = mysql.connector.connect(
  host=hostdb,
  user="root",
  password=password,
  database="TimeKeeping"
)

cursor = mydb.cursor()

def line2json(arrKey : list, lineData) -> dict:
  data = {}
 
  for key,d in zip(arrKey, lineData):
    data[key] = str(d)
  return data

def list2json(arrKey : list, listData):
  data = {}
  for line, index in zip(toList(listData), range(len(listData))):
    data[index] = line2json(arrKey, line)
  return data

def toList(arr):
  data = []
  for line in arr:
    data.append(list(line[0]))
  return data

class database:
  def __init__(self) -> None:
      pass

  def getEmployees(self):
    cursor.execute("SELECT Employee.id,firstName,lastName,idFactory,name FROM Employee, Factory where Factory.id=Employee.idFactory")
    
    myresult =  cursor.fetchall()
    data = line2json(["id","firstName","lastName","idFactory","nameFactory"], myresult)

    return data
    
  def checkExistUsername(self, username : str):
    sql = "select 1 from Employee where username=%s"
    val = (username,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    if result == []:
      return username
    return None

  def generateUsername(self, username : str):
    result = self.checkExistUsername(username)
    count = 1
    while result == None:
      result = self.checkExistUsername(f'{username}{count}')
      count += 1
    return result 

  def addEmployee(self, firstname : str, lastname : str, idFactory) -> bool:
    name = f"{firstname}{lastname}"
    while ' ' in name:
      name = name.replace(' ','')
    username = self.generateUsername(name)
    sql = "INSERT INTO Employee (firstname, lastname, idFactory, username, password) VALUES (%s, %s, %s, %s, %s)"
    val = (firstname, lastname, idFactory, username, name)
    try:
      cursor.execute(sql, val)
      mydb.commit()
      print(cursor.rowcount, "record inserted.")
      return True
    except Exception as e:
      return False

db = database()

result = db.getEmployees()

print(result)