
import unittest
from unittest.mock import patch, MagicMock
from src.utils.document_split import DocumentSplit

class TestDocumentSplit(unittest.TestCase):

    @patch('src.utils.document_split.PyPDFLoader')
    def test_init(self, mock_pypdf_loader):
        """Test that PyPDFLoader is called with the correct path on init."""
        mock_loader_instance = MagicMock()
        mock_pypdf_loader.return_value = mock_loader_instance
        
        path = "/fake/path/to/doc.pdf"
        doc_split = DocumentSplit(path)
        
        mock_pypdf_loader.assert_called_once_with(path)
        mock_loader_instance.load.assert_called_once()
        self.assertEqual(doc_split.docs, mock_loader_instance.load.return_value)

    @patch('src.utils.document_split.PyPDFLoader')
    @patch('src.utils.document_split.RecursiveCharacterTextSplitter')
    def test_split_chunks(self, mock_splitter, mock_pypdf_loader):
        """Test that split_chunks calls the text splitter with the correct documents."""
        # Arrange
        mock_docs = [MagicMock()]
        mock_pypdf_loader.return_value.load.return_value = mock_docs
        
        mock_splitter_instance = MagicMock()
        mock_splitter.return_value = mock_splitter_instance
        
        doc_split = DocumentSplit("/fake/path")
        
        # Act
        doc_split.split_chunks()
        
        # Assert
        mock_splitter.assert_called_once_with(
            chunk_size=1000, 
            chunk_overlap=150, 
            add_start_index=False
        )
        mock_splitter_instance.split_documents.assert_called_once_with(mock_docs)

if __name__ == '__main__':
    unittest.main()
