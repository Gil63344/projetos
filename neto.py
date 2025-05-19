import numpy as np

np.random.seed(42)

ids = np.arange(1,11)
preco = np.random.randint(500,2000,size=10)
vendas_a = np.random.randint(50,500,size=10)
vendas_b = np.random.randint(50,500,size=10)
custo = np.random.randint(50,200,size=10)

dataset = np.column_stack((ids,preco,vendas_a,vendas_b,custo ))



def MediaVendasRegioes(dataset):

    Media_A = round(np.mean([venda[2] for venda in dataset]),2)
    Media_B = round(np.mean([venda[3] for venda in dataset]),2)

    return Media_A,Media_B


def TotalVendasRegioes(dataset):

    Total_A = np.sum([venda[2] for venda in dataset])
    Total_B = np.sum([venda[3] for venda in dataset])

    return Total_A,Total_B

def ValorMaximoMinimoDeCadaColuna(dataset):

    valores_maximos = np.argmax(dataset,axis=0)
    valores_minimos = np.argmin(dataset,axis=0)

    return valores_maximos,valores_minimos

def FaturamentoRegioes(dataset):

    Total_A = round(np.sum([venda[1] * venda[2] for venda in dataset]),2)
    Total_B = round(np.sum([venda[1] * venda[3] for venda in dataset]),2)


    return Total_A,Total_B


print(dataset[:5])
print()
print(MediaVendasRegioes(dataset=dataset))
print()
print(TotalVendasRegioes(dataset))
print()
print(ValorMaximoMinimoDeCadaColuna(dataset=dataset))
print()
print(FaturamentoRegioes(dataset=dataset))