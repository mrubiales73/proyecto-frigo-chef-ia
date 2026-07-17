# Instalación las librerías necesarias
# pip install -r requirements.txt
# para lanzar: streamlit run Interfaz_streamlit.py


# Conexion.py
# -------------------------------------------------------------------------------------------------------
# LIBRERÍAS REQUERIDAS
# -------------------------------------------------------------------------------------------------------
from google import genai
from google.oauth2 import service_account
import streamlit as st
import json

# -------------------------------------------------------------------------------------------------------
# CONFIGURACIÓN DE CONSTANTES (PÚBLICAS)
# -------------------------------------------------------------------------------------------------------
LOCATION = "us-central1"
MODEL = "gemini-2.5-flash"


# -------------------------------------------------------------------------------------------------------
# CARGA DINÁMICA DE CREDENCIALES Y PROJECT_ID (100% Protegido)
# -------------------------------------------------------------------------------------------------------
credentials = None
project_id = None


# 1. Producción: Intentamos leer los secretos de Streamlit (Evitamos exponer el ID del proyecto)
if "gcp_service_account" in st.secrets:
    try:
        info_credenciales = dict(st.secrets["gcp_service_account"])
        credentials = service_account.Credentials.from_service_account_info(
            info_credenciales,
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        # Extraemos el PROJECT_ID dinámicamente del propio secreto
        project_id = info_credenciales.get("project_id")

    except Exception as e:
        st.error(f"Error cargando las credenciales desde Streamlit Secrets: {e}")

# 2. Control de Seguridad: Si no se ha podido determinar el ID de proyecto, lanzamos un aviso
if not project_id:
    st.error("🔒 Error crítico de seguridad: No se pudo determinar el Project ID de Google Cloud de forma dinámica.")

# -------------------------------------------------------------------------------------------------------
# INICIALIZACIÓN DEL CLIENTE MULTIMODAL
# -------------------------------------------------------------------------------------------------------
client = genai.Client(
    vertexai=True,
    project=project_id,
    location=LOCATION,
    credentials=credentials
)