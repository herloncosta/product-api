import mysql.connector
import os

db_config = {
    "host": os.getenv('MYSQL_HOST'),
    "user": os.getenv('MYSQL_USER'),
    "password": os.getenv('MYSQL_PASSWORD'),
    "database": os.getenv('MYSQL_DATABASE')
}


def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print("Error connecting to MySQL", err)
        return None
