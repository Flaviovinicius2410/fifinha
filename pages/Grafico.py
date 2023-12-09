import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Load Titanic dataset
df = pd.read_csv("train.csv")

st.title("Visualizações do Titanic Dataset")

# Choose a column for categories and values
selected_column = st.selectbox("Selecione a coluna para categorias", df.columns)
categories = df[selected_column]

# Count the occurrences of each category
value_counts = categories.value_counts()

# Split data into categories and values
categorias = value_counts.index.tolist()
valores = value_counts.values.tolist()

# Display the bar chart using Streamlit components
st.subheader(f"Contagem por {selected_column} (Gráfico de Barras)")

# Using Altair for a more interactive chart
chart_data = pd.DataFrame({selected_column: categorias, 'Contagem': valores})
st.altair_chart(chart_data, use_container_width=True)

# Display the line chart using Streamlit components
st.subheader(f"Contagem por {selected_column} (Gráfico de Linhas)")

# Using Altair for a more interactive chart
line_chart_data = pd.DataFrame({selected_column: categorias, 'Contagem': valores})
st.line_chart(line_chart_data.set_index(selected_column))

# Display the pie chart using Streamlit components
st.subheader(f"Contagem por {selected_column} (Gráfico de Pizza)")

# Using Plotly for a pie chart
fig_pie = go.Figure(data=[go.Pie(labels=categorias, values=valores)])
fig_pie.update_layout(title=f'Contagem por {selected_column}')
st.plotly_chart(fig_pie)

# Display the bar chart using Matplotlib
st.subheader(f"Contagem por {selected_column} (Matplotlib)")

fig, ax = plt.subplots()
ax.bar(categorias, valores, color='skyblue')
ax.set_xlabel(selected_column)
ax.set_ylabel('Contagem')
ax.set_title(f'Contagem por {selected_column}')
st.pyplot(fig)

# Display the bar chart using Plotly
st.subheader(f"Contagem por {selected_column} (Plotly)")

data = [go.Bar(x=categorias, y=valores, marker=dict(color='lightcoral'))]
layout = go.Layout(title=f'Contagem por {selected_column}', xaxis=dict(title=selected_column), yaxis=dict(title='Contagem'))
fig_bar = go.Figure(data=data, layout=layout)
st.plotly_chart(fig_bar)