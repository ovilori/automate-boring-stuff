from mysql.connector import connection
import pyodbc
def create_connection(server,database,username,password):
    try:
        cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
        ';DATABASE='+database+
        ';UID='+username+
        ';PWD='+ password,
        autocommit=True)
        print('Connection to MSSQL DB server successful!')
    except pyodbc.OperationalError as e:
        print(f"The error '{e}' occurred")
    return cnxn
server = input('Enter the database server e.g.localhost\sqlexpress: ')
database = input('Enter the database you wish to connect to: ')
username = input('Enter your username: ')
password = input('Enter your password: ')

connection = create_connection(server,database,username,password)
cursor = connection.cursor()
create_database = 'CREATE DATABASE Solarwinds'
""" create_table = 'CREATE TABLE Result(SN int, STUDENT_NAME varchar(255),\
                REGISTRATION_NO varchar(255),\
                COURSE varchar(255),\
                UNIT int,\
                SCORE int,\
                POINT int,\
                GRADE varchar(2),\
                TOTAL_UNITS int,\
                TOTAL_LOAD_POINTS int,\
                SEMESTER_GPA decimal(1,2),\
                CLASS_OF_DEGREE varchar,\
                );'  """
create_table = 'CREATE TABLE Reporting (Date datetime, BranchName varchar, VendorName varchar, AverageAvailability int);'
#cursor.execute(create_database)
#delete_table = 'DROP TABLE Result;'
cursor.execute(create_table)
#cursor.execute(delete_table)