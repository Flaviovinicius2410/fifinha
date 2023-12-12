import streamlit as st
import pandas as pd

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("train.csv")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
st.write(df[['name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])


# Gráfico de contagem de jogadores por posição
st.subheader("Contagem de Jogadores por Posição:")
position_counts = df['position'].str.split('|', expand=True).stack().value_counts()
df.bar(position_counts.index, position_counts.values)
df.xlabel('Posição')
df.ylabel('Contagem')
df.title('Contagem de Jogadores por Posição')
st.pyplot()

# Gráfico de distribuição de idades
st.subheader("Distribuição de Idades:")
df.hist(df['age'], bins=20, edgecolor='black')
df.xlabel('Idade')
df.ylabel('Contagem')
df.title('Distribuição de Idades dos Jogadores')
st.pyplot()
