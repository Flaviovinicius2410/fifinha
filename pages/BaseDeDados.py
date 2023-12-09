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
st.write("Os dados do Titanic foram obtidos do Kaggle, disponíveis no seguinte link:")
st.write("[Titanic - Kaggle](https://www.kaggle.com/c/titanic/data)")

# Visão Geral
st.write("## Visão Geral")
st.write("O conjunto de dados do Titanic é amplamente utilizado para análises exploratórias e modelagem preditiva.")
st.write("Ele contém informações sobre os passageiros a bordo do Titanic, incluindo detalhes sobre sobrevivência, classe, sexo, idade, número de irmãos/cônjuges a bordo, número de pais/filhos a bordo, tarifa, entre outros.")

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

# Display a bar chart showing the distribution of passengers by survival status
st.write("### Distribuição de Passageiros por Sobrevivência")
survival_chart = alt.Chart(df).mark_bar().encode(
    x='Survived:O',
    y='count()',
    color='Survived:N'
).properties(
    title="Distribuição de Passageiros por Sobrevivência",
    width=600
)
st.altair_chart(survival_chart, use_container_width=True)

# Display a link to the pandas profiling report
st.write("### Link para o Relatório de Perfil do Conjunto de Dados")
st.markdown("[Download do Relatório de Perfil](sandbox:/path/to/train.csv)")

# Conclusão
st.write("## Conclusão")
st.write("Este documento fornece uma visão geral do conjunto de dados do Titanic, incluindo suas fontes, estrutura e principais colunas.")
st.write("A análise exploratória detalhada, incluindo visualizações interativas, pode revelar insights valiosos sobre os eventos que ocorreram a bordo do Titanic.")