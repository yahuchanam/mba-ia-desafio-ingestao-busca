import os
from llms.llm_strategy import LLMStrategy
from llms.openai_llm import OpenAILLMStrategy
from llms.google_llm import GoogleLLMStrategy

class LLMManager:
  """
  Gerencia a seleção da estratégia de LLM apropriada.
  """
  def __init__(self):
    self._strategy: LLMStrategy = self._select_strategy()

  def _select_strategy(self) -> LLMStrategy:
    """
    Seleciona a estratégia de LLM com base nas variáveis de ambiente, 
    preferindo a OpenAI se disponível.
    """
    if os.getenv("OPENAI_API_KEY"):
      return OpenAILLMStrategy()
    
    return GoogleLLMStrategy()

  def get_llm(self):
    """
    Retorna a instância da LLM configurada.
    """
    return self._strategy.get_llm()
