import streamlit as st
import pandas as pd

# Cargar datos desde los archivos CSV
@st.cache_data
def load_data():
    characters = pd.read_csv("data/characters.csv")
    players = pd.read_csv("data/players.csv")
    return characters, players

st.title("🎮 Galería de Personajes y Nivel de Poder 🏆")

# Cargar datos desde CSV
characters_df, players_df = load_data()

# Selección de jugador
selected_player = st.selectbox("👤 Selecciona un jugador:", players_df["Nombre"].unique())

# Filtrar datos del jugador seleccionado
player_data = players_df[players_df["Nombre"] == selected_player]

st.subheader("⚡ Personajes y Nivel de Poder ⚡")

theme_color = "#4A90E2"  # Color de la interfaz gamer
st.markdown(f"""
    <style>
        .title {{text-align: center; font-size: 14px; color: white; background-color: {theme_color}; 
                 padding: 10px; border-radius: 10px;}}
    </style>
""", unsafe_allow_html=True)

# Obtener lista de prácticas únicas para exploración
practices = characters_df["Categoría"].unique()
selected_practice = st.selectbox("🏹 Selecciona una práctica:", practices)

# Filtrar personajes de la práctica seleccionada
filtered_characters = characters_df[characters_df["Categoría"] == selected_practice]

# Si hay más de un personaje en la práctica, permitir exploración con slider
num_characters = len(filtered_characters)
character_index = 0  # Índice por defecto

if num_characters > 1:
    character_index = st.slider("🔄 Desliza para cambiar de personaje", 0, num_characters - 1, 0)

# Obtener el personaje seleccionado por el slider
selected_character = filtered_characters.iloc[character_index]

# Extraer datos del personaje
character_name = selected_character["Nombre"]
description = selected_character.get("Descripción", "Sin descripción disponible")
insignias = selected_character.get("Insignias", "N/A")
experiencia = selected_character.get("Experiencia", "N/A")
cursos = selected_character.get("Cursos", "N/A")
proyectos = selected_character.get("Proyectos", "N/A")
certificaciones = selected_character.get("Certificaciones", "N/A")

# Obtener nivel de poder del personaje para el jugador seleccionado
power_level = player_data.get(character_name, pd.Series([0])).values[0]
power_level = max(0, min(100, int(power_level)))  # Asegurar rango válido (0-100)

# Manejo de imagen nula o incorrecta
image_url = selected_character["Imagen"] if pd.notna(selected_character["Imagen"]) else "default.png"

col1, col2, col3 = st.columns([2, 2, 3])

with col1:
    st.image(image_url, width=200)
    st.markdown(f"<div class='title'>{character_name}</div>", unsafe_allow_html=True)
    with st.expander("ℹ️ Descripción"):
        st.write(description)

with col2:
    st.markdown(f"**🏹 Práctica:** {selected_practice}")
    st.progress(power_level / 100)
    st.write(f"🔥 **Nivel de Poder:** {power_level}%")

with col3:
    # Usar un DataFrame para mostrar la información de forma ordenada
    table_data = {
        "🏅 Insignias": [insignias],
        "📜 Certificaciones": [certificaciones],
        "📚 Cursos": [cursos],
        "🛠️ Proyectos": [proyectos],
        "🎖️ Experiencia": [experiencia]
    }
    st.dataframe(pd.DataFrame(table_data))