# Crossfit Competition API

Este projeto é parte do desafio proposto pela DIO para o Bootcamp de Python Backend com IA, para criar uma poderosa API assíncrona para uma academia que organiza competições de crossfit, utilizando o framework FastAPI.

## Tecnologias Utilizadas

- **FastAPI (async)**
- **Alembic**
- **SQLAlchemy**
- **Pydantic**
- **PostgreSQL**
- **Docker**

## Funcionalidades

### Query Parameters nos Endpoints

Os endpoints da API permitem a adição de parâmetros de consulta para filtrar os resultados. 

- **nome**: Filtra os atletas pelo nome.
- **cpf**: Filtra os atletas pelo CPF.

### Customização de Resposta

Os endpoints `get all` da API foram customizados para retornar informações específicas.

- **nome**
- **centro_treinamento**
- **categoria**

### Manipulação de Exceções de Integridade dos Dados

Cada módulo/tabela da API possui manipulação de exceções de integridade dos dados. Caso ocorra um conflito de integridade (por exemplo, um CPF duplicado), a API retorna a seguinte mensagem de erro:

- **Mensagem**: "Já existe um atleta cadastrado com o cpf: x"
- **status_code**: 303

### Paginação

Foi adicionada paginação aos endpoints utilizando a biblioteca `fastapi-pagination`. A paginação pode ser controlada pelos seguintes parâmetros:

- **limit**: Limita o número de registros retornados.
- **offset**: Define o deslocamento (quantos registros devem ser pulados antes de começar a retornar os resultados).

## Como Executar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/crossfit-competition-api.git

2. Navegue até o diretório do projeto:
    ```sh
    cd crossfit-competition-api

3. Inicie os contêineres Docker:
    ```sh
    docker-compose up

4. Acesse a documentação interativa da API:
Abra o navegador e vá para http://localhost:8000/docs


















