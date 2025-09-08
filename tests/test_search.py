
import unittest
from unittest.mock import patch, MagicMock
from src.search import SearchManager, PROMPT_TEMPLATE

class TestSearchManager(unittest.TestCase):

    @patch('src.search.EnvManager')
    @patch('src.search.VectorDBManager')
    @patch('src.search.LLMManager')
    @patch('src.search.ChatPromptTemplate')
    @patch('src.search.RunnableLambda')
    @patch('langchain_core.runnables.base.RunnableSequence')
    def test_init_and_create_rag_chain(self, mock_runnable_seq, mock_runnable_lambda, mock_prompt_template, mock_llm_manager, mock_vector_db_manager, mock_env_manager):
        """Test initialization of SearchManager and the RAG chain creation."""
        # Arrange
        mock_llm = MagicMock()
        mock_llm_manager.return_value.get_llm.return_value = mock_llm
        
        mock_retriever = MagicMock()
        mock_runnable_lambda.return_value = mock_retriever
        
        mock_prompt = MagicMock()
        mock_prompt_template.from_template.return_value = mock_prompt

        # Act
        manager = SearchManager()

        # Assert
        mock_env_manager.load_env.assert_called_once()
        mock_vector_db_manager.assert_called_once()
        mock_llm_manager.assert_called_once()
        
        # Test chain creation
        mock_runnable_lambda.assert_called_once()
        mock_prompt_template.from_template.assert_called_once_with(PROMPT_TEMPLATE)
        mock_llm_manager.return_value.get_llm.assert_called_once()
        
        # Check that the chain was assembled with the correct components
        # This is a bit complex due to the chaining, so we check key parts
        self.assertIsNotNone(manager.rag_chain)

    @patch('src.search.EnvManager')
    @patch('src.search.VectorDBManager')
    @patch('src.search.LLMManager')
    def test_search_prompt(self, mock_llm_manager, mock_vector_db_manager, mock_env_manager):
        """Test that search_prompt invokes the RAG chain with the question."""
        # Arrange
        manager = SearchManager()
        manager.rag_chain = MagicMock()
        question = "What is the meaning of life?"
        
        # Act
        manager.search_prompt(question)
        
        # Assert
        manager.rag_chain.invoke.assert_called_once_with(question)

    def test_format_docs(self):
        """Test the format_docs method."""
        # Arrange
        manager = SearchManager()
        doc1 = MagicMock()
        doc1.page_content = "Hello"
        doc2 = MagicMock()
        doc2.page_content = "World"
        docs = [doc1, doc2]
        
        # Act
        result = manager.format_docs(docs)
        
        # Assert
        self.assertEqual(result, "Hello\n\nWorld")

if __name__ == '__main__':
    unittest.main()
