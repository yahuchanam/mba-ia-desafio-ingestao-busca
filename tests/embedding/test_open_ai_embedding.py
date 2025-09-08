
import os
import unittest
from unittest.mock import patch
from src.embedding.open_ai_embedding import OpenAIEmbeddingStrategy

class TestOpenAIEmbeddingStrategy(unittest.TestCase):

    @patch('src.embedding.open_ai_embedding.OpenAIEmbeddings')
    @patch.dict(os.environ, {"GOOGLE_EMBEDDING_MODEL": "test-model-for-openai"})
    def test_get_embeddings(self, mock_openai_embeddings):
        """Test that get_embeddings returns a configured OpenAIEmbeddings instance."""
        # Arrange
        strategy = OpenAIEmbeddingStrategy()
        
        # Act
        embeddings = strategy.get_embeddings()
        
        # Assert
        mock_openai_embeddings.assert_called_once_with(model="test-model-for-openai")
        self.assertEqual(embeddings, mock_openai_embeddings.return_value)

    @patch('src.embedding.open_ai_embedding.OpenAIEmbeddings')
    @patch.dict(os.environ, {}, clear=True)
    def test_get_embeddings_default_model(self, mock_openai_embeddings):
        """Test that get_embeddings uses the default model when the env var is not set."""
        # Arrange
        strategy = OpenAIEmbeddingStrategy()
        
        # Act
        strategy.get_embeddings()
        
        # Assert
        mock_openai_embeddings.assert_called_once_with(model="text-embedding-3-small")

if __name__ == '__main__':
    unittest.main()
