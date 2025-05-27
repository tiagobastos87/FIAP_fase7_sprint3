import pandas as pd
import numpy as np
from datetime import datetime

def carregar_dados():
    """Carrega todos os datasets necessários"""
    ndvi_clean = pd.read_csv('ndvi_clean.csv')
    ndvi_clean['date'] = pd.to_datetime(ndvi_clean['date'])
    prod_historica = pd.read_csv('dados_produtividade_historica.csv')
    print("Dados carregados com sucesso.")
    return ndvi_clean, prod_historica

def agregar_ndvi_anual(ndvi_clean):
    """Agrega dados NDVI por ano"""
    ndvi_clean['year'] = ndvi_clean['date'].dt.year
    ndvi_anual = ndvi_clean.groupby('year').agg({
        'ndvi': ['mean', 'max', 'min', 'std']
    }).round(4)
    ndvi_anual.columns = ['ndvi_medio', 'ndvi_maximo', 'ndvi_minimo', 'ndvi_desvio']
    ndvi_anual = ndvi_anual.reset_index().dropna()
    print(f"NDVI anual: {ndvi_anual.shape}")
    return ndvi_anual

def criar_dataset_integrado(ndvi_anual, prod_historica):
    """Cria dataset integrado para análise"""
    prod_historica = prod_historica.dropna()
    assert 'year' in ndvi_anual.columns, "Coluna 'year' não encontrada em ndvi_anual"
    assert 'ano' in prod_historica.columns, "Coluna 'ano' não encontrada em prod_historica"
    dataset_final = pd.merge(
        ndvi_anual,
        prod_historica,
        left_on='year',
        right_on='ano',
        how='inner'
    )
    dataset_final['ndvi_amplitude'] = dataset_final['ndvi_maximo'] - dataset_final['ndvi_minimo']
    dataset_final['coef_variacao_ndvi'] = dataset_final['ndvi_desvio'] / dataset_final['ndvi_medio']
    print(f"Dataset integrado: {dataset_final.shape}")
    return dataset_final

if __name__ == "__main__":
    ndvi_clean, prod_historica = carregar_dados()
    ndvi_anual = agregar_ndvi_anual(ndvi_clean)
    dataset_integrado = criar_dataset_integrado(ndvi_anual, prod_historica)
    dataset_integrado.to_csv('dataset_integrado_final.csv', index=False)
    print("\nDataset Integrado Final (top 5):")
    print(dataset_integrado.head())
