
import unittest
from unittest.mock import patch, MagicMock
from src.ingest import ingest_pdf

class TestIngestPdf(unittest.TestCase):

    @patch('src.ingest.load_env')
    @patch('src.ingest.DocumentSplit')
    @patch('src.ingest.VectorDBManager')
    def test_ingest_pdf(self, mock_vector_db_manager, mock_document_split, mock_load_env):
        """Test the main ingest_pdf function orchestrates calls correctly."""
        # Arrange
        mock_chunks = [MagicMock()]
        mock_document_split.return_value.split_chunks.return_value = mock_chunks
        
        mock_db_manager_instance = MagicMock()
        mock_vector_db_manager.return_value = mock_db_manager_instance
        
        # Act
        ingest_pdf()
        
        # Assert
        mock_load_env.assert_called_once()
        mock_document_split.assert_called_once_with("./document.pdf")
        mock_document_split.return_value.split_chunks.assert_called_once()
        mock_vector_db_manager.assert_called_once()
        mock_db_manager_instance.save.assert_called_once_with(mock_chunks)

if __name__ == '__main__':
    unittest.main()
