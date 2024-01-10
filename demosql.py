""" import mysql.connector

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "sa", "xxxxxxxxxxxxxxxxxxxxxxxxx") """

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost\sqlexpress' 
#database = 'MyDNNDatabase' 
username = 'sa' 
password = 'xxxxxxxxxxxx' 
try:
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
        #';DATABASE='+database+
        ';UID='+username+
        ';PWD='+ password,
        autocommit=True)
    print('Connection to MSSQL DB successful!')
    cursor = cnxn.cursor()
except pyodbc.OperationalError as e:
    print(f"The error '{e}' occurred")
#create_db = 'CREATE DATABASE PythonDB'
#cursor.execute(create_db)

