# 🤖🍳 FRIGO-CHEF IA — Sistema Multi-Agente Multimodal

FRIGO-CHEF IA es una plataforma inteligente orientada a la gestión eficiente de alimentos en el hogar, el diseño automatizado de recetas y el fomento del residuo cero (sostenibilidad). 

La aplicación está desarrollada de forma nativa sobre la SDK oficial de Google (`google-genai`), aprovechando las capacidades del modelo **Gemini 2.5 Flash** en Agent Platform mediante una arquitectura desacoplada y modular de sub-agentes especializados.

---

## 🗺️ Arquitectura del Sistema (Multi-Agent Cascading)

En lugar de utilizar frameworks monolíticos o pesados (como LangChain), este proyecto implementa un patrón de diseño **nativo en cascada**, donde cada fase del análisis está delegada en un sub-agente experto con responsabilidades únicas (*Single Responsibility Principle*). 

La interfaz de usuario interactúa directamente con el **Agente Orquestador**, el cual coordina el flujo síncrono y consolida las salidas en un contrato JSON estricto.

```text
Frigo-Chef_multiagentes/

│
├── .venv/                      
├── Interfaz_streamlit.py       <-- Interfaz Principal (Streamlit)
├── Conexion.py                 <-- Setup, Conexión y Configuración del Proyecto
├── README.md                   <-- Documentación del proyecto
├── requirements.txt            <-- Librerías del sistema
│
└── streamlit/
    ├── config.toml             <-- Carpeta con fichero configuración streamlit
    │── secret.toml             <-- Carpeta con fichero configuración streamlit
│
└── agentes/                    <-- 📁 Carpeta con los componentes de la IA
    ├── __init__.py             
    ├── agente_orquestador.py   <-- 👑 Coordinador y validador del Contrato JSON
    ├── agente_detector.py      <-- 🕵️‍♂️ Agente 1: Detector Multimodal (Guardrail de Entrada)
    ├── agente_recetas.py       <-- 👨‍🍳 Agente 2: Creador de Recetas personalizadas
    ├── agente_lista_compra.py  <-- 🛒 Agente 3: Gestor de Ingredientes faltantes opcionales
    ├── agent_nutricional.py    <-- 🥗 Agente 4: Evaluador de Balance Nutricional y Alertas
    └── agente_desperdicio.py   <-- ♻️ Agente 5: Control del Desperdicio y Sostenibilidad
```    


## 🚀 Capacidades Multimodales Operativas (Implementadas)

Gracias a la integración nativa con el SDK de **Gemini 2.5 Flash** a través de Vertex AI, la aplicación procesa de manera directa y simultánea diferentes tipos de entrada (*Intake*) sin requerir capas de traducción o transcripción externas, consolidando la información antes de transferirla a la lógica de negocio de los agentes:

*   **Visión por Computador (Múltiples Fotos):** Soporte para la carga simultánea de 2 a 3 imágenes de forma paralela. Esto permite consolidar el inventario visual de la nevera cubriendo diferentes ángulos, evitando los puntos ciegos de los estantes o los cajones cerrados.
*   **Análisis de Vídeo en Movimiento:** Procesamiento nativo de barridos cortos de vídeo (2-3 segundos en formato `.mp4`). El modelo analiza la secuencia de fotogramas de forma temporal para identificar con precisión el stock real de alimentos, marcas y formatos en una sola toma fluida.
*   **Entrada de Voz Nativa:** Procesamiento directo de archivos de audio (`.wav`, `.mp3`). El sistema analiza semánticamente las peticiones contextuales complejas del usuario (ej: *"Quiero cenar algo ligero con base de pasta..."*) extrayendo la intención directamente del archivo de voz, eliminando la latencia y la necesidad de usar servicios de transcripción intermedia (Speech-to-Text).



## 🛠️ Sistema Instalación y Despliegue Local

Requisitos Previos
Python 3.10 o superior.

Entorno virtual configurado en PyCharm.

1.- Instalar dependencias
Abre la terminal de PyCharm e instala los paquetes necesarios desde el archivo de requerimientos:

Bash
pip install -r requirements.txt

2.- Credenciales
Crea un archivo .streamlit/secrets.toml en la raíz del proyecto en el cual debes poner la cuenta de servicio en formato TOML en lugar de JSON

3.- Configuración streamlit
Crea un archivo .streamlit/config.toml en la raíz del proyecto en el cual configuras los parámetros de la interfaz streamlit.
(Configurar tamaños máximos de los archivos que se pueden subir, configurar formatos, etc...)

4.- Ejecutar la aplicación
Lanza el servidor local de Streamlit desde tu terminal de PyCharm para abrir la interfaz gráfica:

Bash
streamlit run Interfaz_streamlit.py
