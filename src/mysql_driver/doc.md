# MySQLDriver - Documentação

## Visão Geral

O `MySQLDriver` é uma classe Python projetada para facilitar a interação com um banco de dados MySQL. Ela oferece métodos para realizar operações básicas de banco de dados, como consultas, inserções, atualizações e deleções. A classe utiliza a biblioteca `mysql-connector-python` para conectar-se ao MySQL.

## Instalação

Certifique-se de ter o Python instalado em seu ambiente. Para instalar a biblioteca necessária, use o seguinte comando:

```bash
pip install mysql-connector-python
```

## Uso Básico

### Importação e Criação de Instância

```python
from mysql_driver import MySQLDriver

# Crie uma instância do driver
db = MySQLDriver(host='localhost', user='root', password='sua_senha', database='seu_banco')
```

### Conectar ao Banco de Dados

```python
# Conecte-se ao banco de dados
db.connect()
```

### Desconectar do Banco de Dados

```python
# Desconecte-se do banco de dados
db.disconnect()
```

### Executar uma Consulta SQL

```python
# Execute uma consulta SQL
result = db.execute_query('SELECT * FROM usuarios')
print(result)
```

### Executar uma Consulta Não SQL (INSERT, UPDATE, DELETE)

```python
# Insira dados em uma tabela
db.insert('usuarios', {'nome': 'João', 'idade': 30})

# Atualize dados em uma tabela
db.update('usuarios', {'idade': 31}, {'nome': 'João'})

# Delete dados de uma tabela
db.delete('usuarios', {'nome': 'João'})
```

## Métodos Disponíveis

### `__init__(self, host, user, password, database)`

- **Descrição:** Inicializa uma nova instância do `MySQLDriver`.
- **Parâmetros:**
  - `host` (str): O endereço do servidor MySQL.
  - `user` (str): O nome de usuário para autenticação.
  - `password` (str): A senha do usuário.
  - `database` (str): O nome do banco de dados a ser usado.

### `connect(self)`

- **Descrição:** Estabelece a conexão com o banco de dados MySQL.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao conectar.

### `disconnect(self)`

- **Descrição:** Fecha a conexão com o banco de dados MySQL.
- **Exceções:** 
  - `None`: Não lança exceções específicas.

### `execute_query(self, query, params=None)`

- **Descrição:** Executa uma consulta SQL e retorna o resultado.
- **Parâmetros:**
  - `query` (str): A consulta SQL a ser executada.
  - `params` (tuple, opcional): Parâmetros a serem passados para a consulta.
- **Retorno:** `list of dict`: Uma lista de dicionários onde cada dicionário representa uma linha do resultado.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao executar a consulta.

### `execute_non_query(self, query, params=None)`

- **Descrição:** Executa uma consulta SQL que não retorna dados (e.g., INSERT, UPDATE, DELETE).
- **Parâmetros:**
  - `query` (str): A consulta SQL a ser executada.
  - `params` (tuple, opcional): Parâmetros a serem passados para a consulta.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao executar a consulta.

### `insert(self, table, data)`

- **Descrição:** Insere dados em uma tabela específica.
- **Parâmetros:**
  - `table` (str): Nome da tabela onde os dados serão inseridos.
  - `data` (dict): Um dicionário contendo os dados a serem inseridos. As chaves são os nomes das colunas e os valores são os valores a serem inseridos.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao executar a consulta.

### `update(self, table, data, where)`

- **Descrição:** Atualiza dados em uma tabela específica.
- **Parâmetros:**
  - `table` (str): Nome da tabela onde os dados serão atualizados.
  - `data` (dict): Um dicionário contendo os dados a serem atualizados. As chaves são os nomes das colunas e os valores são os novos valores.
  - `where` (dict): Um dicionário contendo as condições para a atualização. As chaves são os nomes das colunas e os valores são os valores das condições.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao executar a consulta.

### `delete(self, table, where)`

- **Descrição:** Deleta dados de uma tabela específica.
- **Parâmetros:**
  - `table` (str): Nome da tabela de onde os dados serão deletados.
  - `where` (dict): Um dicionário contendo as condições para a exclusão. As chaves são os nomes das colunas e os valores são os valores das condições.
- **Exceções:** 
  - `mysql.connector.Error`: Lançado se houver um erro ao executar a consulta.

## Exceções

O driver usa a classe `mysql.connector.Error` para capturar erros durante a execução das consultas. Certifique-se de tratar essas exceções para uma melhor gestão de erros em seu aplicativo.

## Exemplos

### Exemplo Completo

```python
from mysql_driver import MySQLDriver

# Crie uma instância do driver
db = MySQLDriver(host='localhost', user='root', password='sua_senha', database='seu_banco')

# Conecte-se ao banco de dados
db.connect()

# Insira dados em uma tabela
db.insert('usuarios', {'nome': 'Maria', 'idade': 28})

# Atualize dados em uma tabela
db.update('usuarios', {'idade': 29}, {'nome': 'Maria'})

# Consulte dados
result = db.execute_query('SELECT * FROM usuarios')
print(result)

# Delete dados
db.delete('usuarios', {'nome': 'Maria'})

# Desconecte-se do banco de dados
db.disconnect()
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções e novas funcionalidades. Crie um pull request ou abra uma issue para discutir qualquer nova ideia ou problema.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).