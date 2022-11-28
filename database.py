import mysql.connector
from mysql.connector import Error

# criando/logando um server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name, 
            user = user_name,
            password = user_password
        )
        print('Successful server connection!!!')
    except Error as err:
        print(f'Ihh, We found some Error: {err}!')
    return connection


# criar banco de dados db 
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f'Database {query} was created with successful!!!')
    except Exception as excp:
        print(f'Exception, we found an error: {excp}')


# acessando banco de dados db criado
def create_database_connection(host_name, user_name, user_password, db_name):
    connection = None  
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print('MySQL was connected with successful!!!')
    except Error as err:
        print(f'Ihh, We found some Error: {err}!')
    return connection


# escrever queries
# def execute_query(con_database, cursor, query):
#     try:
#         cursor.execute(query)
#         con_database.commit()
#         print(f'{query} creates with succsseful!')
#     except Error as err:
#         print(f'Error: Ihh, {err}')

# # ler queries
# def read_query(cursor, query):
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as err:
#         print(f'Error: {err}')