# preparacao_analise.py
import pandas as pd
import numpy as np

def preparar_variaveis_analise(dataset):
    """Prepara variáveis para análise estatística"""

    # Selecionar variáveis para análise
    variaveis_analise = [
        'year',
        'ndvi_medio',
        'ndvi_maximo',
        'ndvi_minimo',
        'ndvi_amplitude',
        'coef_variacao_ndvi',
        'produtividade_real_tons_ha',
        'area_plantada_ha',
        'producao_total_tons'
    ]

    dataset_analise = dataset[variaveis_analise].copy()

    # Criar variáveis derivadas se necessário
    dataset_analise['produtividade_normalizada'] = (
            (dataset_analise['produtividade_real_tons_ha'] -
             dataset_analise['produtividade_real_tons_ha'].mean()) /
            dataset_analise['produtividade_real_tons_ha'].std()
    )

    dataset_analise['ndvi_normalizado'] = (
            (dataset_analise['ndvi_medio'] -
             dataset_analise['ndvi_medio'].mean()) /
            dataset_analise['ndvi_medio'].std()
    )

    return dataset_analise

def gerar_relatorio_preparacao(dataset_analise):
    """Gera relatório da preparação dos dados"""

    print("=== RELATÓRIO DE PREPARAÇÃO DOS DADOS ===")

    print(f"\nDataset final preparado com {len(dataset_analise)} observações")
    print(f"Variáveis disponíveis: {len(dataset_analise.columns)}")

    print("\nVariáveis e tipos:")
    for col in dataset_analise.columns:
        print(f"  {col}: {dataset_analise[col].dtype}")

    print("\nEstatísticas das variáveis principais:")
    variaveis_principais = ['ndvi_medio', 'ndvi_maximo', 'produtividade_real_tons_ha']
    print(dataset_analise[variaveis_principais].describe())

    return True

# Executar preparação
if __name__ == "__main__":
    dataset = pd.read_csv('dataset_integrado_final.csv')
    dataset_analise = preparar_variaveis_analise(dataset)

    # Salvar dataset preparado para análise
    dataset_analise.to_csv('dataset_preparado_analise.csv', index=False)

    gerar_relatorio_preparacao(dataset_analise)
