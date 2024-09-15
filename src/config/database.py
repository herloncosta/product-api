import mysql.connector
import os


def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL", err)
        return None
