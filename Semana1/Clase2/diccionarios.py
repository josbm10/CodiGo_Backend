capitales={'peru':'lima','chile':'santiago','uruguay':'montevideo'}

print(capitales)
capital={'brasil':'brasilia'}
capitales.update(capital)
print(capitales)
c=capitales.pop('bolivia','no existe el pais')
print(c)
capitales2=capitales.copy()
print(capitales2)

for clave in capitales:
    print(clave," : ",capitales[clave])
    
print(capitales.keys())
print(capitales.values())

for clave in capitales.keys():
    print(clave," -- ",capitales[clave])
for clave,valor in capitales.items():
    print(clave," => ",valor)
    