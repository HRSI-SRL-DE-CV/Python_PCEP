diccionario = {1: 3,'key2': 6,'key3':[23,45,67,78,'Justino','Elizabeth']}
print(diccionario)


"""
#Obtiene todos los keys del diccionario
for item in diccionario.keys():
    print(item)

#Obtiene todos los valores del diccionario
for item in diccionario.value():
    print(item)

#Obtiene todos elementos
for key,value in diccionario.items():
    print(key,value)
"""


ropa = ['playera','pantalon','zapatos']
colores = ['negro','rojo','azul']
lista = []

count = 0
for clothe in ropa:
    for color in colores:
        new_struct = {
            clothe+str(count):color
        }
        lista.append(new_struct)
        count += 1

lista[0]['playera0'] = 'Gris'
diccionario['key4'] = 890 
del (lista[0]['playera0'])

print(lista,diccionario)
