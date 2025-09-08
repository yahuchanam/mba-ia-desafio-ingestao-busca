
import os
import unittest
from unittest.mock import patch
from src.utils.load_env import EnvManager

class TestEnvManager(unittest.TestCase):

    def setUp(self):
        """Reset the _loaded flag before each test."""
        EnvManager._loaded = False

    @patch.dict(os.environ, {
        "DATABASE_URL": "test_db_url",
        "PG_VECTOR_COLLECTION_NAME": "test_collection",
        "OPENAI_API_KEY": "test_api_key"
    })
    def test_load_env_success_with_openai(self):
        """Test that load_env runs successfully when all required env vars are set."""
        try:
            EnvManager.load_env()
        except RuntimeError:
            self.fail("EnvManager.load_env() raised RuntimeError unexpectedly!")

    @patch.dict(os.environ, {
        "DATABASE_URL": "test_db_url",
        "PG_VECTOR_COLLECTION_NAME": "test_collection",
        "GOOGLE_API_KEY": "test_api_key"
    })
    def test_load_env_success_with_google(self):
        """Test that load_env runs successfully when all required env vars are set."""
        try:
            EnvManager.load_env()
        except RuntimeError:
            self.fail("EnvManager.load_env() raised RuntimeError unexpectedly!")

    @patch.dict(os.environ, {}, clear=True)
    def test_load_env_missing_mandatory_key(self):
        """Test that load_env raises RuntimeError when a mandatory key is missing."""
        with self.assertRaisesRegex(RuntimeError, "A variável de ambiente obrigatória 'DATABASE_URL' não está definida."):
            EnvManager.load_env()

    @patch.dict(os.environ, {
        "DATABASE_URL": "test_db_url",
        "PG_VECTOR_COLLECTION_NAME": "test_collection"
    }, clear=True)
    def test_load_env_missing_api_key(self):
        """Test that load_env raises RuntimeError when no API key is provided."""
        with self.assertRaisesRegex(RuntimeError, "É necessário definir pelo menos uma das seguintes variáveis de ambiente: OPENAI_API_KEY, GOOGLE_API_KEY"):
            EnvManager.load_env()

    @patch('src.utils.load_env.load_dotenv')
    def test_load_env_called_once(self, mock_load_dotenv):
        """Test that load_dotenv is only called once."""
        EnvManager.load_env()
        EnvManager.load_env()
        mock_load_dotenv.assert_called_once()

if __name__ == '__main__':
    unittest.main()
