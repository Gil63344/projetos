import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('topicos/atividade graficos/carros/carros.csv',sep=';')
df.fillna(0, inplace= True)


quantidades_carros = df.shape[0] #quantidade total de carros
quantidades_carros_zeros = df[df['Zero_km'] == True].shape[0] # aquantidade de carros 0km
print(quantidades_carros)
print(quantidades_carros_zeros)

x2 = ['carros usados','carros zero km']
# grafico de pizza mostando a relaçao de carros novos para carros usados
plt.pie([quantidades_carros-quantidades_carros_zeros,quantidades_carros_zeros],labels=x2)
plt.title('Quantidade de carros/ Zero km')
plt.show()


# carros de maior que ano 2000 em relaçao a carros novos acima de 2000

carrosAcima2000 = df.query('Ano >= 2000').shape[0] #quantidade de carros acima dos anos 2000
carrosNovosAcima2000 = df.query('Ano >= 2000 and Zero_km == True').shape[0] # quntidade de carros > 2000 e novos
carrosUsados2000 = df.query('Ano >= 2000 and Zero_km == False ').shape[0]
print(carrosAcima2000)
print(carrosNovosAcima2000)
print(carrosUsados2000)

plt.barh(['Novos','Usados','Total'],[carrosNovosAcima2000,carrosUsados2000,carrosAcima2000],color='blue')
plt.title('Carros depois do ano 2000 em relação a carros novos acima do mesmo ano',size=6)
plt.xlabel('Quantidade de carros', fontsize=12)
plt.show()


