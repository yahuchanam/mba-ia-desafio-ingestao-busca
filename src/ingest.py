import os

from utils.document_split import DocumentSplit
from utils.load_env import EnvManager
from vector_db.vector_db_manager import VectorDBManager

def ingest_pdf():
    """
    Função principal para ingestão do PDF.
    """
    EnvManager.load_env()
    pdf_path = os.getenv("PDF_PATH") or "./document.pdf"
    doc_split = DocumentSplit(pdf_path)
    chunks = doc_split.split_chunks()
    vector_db_manager = VectorDBManager()
    vector_db_manager.save(chunks)

if __name__ == "__main__":
    ingest_pdf()