
# Smart Templates Application

This application is a proof of concept for an intelligent algorithm designed to detect patterns in user behavior. It identifies similarities in user queries and suggests structured templates when a cluster of related queries is found. It leverages OpenAI's API for query analysis and template generation, and utilizes a graph to visualize relationships between similar queries.

---

## Key Features

- **Similarity Analysis**: Evaluates query similarity using `cosine similarity`.
- **Template Generation**: Suggests templates for clusters of similar queries via OpenAI's language models.
- **Relationship Visualization**: Creates a graph to display queries and connections based on similarity.

---

## Requirements

- Python 3.10 or higher
- Internet connection to access OpenAI's API

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your_user/smart_templates.git
cd smart_templates
```

### 2. Install Dependencies

Run the following command to install all required dependencies:

```bash
pip install -r requirements.txt
```

### 3. OpenAI API Configuration

Add your OpenAI API key in the `config.py` file:

```python
# config.py
OPENAI_API_KEY = "your_openai_api_key"
EMBEDDING_MODEL = "text-embedding-ada-002"
SIMILARITY_THRESHOLD = 0.7                  # Adjust based on desired similarity level
TEMPLATE_TRIGGER = 5                        # Number of connections to trigger a template suggestion
```

---

## Project Structure

- **`main.py`**: Main script to run the application.
- **`config.py`**: Configuration for API keys and parameters.
- **`models.py`**: Defines the `TemplateSuggestion` model for OpenAI's structured output.
- **`embeddings.py`**: Generates embeddings for each query using OpenAI's API.
- **`graph_manager.py`**: Adds queries to the graph and calculates similarities between them.
- **`visualization.py`**: Visualizes the query graph.
- **`queries.py`**: Contains a list of test queries.

---

## Usage

### Running the Application

1. Navigate to the project directory.
2. Run the main script:

```bash
python main.py
```

### Functionality

The application processes the list of queries in `queries.py`, generates embeddings for each query, and evaluates similarities using `cosine similarity`. When a sufficient number of connections are detected for a query, it triggers a template suggestion through OpenAI's API.

---

### Example Output

The output displays progress and template suggestions:

```
Suggestion: Create a template for queries similar to 'Teach me how to make pasta'. Related queries: How to make pasta?, I want to make pasta, ...
Suggested template:
 template_name='Recipe Template' description='Template for cooking recipes.' variables=['ingredients', 'time', 'difficulty']
```

---

### Graph Visualization

The application generates a graph of related queries. Nodes represent queries, and edges indicate similarity based on the threshold defined in `config.py`.

---

## Customization

### Adjusting Similarity Threshold

The similarity threshold in `config.py` determines when two queries are considered similar:

```python
SIMILARITY_THRESHOLD = 0.7  # Increase or decrease to fine-tune similarity detection
```

### Changing the Embedding Model

In `config.py`, you can specify the OpenAI embedding model:

```python
EMBEDDING_MODEL = "text-embedding-ada-002"
```
