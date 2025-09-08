
import unittest
from unittest.mock import patch, MagicMock
from src.llms.google_llm import GoogleLLMStrategy

class TestGoogleLLMStrategy(unittest.TestCase):

    @patch('src.llms.google_llm.os.getenv')
    @patch('src.llms.google_llm.ChatGoogleGenerativeAI')
    def test_get_llm(self, mock_chat_google, mock_getenv):
        """Test that ChatGoogleGenerativeAI is initialized with the correct model name."""
        # Arrange
        mock_getenv.return_value = "test-model-name"
        strategy = GoogleLLMStrategy()
        
        # Act
        llm = strategy.get_llm()
        
        # Assert
        mock_getenv.assert_called_once_with("GOOGLE_MODEL_NAME", "gemini-flash")
        mock_chat_google.assert_called_once_with(model="test-model-name")
        self.assertEqual(llm, mock_chat_google.return_value)

    @patch('src.llms.google_llm.os.getenv')
    @patch('src.llms.google_llm.ChatGoogleGenerativeAI')
    def test_get_llm_default(self, mock_chat_google, mock_getenv):
        """Test that ChatGoogleGenerativeAI uses the default model name when env var is not set."""
        # Arrange
        mock_getenv.return_value = None
        strategy = GoogleLLMStrategy()
        
        # Act
        strategy.get_llm()
        
        # Assert
        mock_chat_google.assert_called_once_with(model="gemini-flash")

if __name__ == '__main__':
    unittest.main()
