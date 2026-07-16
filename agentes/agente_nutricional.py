

from Conexion import client
from Conexion import MODEL

# -----------------------------
# 🤖 DEFINICIÓN AGENTE NUTRICIONAL
# -----------------------------


def agente_nutricional(recetas_borrador, dieta):
    """Agente 3: Calcula el balance y añade alertas nutricionales"""
    prompt = f"""
    Actúas como un Nutricionista. Analiza el borrador de recetas. 
    Añade un resumen breve del balance calórico estimado y confirma si cumple la restricción: {dieta}.
    """
    response = client.models.generate_content(
        model=MODEL, contents=recetas_borrador, config={"system_instruction": prompt, "temperature": 0.1}
    )
    return response.text