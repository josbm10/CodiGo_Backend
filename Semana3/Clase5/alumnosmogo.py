from pymongo import MongoClient

cliente=MongoClient('mongodb://localhost:27017')

db=cliente['codigo11']

colAlumnos=db["alumnos"]

# alumnoId=colAlumnos.insert_one({"nombre":"juan perez","email":"perez@gmail.com","nota":8})

# print(alumnoId)
# consultar datos

for a in colAlumnos.find():
    print(a["nombre"]+"|"+a["email"])