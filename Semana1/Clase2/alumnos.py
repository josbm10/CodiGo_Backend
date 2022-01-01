# programa crud para alumnos
import tabulate

alumnos=[]
opcion = 0
print("===========================")
print("PROGRAMA DE ALUMNOS CODIGO")
print("===========================")
print("MARQUE LA OPCION QUE DESEA")
print("[1] REGISTRAR ALUMNO")
print("[2] MOSTRAR ALUMNO")
print("[3] ACTUALIZAR ALUMNO")
print("[4] ELIMINAR ALUMNO")
print("[5] SALIR DEL PROGRAMA")

while(opcion != 5):
    print("============================")
    opcion = int(input("INGRESE OPCION: "))
    print("============================")
    if (opcion == 1):
        print("==========================")
        print("REGISTRAR NUEVO ALUMNO")
        print("==========================")
        nombre=input("INGRESE NOMBRE: ")
        email=input("INGRESE EMAIL: ")
        celular=input("INGRESE CELULAR: ")
        data={'nombre':nombre,
              'email':email,
              'celular':celular}
        alumnos.append(data)
        print("ALUMNO AGREGADO")
    elif (opcion == 2):
        print("==========================")
        print("RELACION DE ALUMNO")
        print("==========================")
        cabecera=alumnos[0].keys()
        registro=[x.values() for x in alumnos]
        print(tabulate.tabulate(registro,cabecera)) 
        print("==========================")
    elif (opcion == 3):
        print("==========================")
        print("MODIFICAR DATOS DE ALUMNO")
        print("==========================")
        alumno = input("Ingrese el nombre del alumno a modificar: ")
        for x in alumnos:
            if x['nombre'] == alumno:
                x['nombre'] = input("NOMBRE : ")
                x['email'] = input("EMAIL: ")
                x['celular'] = input("CELULAR: ")
                print("Alumno modificado correctamente")
                break
       
    elif (opcion == 4):
        print("==========================")
        print("ELIMINAR DATOS DE ALUMNO")
        print("==========================")
        alumno = input("Ingrese el nombre del alumno a eliminar: ")
        posAlumno = -1
        for i in range(len(alumnos)):
            dictAlumnoBusqueda = alumnos[i]
            for clave,valor in dictAlumnoBusqueda.items():
                if (valor == alumno):
                    posAlumno = i
                    break
        alumnos.pop(posAlumno)
        print("ALUMNO ELIMINADO!!!")
    
    elif (opcion == 5):
        print("=================================")
        print("GRACIAS POR USAR NUESTRO PROGRAMA")
        print("=================================")   
    else:
        print("==========================")
        print("PARAMETRO NO ADMITIDO")
        print("==========================")
        