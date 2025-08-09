from langchain_ollama import OllamaEmbeddings  # New import path

def getEmbedding(model_name='granite-embedding:30m'):
    # Verify model exists first
    try:
        embeddings = OllamaEmbeddings(
            model=model_name,
            temperature=0  # Required parameter
        )
        # Test connection
        embeddings.embed_documents(["test"])
        return embeddings
    except Exception as e:
        raise ValueError(f"Model {model_name} failed: {str(e)}")
