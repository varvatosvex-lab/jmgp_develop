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

# Mostrar galería de personajes
theme_color = "#4A90E2"  # Color para la interfaz gamer
st.markdown("""<style>
    .title {text-align: center; font-size: 24px; color: white; background-color: """ + theme_color + """; padding: 10px; border-radius: 10px;}
    .table-style {border-collapse: collapse; width: 100%;}
    .table-style th, .table-style td {border: 1px solid white; padding: 8px; text-align: left; color: white;}
</style>""", unsafe_allow_html=True)

st.subheader("⚡ Personajes y Nivel de Poder ⚡")

for _, row in characters_df.iterrows():
    character_name = row["Nombre"]
    practice = row.get("Categoría", "Desconocida")  # Obtener la práctica asociada
    insignias = row.get("Insignias", "N/A")
    experiencia = row.get("Experiencia", "N/A")
    cursos = row.get("Cursos", "N/A")
    proyectos = row.get("Proyectos", "N/A")
    certificaciones = row.get("Certificaciones", "N/A")
    power_level = int(player_data[character_name].values[0])
    
    col1, col2, col3 = st.columns([2, 2, 3])
    
    with col1:
        st.image(row["Imagen"], width=200)
        st.markdown(f"<div class='title'>{character_name}</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"**🏹 Práctica:** {practice}")
        st.progress(power_level / 100)
        st.write(f"🔥 **Nivel de Poder:** {power_level}%")
    
    with col3:
        st.markdown("<table class='table-style'>", unsafe_allow_html=True)
        st.markdown(f"<tr><th>🏅 Insignias</th><td>{insignias}</td></tr>", unsafe_allow_html=True)
        st.markdown(f"<tr><th>📜 Certificaciones</th><td>{certificaciones}</td></tr>", unsafe_allow_html=True)
        st.markdown(f"<tr><th>📚 Cursos</th><td>{cursos}</td></tr>", unsafe_allow_html=True)
        st.markdown(f"<tr><th>🛠️ Proyectos</th><td>{proyectos}</td></tr>", unsafe_allow_html=True)
        st.markdown(f"<tr><th>🎖️ Experiencia</th><td>{experiencia}</td></tr>", unsafe_allow_html=True)
        st.markdown("</table>", unsafe_allow_html=True)
