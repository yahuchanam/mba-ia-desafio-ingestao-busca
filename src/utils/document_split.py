import os
from xml.dom.minidom import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

class DocumentSplit():
  """
  Classe responsável por carregar e dividir documentos em chunks menores.
  """

  def __init__(self, path: str):
    """
    Inicializa a classe com o caminho do PDF.
    """
    self.path = path
    self.docs = self._load_pdf()

  def _load_pdf(self) -> list[Document]:
    """"
    Carrega o PDF e retorna uma lista de Documentos.
    """
    return PyPDFLoader(self.path).load()

  def split_chunks(self) -> list[Document]:
    """
    Divide os documentos em chunks menores.
    """
    chunk_size = int(os.getenv("CHUNK_SIZE", 1000))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 150))
    splits = RecursiveCharacterTextSplitter(
      chunk_size=chunk_size, 
      chunk_overlap=chunk_overlap, 
      add_start_index=False
    )
    
    if not splits:
      raise SystemExit(0)
    
    return splits.split_documents(self.docs)