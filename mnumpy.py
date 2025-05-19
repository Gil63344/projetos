import numpy as np 

dados = np.genfromtxt('dados_grande.csv',delimiter=',',skip_header=1,dtype=str)


def MediaIdades(dados):
       
    return round(np.mean([int(pessoa[1]) for pessoa in dados]),2)

def MediaNotas(dados):
       
    return round(np.mean([float(pessoa[2]) for pessoa in dados]),2)


def PessoasAcimaMediaIdade(dados,media):
    nomePessoas = {}

    for linha in dados:
        nomePessoas[f'Pessoa com idade acima da média de {media}'] = [pessoa[0] for pessoa in dados if int(pessoa[1]) > media]

    return nomePessoas

def PessoasAcimaMediaNotas(dados,media):
    pessoasComNotasAcima = {}

    for linha in dados:
        pessoasComNotasAcima[f'Pessoas com média acima de {media}'] = [pessoas[0] for pessoas in dados if float(pessoas[2]) > media]

    return pessoasComNotasAcima



print(f'Média de idades das pessoas: {MediaIdades(dados=dados)}')
print(f'Média notas : {MediaNotas(dados=dados)}')
print(dados[:5])

dataset = PessoasAcimaMediaIdade(dados=dados,media=MediaIdades(dados=dados))
for chave, valor in dataset.items():
    print(f'{chave }: {valor}')

print()
print()

dataset2 = PessoasAcimaMediaNotas(dados,MediaNotas(dados))
for chave,valor in dataset2.items():
    print(f'{chave}: {valor}')


