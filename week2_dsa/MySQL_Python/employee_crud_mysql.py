import pymysql
from tabulate import tabulate

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(
            host='localhost',
            user='root',
            password='SS762902',
            database='sunny_db',
            port=3306,
            charset='utf8'
        )
        print('Database Connected')
    except:
        print('Database Connection Failed')
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print('DB Disconnected')
    except:
        print('DB Disconnection Failed')

def create_table(connection):
    query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        designation VARCHAR(30),
        phone_number BIGINT UNIQUE,
        salary FLOAT,
        commission FLOAT DEFAULT 0,
        years_of_experience TINYINT,
        technology VARCHAR(30) NOT NULL
    )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table Created')
        cursor.close()
    except:
        print('Table Creation Failed')

def read_all_employees(connection):
    query = 'SELECT * FROM employees'
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = []
        for column in cursor.description:
            headers.append(column[0])
        print(tabulate(
            rows,
            headers=headers,
            tablefmt="fancy_grid",   
            missingval="N/A",        
            numalign="center",       
            stralign="center"        
        ))
        print('All Rows Retrieved')
        cursor.close()
    except:
        print('Row Retrieval Failed')

def read_employees_details():
    name = input("Enter employee name: ")
    designation = input("Enter employee designation: ")
    phone_number = int(input("Enter employee phone number: "))
    salary = float(input("Enter employee salary: "))
    commission = float(input("Enter employee commission: "))
    years_of_experience = int(input("Enter employee years of experience: "))
    technology = input("Enter employee technology: ")
    return(name, designation, phone_number, salary, commission, years_of_experience, technology)


def insert_employee(connection):
    employee_data = read_employees_details()
    query = '''INSERT INTO employees(name, designation, phone_number, salary, commission, years_of_experience, technology) 
    VALUES(%s, %s, %s, %s, %s, %s, %s)'''

    try:
        cursor = connection.cursor()
        value = cursor.execute(query,employee_data)
        connection.commit()
        if value == 1:
            print("Employee inserted Successfully.")
        else:
            print("Failed to insert employee.") 
        cursor.close()
    except:
        print("Failed to insert employee.")

def update_employee(connection):
    id = int(input('Enter id of the employee to be updated: '))
    salary = float(input('Enter employee salary: '))
    years_of_experience = input('Enter employee years of experience: ')
    query = f'update employees set years_of_experience = {years_of_experience}, salary = {salary} where id = {id}'

    try:
        cursor = connection.cursor()
        value = cursor.execute(query)
        connection.commit()
        if value == 1:
            print(f'Employee with id = {id} updated.')
        else:
            print(f"Employee with id = {id} not found.")
    except:
        print('Employee update failed')

def delete_employee(connection):
    id = int(input('Enter id of the employee to be updated: '))
    query = (f'DELETE FROM employees where id = {id}')

    try:
        cursor = connection.cursor()
        value = cursor.execute(query)
        connection.commit()
        if value == 1:
            print(f"Employee with id = {id} deleted.")
        else:
            print(f"Employee with id = {id} not found.")
    except:
        print('Employee deletion failed')

