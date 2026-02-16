# 1) Librerías con las que se trabajará
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -----------------------------------------------------------------

# 2) Configuración de la página

st.set_page_config(
    page_title="Análisis del Mercado de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------------------------------------------

# 3) Título y descripción

st.title("🚗 Análisis del Mercado de Vehículos Usados")

st.markdown("""
Este dashboard permite explorar el comportamiento del mercado de vehículos usados en EE.UU.,
analizando precio, kilometraje, antigüedad y tipo de vehículo.
""")

# -----------------------------------------------------------------

# 4) Carga de datos

@st.cache_data
def load_data():
    df = pd.read_csv("data/vehicles_us.csv")
    return df

car_data = load_data()

# -----------------------------------------------------------------

# 5) Limpieza de datos

# Filtrado por percentiles
price_low = car_data['price'].quantile(0.01)
price_high = car_data['price'].quantile(0.99)

odo_low = car_data['odometer'].quantile(0.01)
odo_high = car_data['odometer'].quantile(0.99)

car_data_clean = car_data[
    (car_data['price'] >= price_low) & 
    (car_data['price'] <= price_high) &
    (car_data['odometer'] >= odo_low) &
    (car_data['odometer'] <= odo_high)
].copy()

# Ingeniería de características
car_data_clean['model_year'] = pd.to_numeric(
    car_data_clean['model_year'], errors='coerce'
)

car_data_clean['vehicle_age'] = 2019 - car_data_clean['model_year']

car_data_clean['is_4wd'] = car_data_clean['is_4wd'].fillna(0).astype(int)

# -----------------------------------------------------------------

# 6) Sidebar – Filtros dinámicos

st.sidebar.header("🔎 Filtros")

# Rango de precio
price_range = st.sidebar.slider(
    "Rango de precio",
    int(car_data_clean['price'].min()),
    int(car_data_clean['price'].max()),
    (
        int(car_data_clean['price'].min()),
        int(car_data_clean['price'].max())
    )
)

# Tipo de vehículo
vehicle_type = st.sidebar.multiselect(
    "Tipo de vehículo",
    options=sorted(car_data_clean['type'].dropna().unique()),
    default=sorted(car_data_clean['type'].dropna().unique())
)

# Aplicar filtros

filtered_data = car_data_clean[
    (car_data_clean['price'] >= price_range[0]) &
    (car_data_clean['price'] <= price_range[1]) &
    (car_data_clean['type'].isin(vehicle_type))
]

# -----------------------------------------------------------------

# 7) Métricas clave

st.subheader("📌 Indicadores Clave")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Precio promedio", f"${filtered_data['price'].mean():,.0f}")
col2.metric("Kilometraje promedio", f"{filtered_data['odometer'].mean():,.0f} mi")
col3.metric("Edad promedio", f"{filtered_data['vehicle_age'].mean():.1f} años")
col4.metric("Total de anuncios", f"{filtered_data.shape[0]:,}")

# -----------------------------------------------------------------

# 8) Gráfico 1 – Precio vs Kilometraje

st.subheader("📉 Relación entre Precio y Kilometraje")

fig_scatter = px.scatter(
    filtered_data,
    x="odometer",
    y="price",
    color="type",
    trendline="ols",
    opacity=0.6
)

st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------------------------------------------

# 9) Gráfico 2 – Precio por tipo de vehículo

st.subheader("⏳ Precio vs Antigüedad del Vehículo")

fig_age = px.scatter(
    filtered_data,
    x="vehicle_age",
    y="price",
    trendline="ols",
    opacity=0.6
)

st.plotly_chart(fig_age, use_container_width=True)

st.markdown("---")
st.markdown("Proyecto de análisis de datos - Dashboard interactivo con Streamlit 🚀")

