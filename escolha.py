import string 
import random

def numero_acertos(respostas,gabarito):
    acertos = 0
    for i in range(len(respostas)):
        if respostas[i] == gabarito[i]:
            acertos += 1

    return acertos



questoes:int = 15

gabarito_oficial = [random.choice(string.ascii_uppercase[:6]) for i in range(questoes)]
#print(gabarito_oficial)

respostas_alunos = [numero_acertos([random.choice(string.ascii_uppercase[:6]) for i in range(questoes)],gabarito_oficial) for i in range(15)]
#print(respostas_alunos)

resultado = {}

for i in range(15):
    resultado[i+1] = respostas_alunos[i]


for aluno,acertos in resultado.items():
    print(f'Aluno {aluno} : Acertou {acertos}')







