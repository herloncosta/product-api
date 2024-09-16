import mysql.connector
from mysql.connector import Error


class MySQLDriver():
    """
    Um driver simples para se conectar e manipular dados de um banco MySQL.

    Atributos:
    --------------
    host : str
        Endereço do banco.
    user : str
        O nome do usuário para autenticação.
    password : str
        Senha para autenticação.
    database
        Nome do banco da ser utilizado durante a conexão.
    connection : mysql.connector.connection_cext.CMySQLConnection

    Métodos:
    --------------
    connect()
        Estabelece uma conexão com o banco de dados.
    disconnect()
        Fecha a conexão com o banco de dados.
    execute_query(query, params=None)
        Executa uma consulta SQL e retorna o resultado.
    execute_non_query(query, params=None)
        Executa uma consulta SQL que não retorna dados. (Exemplo: INSERT, UPDATE, DELETE).
    insert()
        Insere dados em uma tabela específica.
    update()
        Atualiza dados em uma tabela específica.
    delete()
        Remove dados em uma tabela específica.
    """

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connection to MySQL DB successful.")
            return True
        except Error as e:
            print(f"The error '{e}' occurred.")
            return False

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed.")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"The error '{e}' occurred.")
            return None

    def execute_non_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            cursor.close()
            print("Query execution completed successfully.")
        except Error as e:
            print(f"Query execution error: '{e}' occurred.")

    def insert(self, table, data):
        """
        Insere dados em uma tabela específica

        Parâmetros
        --------------
        table: str
            Nome da tabela onde os dados serão inseridos.
        data: dict
            Um dicionário contendo os dados a serem inseridos. As chaves são as
            colunas e os valores são os valores a serem inseridos.

        Lança:
        --------------
        mysql.connector.Error
            Se houver um erro ao executar a consulta.
        """
        columns = ", ".join(data.keys())
        values_placeholder = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values_placeholder})"
        self.execute_non_query(query, tuple(data.values()))

    def update(self, table, data, where):
        """
        Atualiza dados em uma tabela específica

        Parâmetros
        --------------
        table: str
            Nome da tabela onde os dados serão atualizados.
        data: dict
            Um dicionário contendo os dados a serem atualizados. As chaves são as
            colunas e os valores são os novos valores.
        where: dict
            Um dicionário contendo as condições para a atualização.As chaves são
            as colunas e os valores são os valores das condições.

        Lança:
        --------------
        mysql.connector.Error
            Se houver um erro ao executar a consulta.
        """
        set_clause = ", ".join([f"{k} = %s" for k in data.keys()])
        where_clause = " AND ".join([f"{k} = %s" for k in where.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.execute_non_query(query, tuple(
            data.values()) + tuple(where.values()))

    def delete(self, table, where):
        """
        Remove dados em uma tabela específica

        Parâmetros
        --------------
        table: str
            Nome da tabela onde os dados serão removidos.
        where: dict
            Um dicionário contendo as condições para a remoção.As chaves são
            as colunas e os valores são os valores das condições.

        Lança:
        --------------
        mysql.connector.Error
            Se houver um erro ao executar a consulta.
        """
        where_clause = " AND ".join([f"{k} = %s" for k in where.keys()])
        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.execute_non_query(query, tuple(where.values()))
