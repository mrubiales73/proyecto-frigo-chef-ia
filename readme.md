# 🤖🍳 FRIGO-CHEF IA — Sistema Multi-Agente Multimodal

FRIGO-CHEF IA es una plataforma inteligente orientada a la gestión eficiente de alimentos en el hogar, el diseño automatizado de recetas y el fomento del residuo cero (sostenibilidad). 

La aplicación está desarrollada de forma nativa sobre la SDK oficial de Google (`google-genai`), aprovechando las capacidades del modelo **Gemini 2.5 Flash** en Vertex AI mediante una arquitectura desacoplada y modular de sub-agentes especializados.

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
└── credentials/
    ├── credentials.json        <-- 📁 Carpeta con fichero credenciales json
│
└── streamlit/
    ├── config.toml             <-- 📁 Carpeta con fichero configuración streamlit
    │
│
└── agentes/                    <-- 📁 Carpeta con los componentes de la IA
    ├── __init__.py             
    ├── agente_orquestador.py   <-- 👑 Coordinador y validador del Contrato JSON
    ├── agente_detector.py      <-- 🕵️‍♂️ Agente 1: Detector Multimodal (Guardrail de Entrada)
    ├── agente_recetas.py       <-- 👨‍🍳 Agente 2: Creador de Recetas personalizadas
    ├── agente_lista_compra.py  <-- 🛒 Agente 3: Gestor de Ingredientes faltantes opcionales
    ├── agent_nutricional.py    <-- 🥗 Agente 4: Evaluador de Balance Nutricional y Alertas
    └── agente_desperdicio.py   <-- ♻️ Agente 5: Control del Desperdicio y Sostenibilidad



🚀 Capacidades Multimodales Avanzadas (Roadmap)
Gracias al uso nativo de Gemini 2.5 Flash, la aplicación está diseñada para expandir su canal de entrada (Intake) hacia los siguientes formatos sin alterar la lógica de negocio de los agentes posteriores:

Visión por Computador (Múltiples Fotos): Carga simultánea de 2 a 3 imágenes para evitar puntos ciegos en los estantes o cajones de la nevera.

Análisis de Vídeo en Movimiento: Barridos cortos de vídeo (2-3 segundos, formato .mp4) donde el modelo procesa los frames temporalmente para identificar de forma precisa el stock de alimentos.

Entrada de Voz Nativa: Procesamiento directo de archivos de audio (.wav, .mp3) para capturar peticiones contextuales complejas del usuario (ej: "Quiero cenar algo ligero con base de pasta...") sin necesidad de transcripción intermedia (STT).



🛠️ Sistema Instalación y Despliegue Local
Requisitos Previos
Python 3.10 o superior.

Entorno virtual configurado en PyCharm.

1. Instalar dependencias
Abre la terminal de PyCharm e instala los paquetes necesarios desde el archivo de requerimientos:

Bash
pip install -r requirements.txt


2. Variables de Entorno y Credenciales
Crea un archivo .env en la raíz del proyecto para configurar el acceso seguro a Vertex AI a través de tu cuenta de servicio:

Fragmento de código
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_APPLICATION_CREDENTIALS=".\credentials\credentials.json"


3. Ejecutar la Aplicación
Lanza el servidor local de Streamlit desde tu terminal de PyCharm para abrir la interfaz gráfica:

Bash
streamlit run Interfaz_streamlit.py

