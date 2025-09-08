import os

from langchain_postgres import PGVector
from embedding.embedding_strategy import EmbeddingStrategy
from embedding.google_embedding import GoogleEmbeddingStrategy
from embedding.open_ai_embedding import OpenAIEmbeddingStrategy
from xml.dom.minidom import Document

class VectorDBManager:
  """
  Gerencia o salvamento de documentos no banco de dados vetorial,
  utilizando a estratégia de embedding apropriada.
  """
  def __init__(self):
    self._strategy: EmbeddingStrategy = self._select_strategy()

  def _select_strategy(self) -> EmbeddingStrategy:
    """
    Seleciona a estratégia de embedding com base nas variáveis de ambiente, 
    preferindo a OpenAI se disponível.
    """
    if os.getenv("OPENAI_API_KEY"):
      return OpenAIEmbeddingStrategy()
    
    return GoogleEmbeddingStrategy()

  def save(self, enriched: list[Document]):
    """
    Salva os documentos enriquecidos no banco de dados vetorial.
    """    
    embeddings = self._strategy.get_embeddings()
    
    collection_name = os.getenv("PG_VECTOR_COLLECTION_NAME")
    connection_url = os.getenv("DATABASE_URL")

    store = PGVector(
      embeddings=embeddings,
      collection_name=collection_name,
      connection=connection_url,
      use_jsonb=True,
    )
    
    ids = [f"doc-{i}" for i in range(len(enriched))]

    store.add_documents(documents=enriched, ids=ids)
    print(f"✅ Documentos salvos com sucesso na coleção '{collection_name}'.")