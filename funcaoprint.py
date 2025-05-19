import csv

dadosGerais = []
with open('dados_grande.csv') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)
    for linha in dados:
        dadosGerais.append(linha)

def DadosPorIdade(dados:list):
    dicionarioPorIdade = {}


    for linha in dados:
        if int(linha[1]) not in dicionarioPorIdade:
            dicionarioPorIdade[int(linha[1])] = [pessoas[0] for pessoas in dados if int(pessoas[1]) == int(linha[1])]

    return dicionarioPorIdade

def DadosAcimadeValor(dados:list,valor):
    dicionarioPorValor = dict()

    for linha in dados:
        dicionarioPorValor[f'Pessoas com Nota maior que {valor}'] = [pessoa[0] for pessoa in dados if float(pessoa[2]) >= float(valor)]
    
    return dicionarioPorValor

def NomesComInicial(dados:list):
    dicionarioLetraIicial = {}

    for linha in dados:
        if linha[0][0][0] not in dicionarioLetraIicial:
            dicionarioLetraIicial[linha[0][0][0]] = [nome[0] for nome in dados if nome[0][0][0] == linha[0][0][0]]

    return dicionarioLetraIicial



dados_ = DadosPorIdade(dadosGerais)
for chave, valor in dados_.items():
    print(chave,valor)


dados_1 = DadosAcimadeValor(dados=dadosGerais,valor=7)

for idade,nome in dados_1.items():
    print(f'{idade}: Nomes: {nome}')


dados_2 = NomesComInicial(dados=dadosGerais)

for chave,nome in dados_2.items():
    print(f'{chave}: Nomes: {nome}')