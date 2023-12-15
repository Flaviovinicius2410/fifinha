import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Adicionando critério de desempate usando idade, potencial, hits e potencial máximo
top_15_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(15, ['overall', 'age', 'potential', 'hits'])

# Calculando o potencial atual, potencial máximo, a diferença de potencial e a idade invertida
current_potential = top_15_players['potential']
max_potential = top_15_players.groupby('name')['potential'].transform('max')
potential_diff = current_potential - top_15_players['overall']
inverse_age = 1 / top_15_players['age']

# Definindo cores com base na diferença de potencial
colors = np.where(potential_diff >= 0, 'green', 'orange')

# Ordenando a tabela dos melhores 15 jogadores do maior para o menor
top_15_players = top_15_players.sort_values(by=['overall', 'age', 'potential', 'hits'], ascending=[False, True, False, False])

# Gráfico dos 15 melhores jogadores usando o critério de desempate
fig, (ax_overall, ax_diff_potential) = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico de barras para Overall
ax_overall.barh(top_15_players['name'], top_15_players['overall'], color='green')
ax_overall.set_ylabel('Jogadores')
ax_overall.set_xlabel('Pontuação Overall')
ax_overall.set_title('Top 15 Jogadores - Overall')
ax_overall.invert_yaxis()  # Inverte a ordem dos jogadores

# Gráfico de barras para Diferença de Potencial
ax_diff_potential.barh(top_15_players['name'], potential_diff, color=colors)
ax_diff_potential.set_ylabel('Jogadores')
ax_diff_potential.set_xlabel('Diferença de Potencial')
ax_diff_potential.set_title('Top 15 Jogadores - Diferença de Potencial')
ax_diff_potential.invert_yaxis()  # Inverte a ordem dos jogadores

# Exibir os gráficos dos 15 melhores jogadores
st.pyplot(fig)

# Gráfico dos 10 melhores jogadores brasileiros
st.subheader("Top 10 Melhores Jogadores Brasileiros:")
top_10_brazilian_players = df[df['nationality'] == 'Brazil'].nlargest(10, 'overall')
fig_top_10_brazilian_players, ax_top_10_brazilian_players = plt.subplots()
ax_top_10_brazilian_players.barh(top_10_brazilian_players['name'][::-1], top_10_brazilian_players['overall'][::-1], color='green')
ax_top_10_brazilian_players.set_ylabel('Jogadores')
ax_top_10_brazilian_players.set_xlabel('Pontuação Overall')
ax_top_10_brazilian_players.set_title('Top 10 Melhores Jogadores Brasileiros')
st.pyplot(fig_top_10_brazilian_players)

# Gráfico dos 10 piores jogadores brasileiros
st.subheader("Top 10 Piores Jogadores Brasileiros:")
bottom_10_brazilian_players = df[df['nationality'] == 'Brazil'].nsmallest(10, 'overall')
fig_bottom_10_brazilian_players, ax_bottom_10_brazilian_players = plt.subplots()
ax_bottom_10_brazilian_players.barh(bottom_10_brazilian_players['name'][::-1], bottom_10_brazilian_players['overall'][::-1], color='red')
ax_bottom_10_brazilian_players.set_ylabel('Jogadores')
ax_bottom_10_brazilian_players.set_xlabel('Pontuação Overall')
ax_bottom_10_brazilian_players.set_title('Top 10 Piores Jogadores Brasileiros')
st.pyplot(fig_bottom_10_brazilian_players)