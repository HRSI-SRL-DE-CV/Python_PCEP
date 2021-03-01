"""
flag = True
numero = 0


while flag:
    numero += 5
    print(numero)
    if numero == 50:
        flag = False
print('Salio del ciclo')"""


"""
for number in range(1,101,5):
    print(number)"""

lista = ['pantalon','camisa','gorra','corbata']
lista2 = ['Negro','Rojo','Azul','Verde']
response = []
"""
for element in lista:
    for item in lista2:
        new_struct = {
            element : item
        }
        response.append(new_struct)
print(response)"""

for item in range(len(lista)):
    print(lista[item])
