dias=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
primos=(2,3,5,7,11,13)
fecha=("martes",14,"diciembre",2021)
# las tuplas no se pueden modificar
primos2=list(primos)
primos2.append(17)
primos=tuple(primos2)
primosordenados=sorted(primos2,reverse=True)
print(max(primos))
print(max(primos2))
print(sum(primos)/len(primos))
