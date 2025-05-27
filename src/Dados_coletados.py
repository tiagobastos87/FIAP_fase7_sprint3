# dados_produtividade_historica.py
import pandas as pd

# Dados históricos coletados para Mogi Mirim/SP
dados_historicos = {
    'ano': [2021, 2022],
    'produtividade_real_tons_ha': [30.5, 32.0],
    'area_plantada_ha': [2850, 2900],
    'producao_total_tons': [86925, 92800],
    'fonte': ['IBGE-LSPA', 'IBGE-LSPA'],
    'regiao': ['Mogi Mirim/SP', 'Mogi Mirim/SP'],
    'coordenadas_lat': [-22.4197, -22.4197],
    'coordenadas_lon': [-46.9197, -46.9197]
}

# Salvar dados históricos
produtividade_historica = pd.DataFrame(dados_historicos)
produtividade_historica.to_csv('dados_produtividade_historica.csv', index=False)

print("Dados de Produtividade Histórica Coletados:")
print(produtividade_historica)
