import mysql.connector
from mysql.connector import Error


class MySQLDriver():
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
        columns = ", ".join(data.keys())
        values_placeholder = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values_placeholder})"
        self.execute_non_query(query, tuple(data.values()))

    def update(self, table, data, where):
        set_clause = ", ".join([f"{k} = %s" for k in data.keys()])
        where_clause = " AND ".join([f"{k} = %s" for k in where.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.execute_non_query(query, tuple(
            data.values()) + tuple(where.values()))

    def delete(self, table, where):
        where_clause = " AND ".join([f"{k} = %s" for k in where.keys()])
        query = f"DELETE FROM {table} WHERE {where_clause}"
        self.execute_non_query(query, tuple(where.values()))
