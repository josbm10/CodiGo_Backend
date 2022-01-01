dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
primos=[2,3,5,7,11,13]
fecha=["martes",14,"diciembre",2021]

print(len(dias))
print(primos)
primos.append(17)
print(primos)
primos.pop()
print(primos)

for dia in dias:
    print("dia: " + dia)
for dia in range(len(dias)):
    print(dias[dia])
    
    