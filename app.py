import streamlit as st
import pandas as pd

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Gráfico de contagem de jogadores por posição
st.subheader("Contagem de Jogadores por Posição:")
# Usando explode() para lidar com valores separados por '|'
position_counts = df['position'].explode().value_counts()
st.bar_chart(position_counts)

# Gráfico de distribuição de idades
st.subheader("Distribuição de Idades:")
st.hist(df['age'], bins=20, edgecolor='black')
st.xlabel('Idade')
st.ylabel('Contagem')
st.title('Distribuição de Idades dos Jogadores')
st.pyplot()