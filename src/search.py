from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from llms.llm_manager import LLMManager
from utils.load_env import EnvManager
from vector_db.vector_db_manager import VectorDBManager

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

class SearchManager:
  def __init__(self):
    EnvManager.load_env()
    self.vector_db_manager = VectorDBManager()
    self.llm_manager = LLMManager()
    self.rag_chain = self._create_rag_chain()
    
  def format_docs(self, docs):
      return "\n\n".join(doc.page_content for doc in docs)

  def _create_rag_chain(self):
    retriever = RunnableLambda(
      lambda question: self.vector_db_manager.query(query=question, k=10)
    )

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    llm = self.llm_manager.get_llm()

    return (
      {"contexto": retriever | self.format_docs, "pergunta": RunnablePassthrough()}
      | prompt
      | llm
      | StrOutputParser()
    )

  def search_prompt(self, question: str) -> str:
    return self.rag_chain.invoke(question)

