import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Página explicativa
st.write("# Análise de Jogadores do FIFA")

st.write("Esta análise explora dados sobre jogadores do FIFA. Abaixo estão detalhes sobre cada coluna:")

# Explicação de cada coluna
st.write("- **player_id**: Identificador único para cada jogador.")
st.write("- **name**: Nome do jogador.")
st.write("- **nationality**: Nacionalidade do jogador.")
st.write("- **position**: Posição ou posições que o jogador ocupa.")
st.write("- **overall**: Pontuação geral do jogador, indicando seu desempenho global.")
st.write("- **age**: Idade do jogador.")
st.write("- **hits**: Número de 'hits' ou popularidade do jogador.")
st.write("- **potential**: Potencial futuro do jogador.")
st.write("- **team**: Time ao qual o jogador pertence.")

# Gráfico de distribuição de jogadores por posição pura em um gráfico de barras
st.write("## Jogadores Por Posições:")
fig, ax = plt.subplots()
pure_positions = df['position'].str.split('|', expand=True).stack().value_counts()
pure_positions.sort_values().plot(kind='barh', ax=ax, color='skyblue')
ax.set_xlabel('Contagem de Jogadores')
ax.set_ylabel('Posição Geral')
ax.set_title('Posições dos jogadores')
st.pyplot(fig)

# Adicionando critério de desempate usando idade, potencial, hits e potencial máximo
top_15_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(15, ['overall', 'age', 'potential', 'hits'])

# ...

# Restante do código (gráficos, tabelas, etc.)