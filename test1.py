import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="CO2StoCal", layout="wide")

# CSS para fondo marino y selectbox completamente en negro
st.markdown(
    """
    <style>
    body {
        background-color: #003366;
    }
    .stApp {
        background-color: #003366;
    }
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: white !important;
    }
    .stButton button {
        background-color: #005580;
        color: white;
    }
    .stButton button:hover {
        background-color: #0077b6;
        color: white;
    }
    /* Estilo del selectbox y su lista desplegable */
    div[data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        border-radius: 5px;
        padding: 5px;
    }
    div[data-baseweb="select"] * {
        color: black !important;
        background-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo y Título
st.markdown("<h1 style='text-align: center;'>🌍 CO2StoCal</h1>", unsafe_allow_html=True)

# Menú de navegación con íconos en horizontal
col1, col2, col3, col4 = st.columns(4)

if "seccion" not in st.session_state:
    st.session_state.seccion = ""

with col1:
    if st.button("🌫️ Emisiones de CO2"):
        st.session_state.seccion = "Emisiones"
with col2:
    if st.button("🪨 Almacenamiento geológico"):
        st.session_state.seccion = "Almacenamiento"
with col3:
    if st.button("📊 Análisis de datos"):
        st.session_state.seccion = "Datos"
with col4:
    if st.button("📍 Análisis geográfico"):
        st.session_state.seccion = "Geográfico"

# Contenido principal según sección seleccionada
if st.session_state.seccion == "Emisiones":
    st.subheader("Emisiones de CO2")
    col1, col2 = st.columns(2)

    with col1:
        pais = st.selectbox("Seleccione un país", ["Ecuador", "Brasil", "Colombia"],
                            key="pais")

    with col2:
        fuente = st.selectbox("Seleccione una fuente",
                              ["ONU", "Banco Mundial", "Agencia Ambiental"],
                              key="fuente")

    if st.button("Calcular emisiones"):
        df = pd.DataFrame({
            "Año": list(range(2000, 2026, 5)),
            "Emisiones": [150, 250, 350, 450, 520, 600]
        })
        fig = px.line(df, x="Año", y="Emisiones",
                      title=f"Emisiones de {pais} ({fuente})",
                      labels={"Emisiones": "Emisiones (Mmc)", "Año": "Año"})
        st.plotly_chart(fig, use_container_width=True)

elif st.session_state.seccion == "Almacenamiento":
    st.subheader("Almacenamiento geológico")
    st.info("Sección en desarrollo")

elif st.session_state.seccion == "Datos":
    st.subheader("Análisis de datos")
    st.info("Sección en desarrollo")

elif st.session_state.seccion == "Geográfico":
    st.subheader("Análisis geográfico")
    st.info("Sección en desarrollo")
