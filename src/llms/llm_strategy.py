from abc import ABC, abstractmethod

class LLMStrategy(ABC):
  """
  Define a interface comum para todas as estratégias de LLM.
  """
  @abstractmethod
  def get_llm(self):
      """
      Método que deve ser implementado pelas estratégias concretas
      para retornar um objeto de LLM configurado.
      """
      pass
