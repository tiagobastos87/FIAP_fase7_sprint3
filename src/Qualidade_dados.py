# controle_qualidade.py
import pandas as pd
import numpy as np

def verificar_qualidade_dados(dataset):
    """Realiza verificações de qualidade nos dados"""

    print("=== RELATÓRIO DE QUALIDADE DOS DADOS ===")

    # 1. Verificar valores ausentes
    print("\n1. VALORES AUSENTES:")
    valores_ausentes = dataset.isnull().sum()
    print(valores_ausentes)

    # 2. Verificar duplicatas
    print(f"\n2. DUPLICATAS: {dataset.duplicated().sum()}")

    # 3. Estatísticas descritivas
    print("\n3. ESTATÍSTICAS DESCRITIVAS:")
    print(dataset.describe())

    # 4. Verificar outliers (método IQR)
    print("\n4. DETECÇÃO DE OUTLIERS:")
    colunas_numericas = dataset.select_dtypes(include=[np.number]).columns

    for coluna in colunas_numericas:
        if coluna not in ['year', 'ano']:
            Q1 = dataset[coluna].quantile(0.25)
            Q3 = dataset[coluna].quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR

            outliers = dataset[
                (dataset[coluna] < limite_inferior) |
                (dataset[coluna] > limite_superior)
                ]

            print(f"   {coluna}: {len(outliers)} outliers detectados")

    # 5. Verificar consistência temporal
    print("\n5. CONSISTÊNCIA TEMPORAL:")
    anos_esperados = [2021, 2022]
    anos_presentes = sorted(dataset['year'].unique())
    print(f"   Anos esperados: {anos_esperados}")
    print(f"   Anos presentes: {anos_presentes}")
    print(f"   Consistente: {anos_esperados == anos_presentes}")

    return True

# Executar controle de qualidade
if __name__ == "__main__":
    dataset = pd.read_csv('dataset_integrado_final.csv')
    verificar_qualidade_dados(dataset)
