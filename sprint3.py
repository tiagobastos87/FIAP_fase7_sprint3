import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Leitura dos dados do arquivo CSV
df = pd.read_csv('E:/SPRINT3/data/dados_mogi_mirim_cafe_talhoes_2023_2024.csv')

# 2. Análise de correlação
pearson_corr, pearson_p = pearsonr(df['ndvi_medio'], df['produtividade_real'])
spearman_corr, spearman_p = spearmanr(df['ndvi_medio'], df['produtividade_real'])

# 3. Regressão linear simples
X = df['ndvi_medio'].values.reshape(-1, 1)
y = df['produtividade_real'].values
reg = LinearRegression().fit(X, y)
y_pred = reg.predict(X)
r2 = r2_score(y, y_pred)

# 4. Interpretação da correlação
def interpretar_correlacao(r):
    if r >= 0.7:
        return 'Correlação forte'
    elif r >= 0.4:
        return 'Correlação moderada'
    elif r > 0:
        return 'Correlação fraca'
    else:
        return 'Correlação negativa ou inexistente'

interpretacao_pearson = interpretar_correlacao(abs(pearson_corr))
interpretacao_spearman = interpretar_correlacao(abs(spearman_corr))

# 5. Resultados
print(f'Correlação de Pearson: {pearson_corr:.3f} (p-valor: {pearson_p:.2e}) - {interpretacao_pearson}')
print(f'Correlação de Spearman: {spearman_corr:.3f} (p-valor: {spearman_p:.2e}) - {interpretacao_spearman}')
print(f'Equação da tendência: y = {reg.coef_[0]:.2f}*NDVI + {reg.intercept_:.2f}')
print(f'Coeficiente de determinação R²: {r2:.3f}')

# 6. Gráfico de dispersão com linha de tendência
plt.figure(figsize=(8,6))
sns.scatterplot(x='ndvi_medio', y='produtividade_real', data=df, color='blue', label='Dados reais')
plt.plot(df['ndvi_medio'], y_pred, color='red', label='Linha de tendência')
plt.xlabel('NDVI Médio')
plt.ylabel('Produtividade Real (t/ha)')
plt.title('Relação entre NDVI Médio e Produtividade Real do Café em Mogi Mirim (SP)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('ndvi_vs_produtividade_cafe_mogi_mirim.png', dpi=150)
plt.show()

# 7. Gráfico comparativo por região e safra
dados_comparativo = {
    'regiao': ['Mogi Mirim', 'Mogi Mirim', 'Campinas', 'Campinas'],
    'safra': ['2022/2023', '2023/2024', '2022/2023', '2023/2024'],
    'produtividade_real': [1.60, 1.61, 1.55, 1.58]
}
df_comp = pd.DataFrame(dados_comparativo)

plt.figure(figsize=(8,6))
sns.barplot(x='regiao', y='produtividade_real', hue='safra', data=df_comp)
plt.title('Produtividade Real do Café por Região e Safra')
plt.ylabel('Produtividade Real (t/ha)')
plt.xlabel('Região')
plt.tight_layout()
plt.show()