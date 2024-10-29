import numpy as np
from openai import OpenAI
from config import OPENAI_API_KEY, EMBEDDING_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def embed_query(query: str) -> np.ndarray:
    response = client.embeddings.create(input=query, model=EMBEDDING_MODEL)
    embedding = response.data[0].embedding
    return np.array(embedding)
