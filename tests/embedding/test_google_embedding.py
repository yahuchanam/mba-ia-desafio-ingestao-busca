
import os
import unittest
from unittest.mock import patch

from embedding.google_embedding import GoogleEmbeddingStrategy

class TestGoogleEmbeddingStrategy(unittest.TestCase):

    @patch('src.embedding.goggle_embedding.GoogleGenerativeAIEmbeddings')
    @patch.dict(os.environ, {"GOOGLE_EMBEDDING_MODEL": "test-model"})
    def test_get_embeddings(self, mock_google_embeddings):
        """Test that get_embeddings returns a configured GoogleGenerativeAIEmbeddings instance."""
        # Arrange
        strategy = GoogleEmbeddingStrategy()
        
        # Act
        embeddings = strategy.get_embeddings()
        
        # Assert
        mock_google_embeddings.assert_called_once_with(model="test-model")
        self.assertEqual(embeddings, mock_google_embeddings.return_value)

    @patch('src.embedding.goggle_embedding.GoogleGenerativeAIEmbeddings')
    @patch.dict(os.environ, {}, clear=True)
    def test_get_embeddings_default_model(self, mock_google_embeddings):
        """Test that get_embeddings uses the default model when the env var is not set."""
        # Arrange
        strategy = GoogleEmbeddingStrategy()
        
        # Act
        strategy.get_embeddings()
        
        # Assert
        mock_google_embeddings.assert_called_once_with(model="models/text-embedding-004")

if __name__ == '__main__':
    unittest.main()
