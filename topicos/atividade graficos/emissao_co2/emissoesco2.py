import matplotlib.pyplot as plt

import pandas as pd



emissoes = pd.read_csv('topicos/atividade graficos/emissao_co2/frame.csv')

#filtrando datset
emissoes.fillna(0, inplace=True)

emissoes['year'] = pd.to_datetime(emissoes['date'],format='%d/%m/%Y')
#pegando somente o ano de cada linha
emissoes['year'] = emissoes['year'].dt.year

# media de 2019
ano_2019 = emissoes.query('year == 2019')
media_2019 = round(ano_2019['value'].mean(),4)
print(media_2019)

#media de 2020
ano_2020 = emissoes.query('year == 2020')
media_2020 = round(ano_2020['value'].mean(),4)
print(media_2020)

#media 2021
ano_2021 = emissoes.query('year == 2021')
media_2021 = round(ano_2021['value'].mean(),4)
print(media_2021)

#media 2022
ano_2022 = emissoes.query('year == 2022')
media_2022 = round(ano_2022['value'].mean(),4)
print(media_2022)

#media 2023
ano_2023 = emissoes.query('year == 2023')
media_2023 = round(ano_2023['value'].mean(),4)
print(media_2023)

y = [media_2019,media_2020,media_2021,media_2022,media_2023]
x2 = ['2019','2020','2021','2022','2023']


#grafico nde ponto que mostra a media de emissao por ano
plt.plot(x2,y,color='g')
plt.xlabel('Ano')
plt.ylabel('Valor')
plt.title('Média de emissão de co2 por ano')

plt.show()


#emissoes por categoria
emissoes_por_categotias = []
secoes = emissoes['sector'].unique()
print(secoes)
for i in secoes:
    new_section = emissoes.query(f"sector == '{i}'") # retorna somente a coluna de cada seção 
    emissoes_por_categotias.append(round(new_section['value'].mean(),2))# adicona a media dos valores de cada coluna numa lista
print(emissoes_por_categotias)


plt.bar(secoes,emissoes_por_categotias)
plt.title('Média de emissão por setor')
plt.xlabel('Seções',size=15)
plt.ylabel('Valores',size=15)
plt.xticks(rotation=45, ha='right', fontsize=12)# Ajustando a rotação dos rótulos do eixo X
plt.tight_layout()# Ajusta o layout para evitar sobreposição
plt.show()

