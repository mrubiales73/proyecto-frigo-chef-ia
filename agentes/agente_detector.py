
# -----------------------------
# 🤖 DEFINICIÓN AGENTE DETECTOR MULTIMODAL
# -----------------------------



from Conexion import client
from Conexion import MODEL
from google.genai import types


def agente_detector(
        ingredientes_texto: str,
        lista_imagenes_bytes: list,
        video_bytes: bytes = None,
        audio_bytes: bytes = None,
        mime_audio: str = None
) -> str:
    """Agente 1: Detecta e integra ingredientes e intenciones usando texto, fotos, vídeo y notas de voz."""

    prompt_base = """
    Actúas como un Detector de Alimentos experto con inteligencia multimodal avanzada.
    Analiza meticulosamente las entradas proporcionadas (pueden ser textos, fotos, vídeos, notas de voz, o todo junto).

    Tus tareas son:
    1. Identificar y unificar todos los ingredientes comestibles reales en una lista única en minúsculas, separados por comas.
    2. Si en el audio o en el texto el usuario añade comentarios, deseos contextuales o peticiones (ej. "quiero algo rápido para ver el partido" o "sugiéreme una bebida"), añádelos claramente al final de la lista precedidos por la etiqueta: "[CONTEXTO_USUARIO]: " y resume lo que pide el usuario.
    3. Evitar duplicados. Si un ingrediente se repite entre las fotos, el vídeo o el audio, añádelo una única vez.
    4. Si no hay elementos comestibles o la entrada no tiene sentido, responde exactamente: 'INVALIDO'.
    5. Devuelve ÚNICAMENTE la lista de ingredientes (y el [CONTEXTO_USUARIO] si existe) en texto limpio. No agregues introducciones, saludos ni explicaciones.
    """

    # Construimos la lista de contenidos mixtos
    contenido_llamada = [prompt_base]

    # 1. Si hay texto manual
    if ingredientes_texto.strip():
        contenido_llamada.append(f"Ingredientes y comentarios añadidos por texto manual: {ingredientes_texto}")

    # 2. Si hay imágenes fijas
    if lista_imagenes_bytes:
        contenido_llamada.append("Analiza estas fotos fijas de la nevera:")
        for img_bytes in lista_imagenes_bytes:
            objeto_imagen = types.Part.from_bytes(
                data=img_bytes,
                mime_type="image/jpeg"
            )
            contenido_llamada.append(objeto_imagen)

    # 3. Si hay vídeo en movimiento
    if video_bytes is not None:
        contenido_llamada.append("Analiza este barrido en vídeo de la nevera:")
        objeto_video = types.Part.from_bytes(
            data=video_bytes,
            mime_type="video/mp4"
        )
        contenido_llamada.append(objeto_video)

    # 4. Si hay una nota de voz (NUEVO)
    if audio_bytes is not None and mime_audio is not None:
        contenido_llamada.append(
            "Escucha atentamente este mensaje de voz donde el usuario menciona ingredientes o peticiones:")
        objeto_audio = types.Part.from_bytes(
            data=audio_bytes,
            mime_type=mime_audio
        )
        contenido_llamada.append(objeto_audio)

    # Llamada nativa unificada a Gemini 2.5 Flash
    response = client.models.generate_content(
        model=MODEL,
        contents=contenido_llamada,
        config=types.GenerateContentConfig(
            system_instruction=prompt_base,
            temperature=0.1
        )
    )
    return response.text.strip()