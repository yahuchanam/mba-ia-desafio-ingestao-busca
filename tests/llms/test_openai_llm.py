
import unittest
from unittest.mock import patch, MagicMock
from src.llms.openai_llm import OpenAILLMStrategy

class TestOpenAILLMStrategy(unittest.TestCase):

    @patch('src.llms.openai_llm.os.getenv')
    @patch('src.llms.openai_llm.ChatOpenAI')
    def test_get_llm(self, mock_chat_openai, mock_getenv):
        """Test that ChatOpenAI is initialized with the correct model name."""
        # Arrange
        mock_getenv.return_value = "test-model-name"
        strategy = OpenAILLMStrategy()
        
        # Act
        llm = strategy.get_llm()
        
        # Assert
        mock_getenv.assert_called_once_with("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
        mock_chat_openai.assert_called_once_with(model="test-model-name")
        self.assertEqual(llm, mock_chat_openai.return_value)

    @patch('src.llms.openai_llm.os.getenv')
    @patch('src.llms.openai_llm.ChatOpenAI')
    def test_get_llm_default(self, mock_chat_openai, mock_getenv):
        """Test that ChatOpenAI uses the default model name when env var is not set."""
        # Arrange
        mock_getenv.return_value = None
        strategy = OpenAILLMStrategy()
        
        # Act
        strategy.get_llm()
        
        # Assert
        mock_chat_openai.assert_called_once_with(model="gpt-3.5-turbo")

if __name__ == '__main__':
    unittest.main()
