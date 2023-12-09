import streamlit as st
import pandas as pd

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("train.csv")

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
st.write(df[['name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Gráfico de contagem de jogadores por posição
st.subheader("Contagem de Jogadores por Posição:")
position_counts = df['position'].str.split('|', expand=True).stack().value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Posição')
plt.ylabel('Contagem')
plt.title('Contagem de Jogadores por Posição')
st.pyplot()

# Gráfico de distribuição de idades
st.subheader("Distribuição de Idades:")
plt.hist(df['age'], bins=20, edgecolor='black')
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.title('Distribuição de Idades dos Jogadores')
st.pyplot()
