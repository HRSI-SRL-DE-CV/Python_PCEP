import time


#Recursividad
start_recursive = time.time()

def recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + recursiva(lista[1:])

print(recursiva([1,4,5,6,82,90,34,56]), "-- %s seconds --" % (time.time() - start_recursive))


start_for = time.time()
lista = [1,4,5,6,82,90,34,56]
result = 0

for number in lista:
    result = result + int(number)

print(result,'--- %s seconds ---' % (time.time() - start_for))


result = lambda x,y,z: x * 50 + y -z
print(result(20,50,20))
print(result(30))



full_name = lambda name,lastname: f'This is my name: {name.title()} {lastname.title()} '
print(full_name('manuel','ruiz'))

