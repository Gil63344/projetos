import pandas as pd 

datafram = pd.read_csv('topicos/gil/status-pagamento.csv',sep=';',encoding='utf-8')

print(datafram.head())