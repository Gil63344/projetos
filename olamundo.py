import string

from random import *

def numeroAcertos(lista,gabarito):
    cont = 0
    for i in range(len(gabarito)):
        if lista[i] == gabarito[i]:
            cont +=1
    
    return lista,cont


gabarito = [choice(string.ascii_uppercase[:5]) for i in range(10)]

dic_respostas_aluno = {}

for i in range(5):
    dic_respostas_aluno[i] = numeroAcertos([choice(string.ascii_uppercase[:5]) for i in range(10)],gabarito)

for chave,valor in dic_respostas_aluno.items():
    print(f'{chave}: {valor}')



