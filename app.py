import streamlit as st
import pandas as pd

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("train.csv")

# Adicione uma coluna 'Contagem' ao DataFrame para armazenar a contagem de passageiros
df['Contagem'] = 1

st.title("Dataset - Titanic")

nome = st.text_input("Informe seu nome")
st.write(f"Saudações {nome}!")

# Informação da quantidade de passageiros
st.subheader("Quantidade de Passageiros:")
st.write(f"Total de passageiros: {len(df)}")

# Informação sobre sobreviventes
sobreviventes = df['Survived'].sum()
nao_sobreviventes = len(df) - sobreviventes

st.subheader("Sobreviventes:")
st.write(f"Passageiros que sobreviveram: {sobreviventes}")

st.subheader("Não Sobreviventes:")
st.write(f"Passageiros que não sobreviveram: {nao_sobreviventes}")

# Outras informações
'''
Hoje irei mostrar todos os gráficos referentes ao dataset de pesquisas
envolvendo o Titanic, como Sobreviveu, Pclass, Nome, Sexo, Idade, SibSp, Parch, Bilhete, Tarifa, Cabine, Embarcado.

Clicando ao lado será possível visualizar o modelo grafico.
'''