from random import *


numeros = [str(randint(1,10000)) for i in range(10)]
print(numeros)

rel = { }

for numero in numeros:
    if numero[0] not in rel:
        rel[numero[0]] = [int(num) for num in numeros if num[0] == numero[0]]

for i,j in rel.items():
    print(f'{i} : {j}')