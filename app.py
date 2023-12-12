import streamlit as st
import pandas as pd

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("train.csv")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

st.write("Conteúdo do DataFrame:", df.head())
# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
st.write(df[['player_id','name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Gráfico de contagem de jogadores por posição
st.subheader("Contagem de Jogadores por Posição:")
position_counts = df['position'].str.split('|', expand=True).stack().value_counts()
st.bar_chart(position_counts)  # Corrigido para st.bar_chart

# Gráfico de distribuição de idades
st.subheader("Distribuição de Idades:")
st.hist(df['age'], bins=20, edgecolor='black')  # Corrigido para st.hist
st.xlabel('Idade')
st.ylabel('Contagem')
st.title('Distribuição de Idades dos Jogadores')
st.pyplot()