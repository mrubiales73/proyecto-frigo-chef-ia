

from Conexion import client
from Conexion import MODEL

# -----------------------------
# 🤖 DEFINICIÓN AGENTE CONTROL DE DESPERDICIOS
# -----------------------------

def agente_antidesperdicio(recetas_borrador, ingredientes):
    """Agente 4: Prioriza caducidad y añade consejos de sostenibilidad"""
    prompt = f"""
    Actúas como un Experto en Sostenibilidad de cocina. Revisa estas recetas y la lista original: {ingredientes}.
    Diseña un consejo clave anti-desperdicio para cada plato enfocado en aprovechar al máximo lo que ya hay en la nevera.
    """
    response = client.models.generate_content(
        model=MODEL, contents=recetas_borrador, config={"system_instruction": prompt, "temperature": 0.2}
    )
    return response.text
