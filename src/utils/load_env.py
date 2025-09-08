import os
from dotenv import load_dotenv

class EnvManager:
    _loaded = False

    @staticmethod
    def load_env():
        """
        Verifica se as variáveis de ambiente obrigatórias e opcionais estão definidas.
        Garante que o .env seja carregado apenas uma vez.
        """
        if EnvManager._loaded:
            return

        # Constrói o caminho absoluto para o arquivo .env na raiz do projeto
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
        load_dotenv(dotenv_path=dotenv_path)

        # Variáveis que são SEMPRE obrigatórias
        mandatory_keys = ("DATABASE_URL", "PG_VECTOR_COLLECTION_NAME")
        for key in mandatory_keys:
            if not os.getenv(key):
                raise RuntimeError(f"A variável de ambiente obrigatória '{key}' não está definida.")

        # Variáveis onde PELO MENOS UMA é obrigatória
        api_keys = ("OPENAI_API_KEY", "GOOGLE_API_KEY")
        if not any(os.getenv(key) for key in api_keys):
            raise RuntimeError(f"É necessário definir pelo menos uma das seguintes variáveis de ambiente: {', '.join(api_keys)}")
        
        EnvManager._loaded = True
