"""lista = [x for x in range(100)]
lista2 = [[x for x in range(8)] for y in range(8)]

lista2[1][5] = 'Peon'

count = 0
for item in lista2:
    if count == 1:
        for element in range(8):
            lista2[1][element] = 'Peon'
    count += 1

print(lista2)"""


tupla = (1,2,4,5,7)
tupla = list(tupla)
tupla.append(90)
tupla = tuple(tupla)


print(tupla)