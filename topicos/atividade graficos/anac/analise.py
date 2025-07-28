import pandas as pd
import matplotlib.pyplot as plt


def media_por_mes():
    medias_tarifa = []
    for i in range(4):
        caminho = f'topicos/atividade graficos/anac/20250{i+1}.CSV'
        dataset = pd.read_csv(caminho,sep=';')
        dataset.columns =[ 'ANO','MES','EMPRESA','ORIGEM','DESTINO','TARIFA','ASSENTOS']
        dataset['TARIFA'] = dataset['TARIFA'].astype(str).str.replace(',','.').astype(float)
        media_mes = round(dataset['TARIFA'].mean(),2)
        medias_tarifa.append(media_mes)

    return medias_tarifa


print(media_por_mes())
plt.bar(['Janeiro','Fevereiro','Março','Abril'],media_por_mes(),color='red')
plt.show() 
    

# grafico para mostrar as os lucros por empresa no ano de 2025

def lucro_por_empresa():
    lucro_por_empresa = {}
    for i in range(4):
        caminho = f'topicos/atividade graficos/anac/20250{i+1}.CSV'
        dataset = pd.read_csv(caminho,sep=';')
        dataset.columns =[ 'ANO','MES','EMPRESA','ORIGEM','DESTINO','TARIFA','ASSENTOS']
        dataset['TARIFA'] = dataset['TARIFA'].astype(str).str.replace(',','.').astype(float)
        empresa = dataset['EMPRESA'].unique()
        for i in empresa:
            if i not in lucro_por_empresa:
                lucro_por_empresa[str(i)] = dataset['TARIFA'].sum()
            else:
                lucro_por_empresa[str(i)] += dataset['TARIFA'].sum()
       
    

