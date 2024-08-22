# app.py

from flask import Flask, request
from crud import create_employee, read_employees, update_employee, delete_employee
from crud import create_department, read_departments, update_department, delete_department

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask with MongoDB (Employee) and MySQL (Department)!"

# Routes for MongoDB (Employee)
@app.route('/employee/create', methods=['POST'])
def employee_create():
    data = request.json
    return create_employee(data)

@app.route('/employee/read', methods=['GET'])
def employee_read():
    return read_employees()

@app.route('/employee/update/<string:name>', methods=['PUT'])
def employee_update(name):
    data = request.json
    return update_employee(name, data)

@app.route('/employee/delete/<string:name>', methods=['DELETE'])
def employee_delete(name):
    return delete_employee(name)

# Routes for MySQL (Department)
@app.route('/department/create', methods=['POST'])
def department_create():
    data = request.json
    return create_department(data)

@app.route('/department/read', methods=['GET'])
def department_read():
    return read_departments()

@app.route('/department/update/<int:id>', methods=['PUT'])
def department_update(id):
    data = request.json
    return update_department(id, data)

@app.route('/department/delete/<int:id>', methods=['DELETE'])
def department_delete(id):
    return delete_department(id)

if __name__ =='__main__':
    app.run(debug=True,port=8000)
