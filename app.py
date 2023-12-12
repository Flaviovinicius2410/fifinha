import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Adicionando gráfico de barras para os 50 melhores jogadores
st.subheader("Top 50 Jogadores - Gráfico de Barras:")
# Adicionando critério de desempate usando idade, potencial e hits
top_50_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(50, ['overall', 'age', 'potential', 'hits'])
fig, ax = plt.subplots()
ax.barh(top_50_players['name'], top_50_players['overall'], color='green')
ax.set_xlabel('Overall')
ax.set_ylabel('Jogadores')
ax.set_title('Top 50 Jogadores')
st.pyplot(fig)