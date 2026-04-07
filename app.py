import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Titulo
st.title ("Analisis de anuncios de coches")
# Grafico 1
fig1 = go.Figure()
fig1.add_trace(go.Histogram(x=car_data["odometer"]))
fig1.update_layout(title="Distribución del odómetro")
st.plotly_chart(fig1, use_container_width=True)

# Grafico 2
fig2 = go.Figure()
fig2.add_trace(go.Histogram(x=car_data["price"]))
fig2.update_layout(title="Distribución del precio")
st.plotly_chart(fig2, use_container_width=True)

# Grafico 3
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=car_data["odometer"],
    y=car_data["price"],
    mode='markers'))

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
