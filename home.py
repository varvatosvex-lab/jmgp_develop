import streamlit as st
from PIL import Image

# Configurar la página
st.set_page_config(page_title="DevOps & Generative AI Dashboard", page_icon="🚀", layout="wide")

# Imagen de cabecera
#header_image = Image.open("header_image.png")  # Asegúrate de tener una imagen relevante
#st.image(header_image, use_column_width=True)

# Mensaje poderoso de bienvenida
st.title("🚀 Ingeniería DevOps & Generative AI: Innovación, Automatización y Excelencia")
st.markdown(
    """
    ## Bienvenido al Hub de Ingeniería DevOps y Generative AI
    
    En este espacio centralizamos la información clave sobre nuestra práctica de Ingeniería en DevOps y Generative AI. Aquí encontrarás:
    
    - 📊 **KPIs Clave:** Medimos y optimizamos el impacto de nuestras soluciones.
    - 🎓 **Seguimiento de Cursos y Certificaciones:** Fomentamos el aprendizaje continuo y el crecimiento profesional.
    - 🏆 **Logros y Reconocimientos:** Celebraremos cada hito alcanzado en la práctica.
    - 🚀 **Proyectos Estratégicos:** Exploramos y ejecutamos iniciativas de alto impacto.
    - 🔍 **Evaluaciones Internas:** Fomentamos la mejora continua mediante revisiones y feedback estructurado.
    
    Creemos en la transformación digital, la automatización y la inteligencia artificial como pilares para el futuro. ¡Avancemos juntos!
    """
)

# Sección de navegación
st.sidebar.title("🔍 Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏠 Inicio", "📊 KPIs", "🎓 Cursos & Certificaciones", "🏆 Logros", "🚀 Proyectos", "🔍 Evaluaciones"]
)