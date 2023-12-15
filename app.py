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

# Critério de desempate final usando hits
top_15_players = top_15_players.sort_values(by=['overall', 'age', 'potential', 'hits'], ascending=[False, True, False, False])

# Definindo cores com base na diferença de potencial
colors = np.where(potential_diff >= 0, 'green', 'orange')

# Criando as tabelas
table_overall = pd.DataFrame({
    'Nome': top_15_players['name'],
    'Overall': top_15_players['overall'],
    'Potencial Máximo': max_potential,
    'Idade Invertida': inverse_age
})

table_diff_potential = pd.DataFrame({
    'Nome': top_15_players['name'],
    'Diferença de Potencial': potential_diff
})

# Configurando a página com uma coluna
col1, col2 = st.columns(2)

# Exibir as tabelas na mesma coluna
col1.write("### Tabela de Overall:")
col1.write(table_overall)
col2.write("### Tabela de Diferença de Potencial:")
col2.write(table_diff_potential)

# Gráfico de barras para Overall na terceira coluna
st.subheader("Gráfico - Top 15 Jogadores - Overall:")
fig_overall, ax_overall = plt.subplots(figsize=(6, 6))
ax_overall.barh(top_15_players['name'], top_15_players['overall'], color='green')
ax_overall.set_ylabel('Jogadores')
ax_overall.set_xlabel('Pontuação Overall')
ax_overall.set_title('Top 15 Jogadores - Overall')
ax_overall.invert_yaxis()  # Inverte a ordem dos jogadores
st.pyplot(fig_overall)

# Gráfico de barras para Diferença de Potencial na quarta coluna
st.subheader("Gráfico - Top 15 Jogadores - Diferença de Potencial:")
fig_diff_potential, ax_diff_potential = plt.subplots(figsize=(6, 6))
ax_diff_potential.barh(top_15_players['name'], potential_diff, color=colors)
ax_diff_potential.set_ylabel('Jogadores')
ax_diff_potential.set_xlabel('Diferença de Potencial')
ax_diff_potential.set_title('Top 15 Jogadores - Diferença de Potencial')
ax_diff_potential.invert_yaxis()  # Inverte a ordem dos jogadores
st.pyplot(fig_diff_potential)