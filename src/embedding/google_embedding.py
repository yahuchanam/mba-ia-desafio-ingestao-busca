import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from embedding.embedding_strategy import EmbeddingStrategy

class GoogleEmbeddingStrategy(EmbeddingStrategy):
  """
  Estratégia para criar embeddings usando a API do Google (Gemini).
  """
  def get_embeddings(self):
    return GoogleGenerativeAIEmbeddings(
        model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/text-embedding-004")
    )