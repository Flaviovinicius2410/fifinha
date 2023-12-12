import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

# Informações sobre jogadoresS
st.subheader("Informações sobre Jogadores:")
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Filtrar apenas as posições puras
pure_positions = df['position'].str.split('|', expand=True).stack().value_counts()

# Gráfico de distribuição percentual de jogadores por posição pura
st.subheader("Distribuição Percentual de Jogadores por Posição Pura:")
fig, ax = plt.subplots()
ax.pie(pure_positions, labels=pure_positions.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Assegura que o gráfico de pizza seja circular
st.pyplot(fig)

# Gráfico de distribuição de idades
st.subheader("Distribuição de Idades:")
st.hist(df['age'], bins=20, edgecolor='black')
st.xlabel('Idade')
st.ylabel('Contagem')
st.title('Distribuição de Idades dos Jogadores')
st.pyplot()