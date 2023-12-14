import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("train.csv")

# Fonte dos Dados
st.write("## Fonte dos Dados")
st.write("JOGADORES DO FIFA")
# Visão Geral
st.write("## Visão Geral")
st.write("Escolhi essa base de dados do ano de 2021 para estudar os dados que fazem um jogador ser considerado um dos melhores do munndo quanto ourtro um dos piores")
st.write("Essa base tem como informação o overall atual dos jogadores, seu possivel potencial junto a idade e hits de cada jogador")

# Estrutura do Conjunto de Dados
st.write("## Estrutura do Conjunto de Dados")
st.write(f"- **Número de Linhas (Amostras):** {df.shape[0]}")
st.write(f"- **Número de Colunas (Variáveis):** {df.shape[1]}")

# Colunas Principais
st.write("## Colunas Principais")
for col in df.columns:
    st.write(f"{col}: {df[col].nunique()} valores únicos")

# Análise Exploratória
st.write("## Análise Exploratória")

# Display an interactive data table
st.write("### Visualização da Tabela de Dados")
st.dataframe(df)
df = pd.read_csv("train.csv", delimiter=";")

# Gráfico de distribuição de jogadores por pontuação "Overall"
st.write("### Distribuição de Jogadores por Pontuação Overall")
overall_chart = alt.Chart(df).mark_bar().encode(
    x='overall:O',
    y='count()',
    color='overall:N'
).properties(
    title="Distribuição de Jogadores por Pontuação Overall",
    width=600
)
st.altair_chart(overall_chart, use_container_width=True)