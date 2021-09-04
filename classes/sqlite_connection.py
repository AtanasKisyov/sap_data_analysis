import sqlite3
from sqlite3 import Error


class SQLiteConnection:

    component_information_path = "/DB/component_information.sqlite"
    material_information_path = "/DB/material_information.sqlite"

    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection

    @staticmethod
    def create_table(connection):
        create_material_table = "CREATE TABLE IF NOT EXISTS materials " \
                                "(material_number TEXT NOT NULL, material_type TEXT);"

        SQLiteConnection.execute_query(connection, create_material_table)

    @staticmethod
    def create_materials(*material_information):
        material_number = material_information[0]
        material_type = material_information[1]
        result = f"INSERT INTO " \
                 f"materials (material_number, material_type) " \
                 f"VALUES " \
                 f"('{material_number}', '{material_type}');"
        return result

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")

    @staticmethod
    def execute_read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
