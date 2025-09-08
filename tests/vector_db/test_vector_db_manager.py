
import unittest
from unittest.mock import patch, MagicMock
from src.vector_db.vector_db_manager import VectorDBManager
from src.embedding.open_ai_embedding import OpenAIEmbeddingStrategy
from src.embedding.google_embedding import GoogleEmbeddingStrategy

class TestVectorDBManager(unittest.TestCase):

    @patch('src.vector_db.vector_db_manager.os.getenv')
    @patch('src.vector_db.vector_db_manager.OpenAIEmbeddingStrategy')
    def test_select_strategy_openai(self, mock_openai_strategy, mock_getenv):
        """Test that OpenAI strategy is selected when API key is present."""
        mock_getenv.return_value = "fake_api_key"
        manager = VectorDBManager()
        self.assertIsInstance(manager._strategy, OpenAIEmbeddingStrategy)
        mock_openai_strategy.assert_called_once()

    @patch('src.vector_db.vector_db_manager.os.getenv', return_value=None)
    @patch('src.vector_db.vector_db_manager.GoogleEmbeddingStrategy')
    def test_select_strategy_google(self, mock_google_strategy, mock_getenv):
        """Test that Google strategy is selected when OpenAI key is not present."""
        manager = VectorDBManager()
        self.assertIsInstance(manager._strategy, GoogleEmbeddingStrategy)
        mock_google_strategy.assert_called_once()

    @patch('src.vector_db.vector_db_manager.PGVector')
    @patch('src.vector_db.vector_db_manager.VectorDBManager._select_strategy')
    @patch('src.vector_db.vector_db_manager.os.getenv')
    def test_get_store(self, mock_getenv, mock_select_strategy, mock_pgvector):
        """Test that PGVector is initialized with correct parameters."""
        mock_strategy_instance = MagicMock()
        mock_embeddings = MagicMock()
        mock_strategy_instance.get_embeddings.return_value = mock_embeddings
        mock_select_strategy.return_value = mock_strategy_instance
        
        mock_getenv.side_effect = lambda key: {
            "PG_VECTOR_COLLECTION_NAME": "test_collection",
            "DATABASE_URL": "test_url"
        }.get(key)

        manager = VectorDBManager()
        
        mock_pgvector.assert_called_once_with(
            embeddings=mock_embeddings,
            collection_name="test_collection",
            connection="test_url",
            use_jsonb=True
        )
        self.assertEqual(manager.store, mock_pgvector.return_value)

    @patch('src.vector_db.vector_db_manager.VectorDBManager._select_strategy')
    @patch('src.vector_db.vector_db_manager.VectorDBManager._get_store')
    def test_save(self, mock_get_store, mock_select_strategy):
        """Test that store.add_documents is called with correct documents and ids."""
        mock_store_instance = MagicMock()
        mock_get_store.return_value = mock_store_instance
        
        manager = VectorDBManager()
        
        mock_docs = [MagicMock(), MagicMock()]
        manager.save(mock_docs)
        
        expected_ids = ["doc-0", "doc-1"]
        mock_store_instance.add_documents.assert_called_once_with(documents=mock_docs, ids=expected_ids)

    @patch('src.vector_db.vector_db_manager.VectorDBManager._select_strategy')
    @patch('src.vector_db.vector_db_manager.VectorDBManager._get_store')
    def test_query(self, mock_get_store, mock_select_strategy):
        """Test that store.similarity_search_with_score is called and results are processed."""
        mock_store_instance = MagicMock()
        mock_doc1 = MagicMock()
        mock_doc2 = MagicMock()
        mock_store_instance.similarity_search_with_score.return_value = [(mock_doc1, 0.9), (mock_doc2, 0.8)]
        mock_get_store.return_value = mock_store_instance

        manager = VectorDBManager()
        
        query_text = "test query"
        k_value = 5
        result_docs = manager.query(query_text, k=k_value)
        
        mock_store_instance.similarity_search_with_score.assert_called_once_with(query_text, k=k_value)
        self.assertEqual(result_docs, [mock_doc1, mock_doc2])

if __name__ == '__main__':
    unittest.main()
