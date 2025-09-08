
import unittest
from unittest.mock import patch, MagicMock
from src.llms.llm_manager import LLMManager
from src.llms.openai_llm import OpenAILLMStrategy
from src.llms.google_llm import GoogleLLMStrategy

class TestLLMManager(unittest.TestCase):

    @patch('src.llms.llm_manager.os.getenv')
    @patch('src.llms.llm_manager.OpenAILLMStrategy')
    def test_select_strategy_openai(self, mock_openai_strategy, mock_getenv):
        """Test that OpenAILLMStrategy is selected when OPENAI_API_KEY is present."""
        mock_getenv.return_value = "fake_api_key"
        manager = LLMManager()
        self.assertIsInstance(manager._strategy, OpenAILLMStrategy)
        mock_openai_strategy.assert_called_once()

    @patch('src.llms.llm_manager.os.getenv', return_value=None)
    @patch('src.llms.llm_manager.GoogleLLMStrategy')
    def test_select_strategy_google(self, mock_google_strategy, mock_getenv):
        """Test that GoogleLLMStrategy is selected when OPENAI_API_KEY is not present."""
        manager = LLMManager()
        self.assertIsInstance(manager._strategy, GoogleLLMStrategy)
        mock_google_strategy.assert_called_once()

    def test_get_llm(self):
        """Test that get_llm calls the strategy's get_llm method."""
        manager = LLMManager()
        mock_strategy = MagicMock()
        manager._strategy = mock_strategy
        
        llm = manager.get_llm()
        
        mock_strategy.get_llm.assert_called_once()
        self.assertEqual(llm, mock_strategy.get_llm.return_value)

if __name__ == '__main__':
    unittest.main()
