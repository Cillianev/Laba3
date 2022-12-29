import mysql.connector 
from mysql.connector import Error 
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection succssesful!")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection succsessfuly")
    except Error as err:
        print(f"Error: '{err}'")
        return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created succssefully")
    except Error as err:
        print(f"Error: '{err}'")