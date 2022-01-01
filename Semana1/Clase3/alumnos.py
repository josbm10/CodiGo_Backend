# programa crud para alumnos
from sistem.libreria import *

alumnos=[{'nombre':'leonel','email':'josbm10@hotmail.com','celular':'998956123'}]
opcion = 0

    
print("===========================")
print("PROGRAMA DE ALUMNOS CODIGO")
print("===========================")
while(opcion != 5):
    menu()
    print("============================")
    opcion = int(input("INGRESE OPCION: "))
    print("============================")
    if (opcion == 1):
        registrar(alumnos)
    elif (opcion == 2):
        mostrar(alumnos)
    elif (opcion == 3):
        modificar(alumnos)
    elif (opcion == 4):
        eliminar(alumnos)
    elif (opcion == 5):
        print("=================================")
        print("GRACIAS POR USAR NUESTRO PROGRAMA")
        print("=================================")   
    else:
        print("==========================")
        print("PARAMETRO NO ADMITIDO")
        print("==========================")
        