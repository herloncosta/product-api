# API de Gestão de Produtos

Esta API foi desenvolvida em Python utilizando o framework Flask, com um banco de dados MySQL rodando em um container Docker. A API permite o cadastro, listagem, busca, atualização e exclusão de produtos. O servidor de produção utiliza o Gunicorn.

## Endpoints

### Cadastrar um Produto
- **Método:** `POST`
- **URL:** `http://127.0.0.1:5000/products`
- **Headers:** `Content-Type: application/json`
  
#### Exemplo de Requisição:

```json
{
    "name": "produto novo id",
    "description": "registrando novo produto",
    "price": 201
}
```

#### Resposta de Sucesso:
- **Código:** `201 Created`
- **Body:** Detalhes do produto cadastrado.

---

### Listar Todos os Produtos
- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/products/`
- **Headers:** `Content-Type: application/json`

#### Exemplo de Resposta:

```json
[
  {
    "id": 1,
    "name": "Produto A",
    "description": "Descrição do Produto A",
    "price": 150
  },
  {
    "id": 2,
    "name": "Produto B",
    "description": "Descrição do Produto B",
    "price": 200
  }
]
```

#### Resposta de Sucesso:
- **Código:** `200 OK`
- **Body:** Lista de todos os produtos cadastrados.

---

### Buscar um Produto por ID
- **Método:** `GET`
- **URL:** `http://127.0.0.1:5000/products/{id}`
- **Headers:** `Content-Type: application/json`

#### Exemplo de Resposta:

```json
{
  "id": 8,
  "name": "Produto X",
  "description": "Descrição do Produto X",
  "price": 250
}
```

#### Resposta de Sucesso:
- **Código:** `200 OK`
- **Body:** Detalhes do produto.

#### Resposta de Erro:
- **Código:** `404 Not Found`
- **Body:** Produto não encontrado.

---

### Atualizar um Produto
- **Método:** `PUT`
- **URL:** `http://127.0.0.1:5000/products/{id}`
- **Headers:** `Content-Type: application/json`

#### Exemplo de Requisição:

```json
{
    "name": "produto novo nome",
    "description": "atualizando produto",
    "price": 202
}
```

#### Resposta de Sucesso:
- **Código:** `200 OK`
- **Body:** Detalhes do produto atualizado.

#### Resposta de Erro:
- **Código:** `404 Not Found`
- **Body:** Produto não encontrado.

---

### Excluir um Produto
- **Método:** `DELETE`
- **URL:** `http://127.0.0.1:5000/products/{id}`
- **Headers:** `Content-Type: application/json`

#### Resposta de Sucesso:
- **Código:** `204 No Content`

#### Resposta de Erro:
- **Código:** `404 Not Found`
- **Body:** Produto não encontrado.

---

## Setup do Ambiente

### Requisitos
- **Python 3.x**
- **Flask**
- **MySQL**
- **Docker**

### Configuração do Docker

O banco de dados MySQL é executado em um container Docker com a seguinte configuração:

```yaml
version: '3.1'
services:
  db:
    image: mysql:latest
    ports:
      - "3306:3306"
    volumes:
      - products:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=admin
      - MYSQL_DATABASE=products
volumes:
  products:
```

### Servidor de Produção com Gunicorn

A API é executada com o Gunicorn para melhorar o desempenho e a escalabilidade:

- **Bind:** `0.0.0.0:5000`
- **Workers:** 2
- **Timeout:** 30 segundos

#### Exemplo de comando para iniciar o Gunicorn:

```bash
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

## Como Executar o Projeto

1. Clone o repositório.
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Inicie o Docker:
    ```bash
    docker-compose up
    ```
5. Execute a aplicação:
    ```bash
    flask run
    ```

## Contribuição

Sinta-se à vontade para abrir _issues_ ou enviar _pull requests_ para melhorias ou correções.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).