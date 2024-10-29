# Smart Templates Application

Esta aplicación está diseñada para detectar similitudes en consultas hechas por usuarios y sugerir plantillas estructuradas cuando se identifica un grupo de consultas relacionadas. Utiliza la API de OpenAI para analizar las consultas y generar plantillas, y emplea un grafo para visualizar relaciones entre consultas similares.

## Características Principales

- **Análisis de similitudes**: Evalúa la similitud entre consultas usando `cosine similarity`.
- **Generación de plantillas**: Sugiere plantillas para grupos de consultas similares utilizando modelos de lenguaje de OpenAI.
- **Visualización de relaciones**: Crea un grafo para visualizar consultas y conexiones basadas en similitudes.

## Requisitos

- Python 3.10 o superior
- Conexión a internet para acceder a la API de OpenAI

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/smart_templates.git
cd smart_templates
```

### 2. Instalar Dependencias

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 3. Configuración de la API de OpenAI

En el archivo `config.py`, agrega tu clave de API de OpenAI:

```python
# config.py
OPENAI_API_KEY = "your_openai_api_key"
EMBEDDING_MODEL = "text-embedding-ada-002"
SIMILARITY_THRESHOLD = 0.7                  # Ajusta según el nivel de similitud deseado
TEMPLATE_TRIGGER = 5                        # Número de conexiones para sugerir una plantilla
```

## Estructura del Proyecto

- **`main.py`**: Archivo principal que ejecuta la aplicación.
- **`config.py`**: Configuración de claves API y parámetros.
- **`models.py`**: Define el modelo `TemplateSuggestion` para la structured output de OpenAI.
- **`embeddings.py`**: Genera embeddings para cada consulta usando la API de OpenAI.
- **`graph_manager.py`**: Añade consultas al grafo y calcula similitudes entre ellas.
- **`visualization.py`**: Visualiza el grafo de consultas.
- **`queries.py`**: Lista de consultas para los tests.

## Uso

### Ejecución

1. Navega al directorio del proyecto.
2. Ejecuta el archivo principal:

```bash
python main.py
```

### Funcionalidad

La aplicación toma la lista de consultas de `queries.py`, genera un embedding para cada consulta y evalúa similitudes usando `cosine similarity`. Si se identifican conexiones suficientes con una consulta, se sugiere una plantilla usando la API de OpenAI.

### Ejemplo de Salida

La salida muestra el progreso y la sugerencia de plantilla:

```
Suggestion: Create a template for queries similar to 'Teach me how to make pasta'. Related queries: How to make pasta?, I want to make pasta, ...
Suggested template:
 template_name='Recipe Template' description='Template for cooking recipes.' variables=['ingredients', 'time', 'difficulty']
```

### Visualización del Grafo

La aplicación dibuja un grafo de consultas relacionadas. Los nodos representan consultas, y las aristas indican similitud basada en el umbral definido en `config.py`.

## Personalización

### Modificar el Umbral de Similitud

El umbral de similitud en `config.py` determina cuándo dos consultas son consideradas similares:

```python
SIMILARITY_THRESHOLD = 0.7  # Aumenta o disminuye para ajustar el nivel de similitud
```

### Cambiar el Modelo de Embedding

En `config.py`, puedes especificar el modelo de embeddings de OpenAI:

```python
EMBEDDING_MODEL = "text-embedding-ada-002"
```
