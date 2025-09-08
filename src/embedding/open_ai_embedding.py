import os
from langchain_openai import OpenAIEmbeddings
from embedding.embedding_strategy import EmbeddingStrategy


class OpenAIEmbeddingStrategy(EmbeddingStrategy):
  """
  Estratégia para criar embeddings usando a API da OpenAI.
  """
  def get_embeddings(self):
    return OpenAIEmbeddings(
        model=os.getenv("GOOGLE_EMBEDDING_MODEL", "text-embedding-3-small")
    )