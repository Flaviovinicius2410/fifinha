import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregando o conjunto de dados do Titanic
# Usando ";" como delimitador no read_csv
df = pd.read_csv("train.csv", delimiter=";")

# Imprima as colunas do DataFrame
st.write("Colunas no DataFrame:", df.columns)

# Informações sobre jogadores
st.subheader("Informações sobre Jogadores:")
# Exibe uma tabela com informações específicas sobre os jogadores
st.write(df[['player_id', 'name', 'nationality', 'position', 'overall', 'age', 'hits', 'potential', 'team']])

# Filtrar apenas as posições puras
# Conta a quantidade de jogadores por posição pura
pure_positions = df['position'].str.split('|', expand=True).stack().value_counts()

# Gráfico de distribuição de jogadores por posição pura em um gráfico de barras
st.subheader("Jogadores Por Posições:")
# Cria um gráfico de barras horizontais mostrando a distribuição de jogadores por posição pura
def plot_position_distribution(data):
    fig, ax = plt.subplots()
    data.sort_values().plot(kind='barh', ax=ax, color='skyblue')
    ax.set_xlabel('Contagem de Jogadores')
    ax.set_ylabel('Posição Geral')
    ax.set_title('Posições dos jogadores')
    st.pyplot(fig)

# Adicionando critério de desempate usando idade, potencial, hits e potencial máximo
top_15_players = df[['name', 'overall', 'age', 'potential', 'hits']].nlargest(15, ['overall', 'age', 'potential', 'hits'])

# Calculando o potencial atual, potencial máximo e a diferença de potencial
current_potential = top_15_players['potential']
max_potential = top_15_players.groupby('name')['potential'].transform('max')
potential_diff = current_potential - top_15_players['overall']
inverse_age = 1 / top_15_players['age']

# Definindo cores com base na diferença de potencial
colors = np.where(potential_diff >= 0, 'green', 'orange')

# Ordenando a tabela dos melhores 15 jogadores do maior para o menor
top_15_players = top_15_players.sort_values(by=['overall', 'age', 'potential', 'hits'], ascending=[False, True, False, False])

# Gráfico de barras para os 15 melhores jogadores exibindo apenas o potencial atual
bar_width = 0.5
bar_spacing = 1  # Espaçamento entre as barras
names_with_spacing = top_15_players['name'] + ' ' + (np.arange(len(top_15_players)) * bar_spacing).astype(str)

def plot_top_15_players():
    fig, ax = plt.subplots()
    ax.barh(names_with_spacing, current_potential - top_15_players['overall'], color='green', height=bar_width, label='Potencial - Overall')
    ax.set_ylabel('Jogadores')
    ax.set_xlabel('Diferença de Potencial (Atual - Overall)')
    ax.set_title('Top 15 Jogadores - Diferença de Potencial (Atual - Overall)')
    ax.legend()
    ax.invert_yaxis()  # Inverte a ordem dos jogadores
    st.pyplot(fig)

# Exibir tabela de Overall, Potencial Máximo, Diferença de Potencial e Idade Invertida
st.write("### Tabela de Overall, Potencial Máximo, Diferença de Potencial (não visível) e Idade Invertida:")
# Cria uma tabela com informações sobre os 15 melhores jogadores
def display_potentials_table():
    potentials_table = pd.DataFrame({
        'Nome': top_15_players['name'],
        'Overall': top_15_players['overall'],
        'Potencial Máximo': max_potential,
        'Diferença de Potencial (não visível)': potential_diff,
        'Idade Invertida': inverse_age
    })
    st.write(potentials_table)

# Mostrar o gráfico
plot_top_15_players()

# Exibir tabela de Overall, Potencial Máximo, Diferença de Potencial e Idade Invertida
display_potentials_table()

# Gráfico de barras para mostrar o overall atual dos 15 melhores jogadores
def plot_overall():
    overall_fig, overall_ax = plt.subplots()
    overall_ax.barh(names_with_spacing, top_15_players['overall'], color='purple', height=bar_width, label='Overall Atual')
    overall_ax.set_ylabel('Jogadores')
    overall_ax.set_xlabel('Overall Atual')
    overall_ax.set_title('Overall Atual dos 15 Melhores Jogadores')
    overall_ax.legend()
    overall_ax.invert