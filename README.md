# Desafio MBA Engenharia de Software com IA - Full Cycle

## Objetivo

Você deve entregar um software capaz de:

Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

### Exemplo no CLI

#### Faça sua pergunta:

```bash
PERGUNTA: Qual o faturamento da empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.
```

#### Perguntas fora do contexto:

```bash
PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

## Pré-requisitos

Antes de começar, garanta que você tenha as seguintes ferramentas instaladas em seu sistema:

-   Python 3.10+
-   Docker
-   Docker Compose

## Pré-requisitos

Antes de começar, garanta que você tenha as seguintes ferramentas instaladas em seu sistema:

-   Python 3.10+
-   Docker
-   Docker Compose

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

### Crie e ative um ambiente virtual

```bash
python3 -m venv venv
```

### No Linux ou macOS:

```bash
source venv/bin/activate
```

### No Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

### Ou no Windows (Command Prompt):

```bash
.\venv\Scripts\activate.bat
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

## Suba o container Docker com o PGVector

```bash
docker compose up -d
```

## Executando a Ingestão de Documentos

Para executar o script de ingestão de documentos PDF, utilize o seguinte comando:

```bash
python src/ingest.py 
```

O script irá ler o caminho do PDF a partir da variável `PDF_PATH` no seu arquivo `.env`. Se não estiver definida, ele usará o arquivo `document.pdf` na raiz do projeto como padrão.

## Executando o CLI

Para executar o CLI, utilize o seguinte comando:

```bash
python src/chat.py 
```

Após isso faça suas perguntas relacionadas ao PDF que foi feita a ingestão.
Para sair basta digitar `exit` ou `quit`.

## Executando os Testes Unitários

Para executar os testes unitários e garantir que tudo está funcionando como esperado, utilize o seguinte comando:

```bash
PYTHONPATH=./src python -m unittest discover tests
```
