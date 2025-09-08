import os
from langchain_google_genai import ChatGoogleGenerativeAI
from llms.llm_strategy import LLMStrategy

class GoogleLLMStrategy(LLMStrategy):
  """
  Estratégia para criar LLMs usando a API do Google (Gemini).
  """
  def get_llm(self):
    return ChatGoogleGenerativeAI(model=os.getenv("GOOGLE_MODEL_NAME", "gemini-flash"))
