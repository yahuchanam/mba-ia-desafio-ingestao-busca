from abc import ABC, abstractmethod

class EmbeddingStrategy(ABC):
  """
  Define a interface comum para todas as estratégias de embedding.
  """
  @abstractmethod
  def get_embeddings(self):
      """
      Método que deve ser implementado pelas estratégias concretas
      para retornar um objeto de embedding configurado.
      """
      pass
    