from .authentication import authenticate

client = authenticate()

def create_lead_embedding(lead_data: dict) -> dict:
    """
    Create and store lead data embeddings using Groclake's Vectorlake.
    """
    embedding = client.vectorlake.create_embedding(data=lead_data)
    client.vectorlake.store_embedding(embedding_id=lead_data["name"], embedding=embedding)
    return embedding

def get_similar_leads(lead_name: str, top_k: int = 5) -> list:
    """
    Retrieve similar leads from Groclake's Vectorlake.
    """
    return client.vectorlake.query_embedding(embedding_id=lead_name, top_k=top_k)
