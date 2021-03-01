"""import time

start = time.time() 
lista = [1,5,7,3,9]
#lista = ['manuel','Manuel','lalo','Eduardo','Juan']
flag = True
while flag:
    flag = False
    for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            flag = True
            lista[x],lista[x+1] = lista[x+1],lista[x]
    result = lista
    print(lista)
print(result,"--- %s seconds ---" % (time.time() - start),start) """


import time
start = time.time() 
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
            [arr[0]] + \
            qsort([x for x in arr[1:] if x >= arr[0]])
#lista = ['manuel','Manuel','lalo','Eduardo','Juan']
lista = [1,5,7,3,9]
result = qsort(lista)
print(result,"--- %s seconds ---" % (time.time() - start),start)