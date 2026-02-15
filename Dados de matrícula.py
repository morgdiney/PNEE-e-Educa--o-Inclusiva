import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Dados Simulados (Espelhando a realidade do Censo Escolar/INEP)
# Dados aproximados de matrículas na Educação Especial (Classes Comuns + Especiais)
dados_censo = {
    'Ano': [1998, 2002, 2006, 2007, 2008, 2009, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023],
    'Matriculas': [337000, 445000, 700000, 654000, 695000, 752000, 886000, 820000, 880000, 971000, 1180000, 1300000, 1500000, 1600000],
    'Evento_Chave': [
        None, None, None, 'Pré-PNEE 2008', 'PNEE 2008 (Marco)', None, None, 
        None, None, 'LBI 2015', None, 'Decreto 10.502', None, 'Nova PNEE'
    ]
}

df = pd.DataFrame(dados_censo)

# 2. Visualizando a História
plt.figure(figsize=(12, 6))

# Gráfico de Linha com Pontos
sns.lineplot(data=df, x='Ano', y='Matriculas', marker='o', color='navy', linewidth=2.5)

# Adicionando anotações para os eventos legislativos
eventos = df.dropna(subset=['Evento_Chave'])
for i, row in eventos.iterrows():
    plt.annotate(
        row['Evento_Chave'], 
        (row['Ano'], row['Matriculas']),
        xytext=(10, 30), 
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='red'),
        fontsize=10,
        fontweight='bold',
        color='darkred'
    )

plt.title('Evolução das Matrículas da Educação Especial (1998-2023)', fontsize=14)
plt.xlabel('Ano do Censo')
plt.ylabel('Número de Matrículas')
plt.grid(True, linestyle='--', alpha=0.6)

# Formatando o eixo Y para não ficar em notação científica
plt.ticklabel_format(style='plain', axis='y') 

plt.show()

# 1. Preparando os dados para o Scikit-Learn
# O modelo precisa de arrays 2D (formato de tabela)
X = df[['Ano']] # Variável que explica (Tempo)
y = df['Matriculas'] # Variável que queremos prever

# 2. Criando e Treinando o Modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 3. Criando os anos futuros para previsão
anos_futuros = np.array([[2024], [2025], [2026], [2028], [2030]])
previsao = modelo.predict(anos_futuros)

# 4. Juntando Passado e Futuro num gráfico só
plt.figure(figsize=(12, 6))

# Dados Reais (Linha Sólida Azul)
plt.plot(df['Ano'], df['Matriculas'], label='Dados Históricos (Real)', color='blue', marker='o', linewidth=2)

# Previsão (Linha Tracejada Laranja)
# Vamos conectar o último ponto real ao primeiro previsto para ficar bonito
plt.plot(
    np.concatenate([[df['Ano'].iloc[-1]], anos_futuros.flatten()]), 
    np.concatenate([[df['Matriculas'].iloc[-1]], previsao]),
    label='Projeção Tendencial (Se nada mudar)', 
    color='orange', 
    linestyle='--', 
    marker='x',
    linewidth=2
)

plt.title('Projeção de Matrículas: O Cenário Base para a Nova PNEE', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Matrículas (Milhões)')
plt.legend()
plt.grid(True, alpha=0.5)
plt.ticklabel_format(style='plain', axis='y')

# Mostrando os números previstos no console
print("--- PREVISÃO DO MODELO (Cenário Base) ---")
for ano, valor in zip(anos_futuros.flatten(), previsao):
    print(f"Ano {ano}: {int(valor):,} matrículas esperadas".replace(',', '.'))

plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. CRIANDO O CENÁRIO HISTÓRICO (Simulação baseada em tendências do INEP pós-2008)
# Note: Regular sobe, Especializada estagna/cai levemente após 2008
anos_hist = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023]
matr_regular = [400000, 550000, 680000, 750000, 900000, 1100000, 1250000, 1350000]
matr_especializada = [300000, 280000, 250000, 230000, 200000, 190000, 185000, 180000]

df = pd.DataFrame({
    'Ano': anos_hist,
    'Regular': matr_regular,
    'Especializada': matr_especializada
})

# 2. PROJETANDO O FUTURO (Onde sua hipótese entra)
anos_futuros = [2024, 2025, 2026, 2027, 2028, 2030]

# FATOR DE ACELERAÇÃO "SEM LAUDO": 
# Vamos assumir que o crescimento orgânico ganha um "turbo" de 15% ao ano extra pela facilidade
crescimento_base_regular = 1.08 # 8% ao ano (histórico)
fator_sem_laudo = 1.15 # O impacto da nova política (Turbo)

# FATOR DE QUEDA "MIGRAÇÃO":
# Escolas especializadas perdem alunos mais rápido
fator_queda_especializada = 0.90 # Perde 10% ao ano

futuro_regular = []
futuro_especializada = []

# Pegamos os últimos valores de 2023
ultimo_reg = matr_regular[-1]
ultimo_esp = matr_especializada[-1]

for ano in anos_futuros:
    # Cálculo Regular: Crescimento Histórico * Facilidade do Sem Laudo
    novo_valor_reg = ultimo_reg * crescimento_base_regular * fator_sem_laudo
    futuro_regular.append(novo_valor_reg)
    ultimo_reg = novo_valor_reg # Atualiza para o próximo ano (juros compostos)
    
    # Cálculo Especializada: Decaimento
    novo_valor_esp = ultimo_esp * fator_queda_especializada
    futuro_especializada.append(novo_valor_esp)
    ultimo_esp = novo_valor_esp

# 3. VISUALIZANDO O "EFEITO TESOURA"
plt.figure(figsize=(12, 7))

# Plot Histórico (Linhas Sólidas)
plt.plot(df['Ano'], df['Regular'], label='Rede Regular (Histórico)', color='blue', marker='o', linewidth=2)
plt.plot(df['Ano'], df['Especializada'], label='Especializada (Histórico)', color='red', marker='o', linewidth=2)

# Plot Previsão (Linhas Tracejadas)
plt.plot(anos_futuros, futuro_regular, label='Projeção PNEE "Sem Laudo" (Explosão)', color='cyan', linestyle='--', marker='x', linewidth=3)
plt.plot(anos_futuros, futuro_especializada, label='Projeção PNEE (Esvaziamento)', color='orange', linestyle='--', marker='v', linewidth=3)

# Adicionando uma linha vertical para marcar o início da nova política
plt.axvline(x=2023, color='gray', linestyle=':', label='Início Nova PNEE')

plt.title('Impacto da PNEE (Fim da Exigência de Laudo): O Efeito Tesoura', fontsize=14)
plt.ylabel('Número de Matrículas')
plt.xlabel('Ano')
plt.legend()
plt.grid(True, alpha=0.3)
plt.ticklabel_format(style='plain', axis='y') # Remove notação científica

# Anotação Explicativa no Gráfico
plt.annotate('Boom de Acesso\n(Fim da Barreira do Laudo)', 
             xy=(2026, futuro_regular[2]), 
             xytext=(2025, futuro_regular[2] + 500000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, color='blue')

plt.show()