cantidad=int(input("ingrese la cantidad de datos: "))
numeros=[]
for numero in range(cantidad):
    numero=int(input("ingrese numero "+ str(numero+1)+": "))
    numeros.append(numero)
    
print("mayor",max(numeros))
print("menor",min(numeros))
print("promedio",sum(numeros)/cantidad)

numeros2=tuple(numeros)
print("tuple",sorted(numeros2))