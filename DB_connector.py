# db_connector.py

from pymongo import MongoClient
import mysql.connector

# MongoDB Configuration for Employee
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['company_db']
    employee_collection = db['employees']
    return client, employee_collection

# MySQL Configuration for Department
def get_mysql_connection():
    conn = mysql.connector.connect(
        host='localhost',
        database='company_db',
        user='your_mysql_user',
        password='your_mysql_password'
    )
    cursor = conn.cursor()
    return conn, cursor
