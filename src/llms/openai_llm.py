import os
from langchain_openai import ChatOpenAI
from llms.llm_strategy import LLMStrategy

class OpenAILLMStrategy(LLMStrategy):
  """
  Estratégia para criar LLMs usando a API da OpenAI.
  """
  def get_llm(self):
    return ChatOpenAI(model=os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo"))
