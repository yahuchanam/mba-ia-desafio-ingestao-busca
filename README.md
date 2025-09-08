# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.

## Configuração do Ambiente

Antes de executar a aplicação, você precisa configurar as variáveis de ambiente.

1.  Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`:

    ```bash
    cp .env.example .env
    ```

2.  Abra o arquivo `.env` e preencha as variáveis com os seus valores. Em especial, certifique-se de que a `DATABASE_URL` esteja configurada corretamente para apontar para o seu banco de dados PostgreSQL com a extensão `pgvector` habilitada. Se estiver usando o Docker Compose fornecido, o valor deve ser:

    ```
    DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
    ```

## Instale as dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

## Executando a Ingestão de Documentos

Para executar o script de ingestão de documentos PDF, utilize o seguinte comando:

```bash
python src/ingest.py 
```

O script irá ler o caminho do PDF a partir da variável `PDF_PATH` no seu arquivo `.env`. Se não estiver definida, ele usará o arquivo `document.pdf` na raiz do projeto como padrão.

## Executando os Testes Unitários

Para executar os testes unitários e garantir que tudo está funcionando como esperado, utilize o seguinte comando:

```bash
PYTHONPATH=./src python -m unittest discover tests
```
