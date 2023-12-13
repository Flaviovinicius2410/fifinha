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
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Filtrar apenas as posições puras
pure_positions = df['position'].str.split('|', expand=True).stack().value_counts()

# Gráfico de distribuição de jogadores por posição pura em um gráfico de barras
st.subheader("Jogadores Por Posições:")
fig, ax = plt.subplots()
pure_positions.sort_values().plot(kind='barh', ax=ax, color='skyblue')
ax.set_xlabel('Contagem de Jogadores')
ax.set_ylabel('Posição Geral')
ax.set_title('Posições dos jogadores')
st.pyplot(fig)

# Adicionando gráfico de barras para os 15 melhores jogadores
st.subheader("Top 15 Jogadores - Gráfico de Barras:")
# Adicionando critério de desempate usando idade, potencial e hits
top_15_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(15, ['overall', 'age', 'potential', 'hits'])
fig, ax = plt.subplots()

# Gráfico de barras para o Overall
bar_width = 0.5
bar_spacing = 1  # Espaçamento entre as barras
names_with_spacing = top_15_players['name'] + ' ' + (np.arange(len(top_15_players)) * bar_spacing).astype(str)
ax.barh(names_with_spacing, top_15_players['overall'], color='green', height=bar_width, label='Overall')
ax.set_xlabel('Pontuação')
ax.set_ylabel('Jogadores')
ax.set_title('Top 15 Jogadores - Overall')
ax.legend()
ax.invert_yaxis()  # Inverte a ordem dos jogadores

# Exibir tabela de Overall
st.write("### Tabela de Overall:")
st.write(top_15_players[['name', 'overall']])

# Gráfico de barras para o Potencial Total
fig, ax = plt.subplots()
ax.barh(names_with_spacing, top_15_players['potential'], color='orange', height=bar_width, label='Potencial')
ax.set_xlabel('Pontuação')
ax.set_ylabel('Jogadores')
ax.set_title('Top 15 Jogadores - Potencial Total')
ax.legend()
ax.invert_yaxis()  # Inverte a ordem dos jogadores

# Exibir tabela de Potencial
st.write("### Tabela de Potencial Total:")
st.write(top_15_players[['name', 'potential']])

# Mostrar os gráficos
st.pyplot(fig)