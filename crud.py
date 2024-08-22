# crud_operations.py

from flask import jsonify
from DB_connector import get_mongo_connection, get_mysql_connection

# MongoDB CRUD Operations for Employee

def create_employee(data):
    client, employee_collection = get_mongo_connection()
    employee_collection.insert_one(data)
    client.close()
    return jsonify(message="Employee created successfully in MongoDB"), 201

def read_employees():
    client, employee_collection = get_mongo_connection()
    employees = list(employee_collection.find({}, {'_id': False}))
    client.close()
    return jsonify(employees)

def update_employee(name, data):
    client, employee_collection = get_mongo_connection()
    employee_collection.update_one({'name': name}, {'$set': data})
    client.close()
    return jsonify(message="Employee updated successfully in MongoDB")

def delete_employee(name):
    client, employee_collection = get_mongo_connection()
    employee_collection.delete_one({'name': name})
    client.close()
    return jsonify(message="Employee deleted successfully from MongoDB")

# MySQL CRUD Operations for Department

def create_department(data):
    conn, cursor = get_mysql_connection()
    query = "INSERT INTO departments (name, location) VALUES (%s, %s)"
    values = (data['name'], data['location'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(message="Department created successfully in MySQL"), 201

def read_departments():
    conn, cursor = get_mysql_connection()
    cursor.execute("SELECT * FROM departments")
    departments = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(departments)

def update_department(id, data):
    conn, cursor = get_mysql_connection()
    query = "UPDATE departments SET name = %s, location = %s WHERE id = %s"
    values = (data['name'], data['location'], id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(message="Department updated successfully in MySQL")

def delete_department(id):
    conn, cursor = get_mysql_connection()
    query = "DELETE FROM departments WHERE id = %s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(message="Department deleted successfully from MySQL")
