
from agentes.agente_detector import agente_detector
from agentes.agente_recetas import  agente_recetas
from agentes.agente_lista_compra import agente_lista_compra
from agentes.agente_nutricional import  agente_nutricional
from agentes.agente_desperdicio import agente_antidesperdicio

from Conexion import client
from Conexion import MODEL

import json
import streamlit as st



# -----------------------------
# 👑 AGENTE ORQUESTADOR (CONTRATO JSON)
# -----------------------------


def agente_orquestador(ingredientes_manual, lista_de_bytes, video_bytes, audio_bytes, mime_audio, tiempo, dieta):
    """Coordina el flujo completo y consolida la salida en el JSON oficial."""

    # Se los pasamos al agente detector
    ingredientes_ok = agente_detector(ingredientes_manual, lista_de_bytes, video_bytes, audio_bytes, mime_audio)

    if "INVALIDO" in ingredientes_ok:
        return {"error": "El Agente Detector no ha podido identificar ingredientes válidos en tu entrada."}



    if "INVALIDO" in ingredientes_ok:
        return {"error": "El Agente Detector no ha podido identificar comida válida en la entrada multimedia."}


    # Mostramos en Streamlit un aviso de lo que ha descubierto el Agente 1
    st.sidebar.markdown(f"**🔍 Alimentos detectados por IA:**\n*{ingredientes_ok}*")

    # 2. Ejecución en Cascada de los agentes especializados
    recetas_base = agente_recetas(ingredientes_ok, tiempo, dieta)
    analisis_nutri = agente_nutricional(recetas_base, dieta)
    consejos_eco = agente_antidesperdicio(recetas_base, ingredientes_ok)
    lista_compra = agente_lista_compra(recetas_base)

    # 3. Consolidación Final en el Formato de Salida Obligatorio
    prompt_ensamblador = f"""
    Une toda la información recolectada de la cocina en un único JSON estructurado.
    - Recetas base: {recetas_base}
    - Análisis nutricional: {analisis_nutri}
    - Consejos ecológicos: {consejos_eco}
    - Faltantes sugeridos: {lista_compra}

    Formatea TODO obligatoriamente en este JSON estructurado:
    {{
      "recetas": [
        {{
          "nombre": "string",
          "tiempo_min": 20,
          "ingredientes_usados": ["lista"],
          "faltantes_opcionales": ["lista de la compra sugerida"],
          "pasos": ["lista"],
          "informacion_nutricional": "resumen del balance y alertas",
          "consejo_antidesperdicio": "consejo de sostenibilidad"
        }}
      ]
    }}
    """

    response = client.models.generate_content(
        model=MODEL,
        contents="Consolida el JSON.",
        config={
            "system_instruction": prompt_ensamblador,
            "response_mime_type": "application/json",
            "temperature": 0.0
        }
    )
    return json.loads(response.text)
