
from Conexion import client
from Conexion import MODEL

# -----------------------------
# 🤖 DEFINICIÓN
# -----------------------------


def agente_recetas(ingredientes_limpios, tiempo, dieta):
    """Agente 2: Diseña exclusivamente los platos viables"""
    prompt = f"""
    Actúas como un Chef. Genera 3 recetas realistas usando únicamente estos ingredientes: {ingredientes_limpios}.
    Ajustate al tiempo máximo de {tiempo} y la dieta {dieta}.
    Devuelve solo el Nombre, Ingredientes usados y Pasos.
    """
    response = client.models.generate_content(
        model=MODEL, contents="Genera las recetas básicas.", config={"system_instruction": prompt, "temperature": 0.2}
    )
    return response.text
