import pandas as pd 
from datetime import *



carros = pd.read_csv('carros.csv',sep=';')
carros.fillna(0, inplace=True)
ano = datetime.now().year

def linhas():
    print('*'*50)
    

def mediakm(dataset,ano):
    dataset['Km_media'] = dataset['Quilometragem'] / (ano - dataset['Ano'])
    print(f"Carros com suas respectivas media de km:\n{dataset[['Nome','Km_media']].head()}\n")
    linhas()
    print(f"Quantidade de carros 0km:\n{dataset['Km_media'].isnull().sum()}\n")
    linhas()
    


def analisar_frame(dataset):
    #mostrar dataset
    df = dataset
    

    print(f'{df.head()}\n')
    linhas()
    #mostre os tipos de dados do dataset: comando: dtypes. Quais os tipos de dados das colunas deste dataset?
    print(f'{df.dtypes}\n')
    linhas()

    # mostre a estatística descritiva das colunas: quilometragem e valor. Qual o significado dessas informações?
    print(f"{df[['Quilometragem','Valor']].describe()}\n")
    linhas()

    #Obtenha mais informações do dataset com a função info(). Tem alguma coluna com dados nulos? Se sim, qual a coluna e quantos  dados nulos possui?
    print(f'{df.info()}\n')
    linhas()

    print(f'Quantidade de valores nulos por colunas:\n{df.isnull().sum()}')
    linhas()

    

def carros_com_motorv8(dataset):
   # mostre os carros com motor "Diesel V8"
   print('carros com motor "Diesel V8":')
   print(dataset.query("Motor == 'Motor Diesel V8'"))


def carros_1_8v_usado_preco_100000(dataset):
    #pesquise por carros com motor 1.0 8v usados com preço inferior a R$ 100.000
    print('Carros commotor 1.0 8v, usados com preço menor que R$ 100,000::')
    print(dataset.query('Motor == "Motor 1.0 8v" and Zero_km == False and Valor < 100000'))

def carros_km_10000_motor_18(dataset):
    #pesquise por carros com km média de até 10.000 km com Motor 1.8 16v
    print('Carros com km media de ate 10.000km com motor 1.8 16v:')
    print(dataset.query('Km_media <= 10000 and Motor == "Motor 1.8 16v"'))


def lista_motores_cadastrados(dataset):
    tipo_motores = (dataset['Motor'].unique())
    print('Listas de motores cadastrados:')
    for i in tipo_motores:
        print(i)

def  carros_automático_abaixo_100000(dataset):
    print(' liste os carros com câmbio automático com valor abaixo de R$ 100.000 :')
    print(dataset.query('Valor < 100000 and Acessórios.str.contains("Câmbio automático")'))


def carros_novos_freios_ABS_acima_100000(dataset):
    print('Liste os carros novos com "freios ABS" que custam acima de R$ 100.000 :')
    print(dataset.query('Valor > 100000 and Acessórios.str.contains("Freios ABS") and Zero_km == True'))


def carros_novos_usados_km_média_abaixo_10000_km_ate_100000(dataset):
    print(' liste os carros novos ou usados com km média abaixo de 10.000 km que custam até R$ 100.000')
    print(dataset.query('Km_media < 10000 and Valor <= 100000'))





analisar_frame(carros)
print(ano)

linhas()
mediakm(carros,ano)
linhas()
carros_com_motorv8(carros)
linhas()
carros_1_8v_usado_preco_100000(carros)
linhas()
carros_km_10000_motor_18(carros)
linhas()
lista_motores_cadastrados(carros)
carros_automático_abaixo_100000(carros)
linhas()
carros_novos_freios_ABS_acima_100000(carros)
linhas()
carros_novos_usados_km_média_abaixo_10000_km_ate_100000(carros)
linhas()

