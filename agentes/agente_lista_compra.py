
from Conexion import client
from Conexion import MODEL


# -----------------------------
# 🤖 DEFINICIÓN AGENTE LISTA DE LA COMPRA
# -----------------------------


def agente_lista_compra(recetas_borrador):
    """Agente 5: Identifica faltantes mínimos opcionales para mejorar el plato"""
    prompt = """
    Actúas como un Asistente del supermercado. Revisa las recetas.
    Identifica si hay algún ingrediente secundario no indispensable (especias, un toque de condimento, etc.) 
    que el usuario podría añadir opcionalmente para mejorar sustancialmente el plato.
    """
    response = client.models.generate_content(
        model=MODEL, contents=recetas_borrador, config={"system_instruction": prompt, "temperature": 0.1}
    )
    return response.text
