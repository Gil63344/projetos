from random import *
import string

def numeroAcertos(respostas,gabarito):
    acertos = 0
    for i in range(len(respostas)):
        if respostas[i] == gabarito[i]:
            acertos+=1
    return acertos


gabarito = [choice(string.ascii_uppercase[:4]) for i in range(10)]
numero_alunos = 40
dic_alunos = {}

for i in range(numero_alunos):
    dic_alunos[i] = numeroAcertos([choice(string.ascii_uppercase[:4]) for i in range(10)],gabarito)


for chave,valor in dic_alunos.items():
    print(f'Aluno {chave + 1} : Acertou {valor}')

