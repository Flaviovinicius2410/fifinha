import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
# Exibe uma tabela com informações específicas sobre os jogadores
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

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

# Gráfico de barras para Overall e Diferença de Potencial
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

# Exibir tabela de Overall, Diferença de Potencial, Potencial Máximo e Idade Invertida
st.write("### Tabela de Overall, Diferença de Potencial, Potencial Máximo e Idade Invertida:")
# Cria uma tabela com informações sobre os 15 melhores jogadores
potentials_table = pd.DataFrame({
    'Nome': top_15_players['name'],
    'Overall': top_15_players['overall'],
    'Diferença de Potencial': potential_diff,
    'Potencial Máximo': max_potential,
    'Idade Invertida': inverse_age
})
st.write(potentials_table)

# Mostrar os gráficos
st.pyplot(fig)