
# w=write sobreescribe todo el archivo a=apend mantiene los cambios r=read los lee
# f=open('alumnos.txt','a')
# f.write('\njose arcos')

from os import close


f=open('alumnos.txt','r')
alumnos=f.read()
lstresultados=[]

lstAlumnos=alumnos.splitlines()
print(lstAlumnos)

for dicAlumnos in lstAlumnos:
    lstdicAlumnos=dicAlumnos.split(',')
    print(lstdicAlumnos)
    dicAlumnos={
        'nombre':lstdicAlumnos[0],
        'email':lstdicAlumnos[0],
        'celular':lstdicAlumnos[0]
    }
    lstresultados.append(dicAlumnos)
    
print(lstresultados)
f.close