import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import embed_query
from models import TemplateSuggestion
from config import SIMILARITY_THRESHOLD, TEMPLATE_TRIGGER
from openai import OpenAI
from typing import Dict
import numpy as np
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
query_embeddings: Dict[str, np.ndarray] = {}
G = nx.Graph()

def suggest_template(query: str, related_queries: str) -> TemplateSuggestion:
    prompt = (
        f"Create a structured template suggestion based on the following:\n\n"
        f"Query: '{query}'\n"
        f"Related queries: {related_queries}\n\n"
        "Template requirements:\n"
        "- Template name\n"
        "- Description\n"
        "- List of variables with names and descriptions"
    )

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "Generate a structured template suggestion."},
            {"role": "user", "content": prompt},
        ],
        response_format=TemplateSuggestion,
    )

    template = completion.choices[0].message.parsed
    return template


def add_query_to_graph(query: str, graph: nx.Graph = G) -> None:
    if query in query_embeddings:
        embedding = query_embeddings[query]
    else:
        embedding = embed_query(query)
        query_embeddings[query] = embedding

    graph.add_node(query, embedding=embedding)

    for existing_query, data in graph.nodes(data=True):
        if existing_query == query:
            continue

        similarity = cosine_similarity(embedding.reshape(1, -1), data['embedding'].reshape(1, -1))[0][0]
        if similarity >= SIMILARITY_THRESHOLD:
            graph.add_edge(query, existing_query, weight=similarity)

    neighbors = list(graph.neighbors(query))
    if len(neighbors) >= TEMPLATE_TRIGGER:
        related_queries = ', '.join(neighbors)
        print(f"Suggestion: Create a template for queries similar to '{query}'. Related queries: {related_queries}")
        
        template_suggestion = suggest_template(query, related_queries)
        if template_suggestion:
            print("\nSuggested template:\n", template_suggestion)
