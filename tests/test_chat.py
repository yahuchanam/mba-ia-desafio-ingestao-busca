
import unittest
from unittest.mock import patch, MagicMock
from src.chat import main

class TestChat(unittest.TestCase):

    @patch('src.chat.EnvManager')
    @patch('src.chat.SearchManager')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_loop(self, mock_print, mock_input, mock_search_manager, mock_env_manager):
        """Test the main loop of the chat application."""
        # Arrange
        mock_search_instance = MagicMock()
        mock_search_manager.return_value = mock_search_instance
        mock_search_instance.search_prompt.return_value = "Test answer"
        
        # Simulate user entering one question and then 'exit'
        mock_input.side_effect = ["Test question", "exit"]
        
        # Act
        main()
        
        # Assert
        mock_env_manager.load_env.assert_called_once()
        mock_search_manager.assert_called_once()
        
        # Check that input was called twice
        self.assertEqual(mock_input.call_count, 2)
        
        # Check that search_prompt was called with the question
        mock_search_instance.search_prompt.assert_called_once_with("Test question")
        
        # Check that the response was printed
        mock_print.assert_called_once_with("RESPOSTA: Test answer\n")

    @patch('src.chat.EnvManager')
    @patch('src.chat.SearchManager')
    @patch('builtins.input', side_effect=EOFError) # Simulate Ctrl+D
    def test_main_loop_eof_error(self, mock_input, mock_search_manager, mock_env_manager):
        """Test that the loop breaks on EOFError."""
        # Act
        main()
        
        # Assert
        mock_env_manager.load_env.assert_called_once()
        mock_search_manager.assert_called_once()
        mock_input.assert_called_once()

    @patch('src.chat.EnvManager')
    @patch('src.chat.SearchManager')
    @patch('builtins.input', side_effect=KeyboardInterrupt) # Simulate Ctrl+C
    def test_main_loop_keyboard_interrupt(self, mock_input, mock_search_manager, mock_env_manager):
        """Test that the loop breaks on KeyboardInterrupt."""
        # Act
        main()
        
        # Assert
        mock_env_manager.load_env.assert_called_once()
        mock_search_manager.assert_called_once()
        mock_input.assert_called_once()

if __name__ == '__main__':
    unittest.main()
