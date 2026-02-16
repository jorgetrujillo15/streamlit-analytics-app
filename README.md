# 🚗 Análisis del Mercado de Vehículos Usados

Link Render (Visualizacion de app interactiva): https://streamlit-analytics-app-np4q.onrender.com

Video ejemplo funcionamiento app interactiva: https://drive.google.com/drive/folders/1BLMhtYlsXkENR4tfOsmHJqeIXnTTFmpf?usp=sharing

## 📌 Descripción del Proyecto

Este proyecto analiza un conjunto de datos del mercado de vehículos usados en Estados Unidos con el objetivo de identificar patrones en el comportamiento de precios.

Se realizó un proceso completo de:

- Limpieza de datos
- Detección y eliminación de valores atípicos
- Ingeniería de características
- Análisis exploratorio
- Desarrollo de un dashboard interactivo con Streamlit

---

## 🎯 Objetivos

- Analizar la relación entre precio, kilometraje y antigüedad del vehículo.
- Identificar diferencias de precio según el tipo de vehículo.
- Construir una aplicación interactiva para explorar los datos dinámicamente.

---

## 🧹 Proceso de Limpieza

Se aplicó un filtrado por percentiles (1% – 99%) en las variables:

- `price`
- `odometer`

Con esto se eliminaron valores extremos que distorsionaban el análisis, manteniendo la integridad estadística del dataset.

También se creó la variable:

- `vehicle_age`: antigüedad del vehículo calculada a partir del año del modelo.

---

## 📊 Análisis Realizado

- Distribución de precios antes y después de limpieza.
- Correlación entre precio, kilometraje y antigüedad.
- Comparación de precios promedio por tipo de vehículo.
- Visualización de relaciones clave mediante gráficos interactivos.

---

## 🚀 Dashboard Interactivo

La aplicación fue desarrollada utilizando **Streamlit** y permite:

- Filtrar por rango de precio.
- Filtrar por tipo de vehículo.
- Visualizar métricas clave en tiempo real.
- Explorar la relación entre precio y kilometraje.
- Analizar la distribución de precios por segmento.

---

## 🛠 Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---


