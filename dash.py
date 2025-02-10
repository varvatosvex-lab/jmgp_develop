import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos simulados
ingenieros_df = pd.read_csv("ingenieros.csv")
proyectos_df = pd.read_csv("proyectos.csv")
cursos_df = pd.read_csv("cursos.csv")

# Configurar diseño de Streamlit
st.set_page_config(page_title="Dashboard Ingeniería Cloud", layout="wide")

# Encabezado principal
st.title("📊 Dashboard Ingeniería de Cloud e IA")
st.markdown("---")

# KPI Resumen
col1, col2, col3 = st.columns(3)
col1.metric("Total Ingenieros", len(ingenieros_df))
col2.metric("Proyectos Activos", len(proyectos_df[proyectos_df["Estado"] == "En curso"]))
col3.metric("Cursos en Progreso", len(cursos_df))

st.markdown("---")

# Sección: Desempeño por Grupo
grupos = ingenieros_df["Grupo"].unique()
grupo_seleccionado = st.selectbox("📌 Selecciona un Grupo de Ingenieros", grupos)

filtro_ingenieros = ingenieros_df[ingenieros_df["Grupo"] == grupo_seleccionado]
fig_prod = px.bar(filtro_ingenieros, x="Nombre", y="KPI Productividad", color="Nombre",
                  title=f"Productividad del Grupo: {grupo_seleccionado}")
st.plotly_chart(fig_prod, use_container_width=True)

st.markdown("---")

# Sección: Estado de Proyectos
st.subheader("📌 Estado de Proyectos")
fig_proyectos = px.bar(proyectos_df, x="Proyecto", y="Progreso", color="Estado",
                       title="Progreso de Proyectos")
st.plotly_chart(fig_proyectos, use_container_width=True)

# Sección: Cursos y Avance
st.subheader("🎓 Avance en Entrenamientos")
cursos_grupo = cursos_df[cursos_df["Grupo"] == grupo_seleccionado]
fig_cursos = px.bar(cursos_grupo, x="Curso", y="Avance", color="Curso", title=f"Avance en Cursos - {grupo_seleccionado}")
st.plotly_chart(fig_cursos, use_container_width=True)

st.markdown("---")

# Tabla con detalles de proyectos
st.subheader("📋 Detalles de Proyectos")
st.dataframe(proyectos_df)
