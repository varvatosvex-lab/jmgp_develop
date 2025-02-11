import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar página
st.set_page_config(page_title="Dashboard Ingeniería Cloud", layout="wide")

# Cargar datos simulados
def load_data():
    kpis_cloud = pd.read_csv("kpis_cloud.csv")
    logros = pd.read_csv("logros.csv")
    learning_path = pd.read_csv("learning_path.csv")
    jira_tracking = pd.read_csv("jira_tracking.csv")
    ingenieros_df = pd.read_csv("ingenieros.csv")
    proyectos_df = pd.read_csv("proyectos.csv")
    cursos_df = pd.read_csv("cursos.csv")
    niveles_df = pd.read_csv("niveles.csv")
    insignias_df = pd.read_csv("insignias.csv")
    return kpis_cloud, logros, learning_path, jira_tracking, ingenieros_df, proyectos_df, cursos_df, niveles_df, insignias_df

kpis_cloud, logros, learning_path, jira_tracking, ingenieros_df, proyectos_df, cursos_df, niveles_df, insignias_df = load_data()

# Menú de Navegación
menu = st.sidebar.radio("Menú", ["🏆 KPIs Cloud DevOps", "🎯 Logros", "📚 Learning Path", "📊 Seguimiento de Proyectos", "📡 Dashboard General", "📈 Desempeño de Ingeniería", "🎖 Niveles y Logros"])

if menu == "🏆 KPIs Cloud DevOps":
    st.title("KPIs de Cloud DevOps")
    st.markdown("## 📌 Métricas de Infraestructura como Código (IaC), Configuración como Código (CaC) y Pipelines como Código (PaC)")
    
    # Gráfico de KPIs
    fig_kpis = px.bar(kpis_cloud, x="Métrica", y="Valor", color="Métrica", title="Métricas de Cloud DevOps")
    st.plotly_chart(fig_kpis, use_container_width=True)

elif menu == "🎯 Logros":
    st.title("Logros del Equipo")
    st.markdown("## 🎖 Resumen de logros por mes")
    st.dataframe(logros)
    
elif menu == "📚 Learning Path":
    st.title("Seguimiento de Cursos y Certificaciones")
    st.markdown("## 📘 Estado de Certificaciones por Ingeniero")
    st.dataframe(learning_path)
    
elif menu == "📊 Seguimiento de Proyectos":
    st.title("Seguimiento de Proyectos en Jira")
    st.markdown("## 📋 Métricas de Jira - Horas y Avance")
    fig_jira = px.bar(jira_tracking, x="Proyecto", y="Porcentaje de Avance", color="Proyecto", title="Avance de Proyectos en Jira")
    st.plotly_chart(fig_jira, use_container_width=True)
    
elif menu == "📡 Dashboard General":
    st.title("Dashboard General de Ingeniería Cloud")
    st.markdown("## 🔍 Resumen de métricas clave")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total KPIs Monitoreados", len(kpis_cloud))
    col2.metric("Logros Documentados", len(logros))
    col3.metric("Proyectos en Seguimiento", len(jira_tracking))
    st.markdown("### 📊 Vista General de KPIs")
    st.plotly_chart(px.bar(kpis_cloud, x="Métrica", y="Valor", color="Métrica", title="Vista General de KPIs"), use_container_width=True)

elif menu == "📈 Desempeño de Ingeniería":
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

elif menu == "🎖 Niveles y Logros":
    st.title("🎖 Niveles y Logros de Ingenieros")
    st.markdown("## 🚀 Progreso de Ingenieros en XP y Niveles")
    st.dataframe(niveles_df)
    
    st.markdown("## 🏆 Insignias Ganadas")
    st.dataframe(insignias_df)
