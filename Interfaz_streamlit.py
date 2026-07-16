
# -----------------------------
# INTERFAZ DE USUARIO (STREAMLIT)
# -----------------------------

# Interfaz_streamlit.py
import streamlit as st
from agentes.agente_orquestador import agente_orquestador

st.set_page_config(page_title="Frigo-Chef Multimodal", page_icon="🤖📸", layout="centered")

st.title("🤖📸 Frigo-Chef IA — Modo Multimodal Avanzado")
st.caption("Ecosistema de agentes con soporte para múltiples imágenes, vídeo, texto y audio nativo")

st.write("### 1. ¿Cómo quieres cargar tus ingredientes?")




# --- INPUT A: Múltiples imágenes ---
archivos_imagenes = st.file_uploader(
    "Opción IMAGEN : Sube entre 1 y 3 fotos de tu nevera (puntos ciegos, cajones...)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True)

lista_de_bytes = []
if archivos_imagenes:
    archivos_validos = archivos_imagenes[:3]
    columnas = st.columns(len(archivos_validos))
    for idx, img in enumerate(archivos_validos):
        with columnas[idx]:
            st.image(img, caption=f"Foto {idx + 1}", use_container_width=True)
    lista_de_bytes = [img.read() for img in archivos_validos]

# --- INPUT B: Barrido de Vídeo ---
archivo_video = st.file_uploader(
    "Opción VIDEO: Sube un barrido corto de vídeo (2-3 segundos)",
    type=["mp4", "mov", "avi"]
)

video_bytes = None
if archivo_video:
    st.video(archivo_video)
    video_bytes = archivo_video.read()

# --- INPUT C: Nota de Voz / Audio (NUEVO) ---
archivo_audio = st.file_uploader(
    "Opción AUDIO: Sube una nota de voz con tus ingredientes",
    type=["wav", "mp3", "m4a", "ogg"]
)

audio_bytes = None
mime_audio = None
if archivo_audio:
    st.audio(archivo_audio)
    audio_bytes = archivo_audio.read()
    # Guardamos el tipo MIME correcto para pasárselo a Gemini (ej. "audio/wav")
    mime_audio = archivo_audio.type

# --- INPUT D: Texto manual ---
ingredientes_manual = st.text_area(
    "Opción TEXTO: Escribe ingredientes:",
    placeholder="Ejemplo: Se me olvidaba la salsa barbacoa y salsa de soja"
)


st.write("### 2. Preferencias de cocinado")
col1, col2 = st.columns(2)
with col1:
    tiempo = st.selectbox("Tiempo disponible:", ["Sin límite", "15 minutos", "30 minutos", "1 hora"])
with col2:
    dieta = st.multiselect("Filtros dietéticos:", ["Sin gluten", "Sin lactosa", "Vegano", "Vegetariano"],
                           placeholder="Ninguna")

# Botón único de ejecución
boton_ejecutar = st.button("Lanzar Análisis de Nevera 🚀", use_container_width=True)

if boton_ejecutar:
    # Validamos que haya al menos un tipo de entrada
    if not ingredientes_manual and not lista_de_bytes and video_bytes is None and audio_bytes is None:
        st.warning("⚠️ Por favor, introduce texto, fotos, vídeo o audio para poder trabajar.")
    else:
        with st.status("🧠 Ecosistema procesando la solicitud...", expanded=True) as status:
            st.write("🕵️‍♂️ Agente Detector analizando la entrada multimodal (Texto + Multimedia + Voz)...")

            # ATENCIÓN: Añadimos parámetros de audio a la llamada del orquestador
            datos_finales = agente_orquestador(
                ingredientes_manual,
                lista_de_bytes,
                video_bytes,
                audio_bytes,
                mime_audio,
                tiempo,
                dieta
            )
            status.update(label="¡Procesamiento finalizado!", state="complete", expanded=False)

        if "error" in datos_finales:
            st.error(datos_finales["error"])
        else:
            st.success("🎉 ¡Propuestas de los agentes listas!")
            for receta in datos_finales["recetas"]:
                with st.expander(f"📖 {receta['nombre']} ({receta['tiempo_min']} min)"):
                    st.write("**Ingredientes utilizados:** " + ", ".join(receta['ingredientes_usados']))
                    if receta.get('faltantes_opcionales'):
                        st.write("**🛒 Sugerencia de compra extra:** " + ", ".join(receta['faltantes_opcionales']))
                    st.write("**Instrucciones de preparación:**")
                    for paso in receta['pasos']:
                        st.write(f"- {paso}")
                    st.info(f"🥗 **Perfil Nutricional:** {receta['informacion_nutricional']}")
                    st.warning(f"💡 **Sostenibilidad:** {receta['consejo_antidesperdicio']}")