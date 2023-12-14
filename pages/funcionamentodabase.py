# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
# Exibe uma tabela com informações específicas sobre os jogadores
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Filtrar apenas as posições puras
# Conta a quantidade de jogadores por posição pura
pure_positions = df['position'].str.split('|', expand=True).stack().value_counts()

# Gráfico de distribuição de jogadores por posição pura em um gráfico de barras
st.subheader("Jogadores Por Posições:")
# Cria um gráfico de barras horizontais mostrando a distribuição de jogadores por posição pura
fig, ax = plt.subplots()
pure_positions.sort_values().plot(kind='barh', ax=ax, color='skyblue')
ax.set_xlabel('Contagem de Jogadores')
ax.set_ylabel('Posição Geral')
ax.set_title('Posições dos jogadores')
st.pyplot(fig)

# Adicionando critério de desempate usando idade, potencial, hits e potencial máximo
# Seleciona os 15 melhores jogadores com base nos critérios especificados
top_15_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(15, ['overall', 'age', 'potential', 'hits'])

# Calculando o potencial atual, potencial máximo, a diferença de potencial e a idade invertida
# Calcula algumas métricas adicionais para análise
current_potential = top_15_players['potential']
max_potential = top_15_players.groupby('name')['potential'].transform('max')
potential_diff = current_potential - top_15_players['overall']
inverse_age = 1 / top_15_players['age']

# Definindo cores com base na diferença de potencial
# Atribui cores diferentes dependendo da diferença de potencial ser positiva ou negativa
colors = np.where(potential_diff >= 0, 'green', 'orange')

# Ordenando a tabela dos melhores 15 jogadores do maior para o menor
# Ordena os jogadores com base em múltiplos critérios em ordem decrescente
top_15_players = top_15_players.sort_values(by=['overall', 'age', 'potential', 'hits'], ascending=[False, True, False, False])

# Gráfico de barras com destaque amarelo para a diferença de potencial
# Cria um gráfico de barras horizontais para os 15 melhores jogadores
bar_width = 0.5
bar_spacing = 1  # Espaçamento entre as barras
names_with_spacing = top_15_players['name'] + ' ' + (np.arange(len(top_15_players)) * bar_spacing).astype(str)

fig, ax = plt.subplots()
ax.barh(names_with_spacing, top_15_players['overall'], color='green', height=bar_width, label='Overall')
ax.barh(names_with_spacing, potential_diff, left=top_15_players['overall'].min(), color=colors, height=bar_width, alpha=0.5, label='Diferença de Potencial')

ax.set_xlabel('Pontuação')
ax.set_ylabel('Jogadores')
ax.set_title('Top 15 Jogadores - Overall e Diferença de Potencial')
ax.legend()
ax.invert_yaxis()  # Inverte a ordem dos jogadores

# Exibir tabela de Overall, Diferença de Potencial, Potencial Máximo e Idade Invertida
st.write("### Tabela de Overall, Diferença de Potencial, Potencial Máximo e Idade Invertida:")
# Cria uma tabela com informações sobre os 15 melhores jogadores
potentials_table = pd.DataFrame({
    'Nome': top_15_players['name'],
    'Overall': top_15_players['overall'],
    'Diferença de Potencial': potential_diff,
    'Potencial Máximo': max_potential,
    'Idade Invertida': inverse_age
})
st.write(potentials_table)

# Mostrar o gráfico
st.pyplot(fig)