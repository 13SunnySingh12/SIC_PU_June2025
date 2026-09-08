"""What is this written for?

The data-access layer behind the person REST API. `Person` is the plain record
the API passes around, and `Db_operations` wraps every SQL statement the API
needs: create the table, insert, update, delete, search by id, list all.

Keeping the SQL here means main.py only deals with HTTP concerns. Credentials
are read from the environment, or from a .env file one folder up - see
.env.example there. Nothing is hardcoded.
"""

import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

# Reads coursework/04_databases_and_apis/.env if it exists. Real environment
# variables take precedence, so nothing is overridden in CI or production.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name       = name
        self.gender     = gender
        self.dob        = dob
        self.location   = location

    def __str__(self):
        print(f'Name:{self.name}, Location:{self.location}')

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.Connect(
                host=os.environ.get('MYSQL_HOST', 'localhost'),
                port=int(os.environ.get('MYSQL_PORT', '3306')),
                user=os.environ.get('MYSQL_USER', 'root'),
                password=os.environ.get('MYSQL_PASSWORD', ''),
                database=os.environ.get('MYSQL_DATABASE', 'sunny_db'),
                charset='utf8',
            )
            print('DB connected')
            return connection
        except:
            print('DB connection failed')

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('DB disconnected')
        except:
            print('Error while disconnecting DB')

    def create_db(self):
        connection = self.connect_db()
        query = 'create database IF NOT EXISTS sunny_db;'
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('DB created')
        self.disconnect_db(connection)

    def create_table(self):
        connection = self.connect_db()
        query = "create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(32) not null, gender char check(gender in('m','M', 'f','F')), location varchar(32), dob date);"
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('Table created')
        self.disconnect_db(connection)

    def read_person_details(self):
        name = input('Enter person name: ')
        gender = input('Enter person gender: ')[0]
        location = input('Enter person location: ')
        dob = input('Enter person date of borth(yyyy-mm-dd): ')
        return (name, gender, location, dob)

    def insert_row(self, person):
        query = 'insert into persons(name, gender, location, dob) values(%s, %s, %s, %s);'
        person_tuple = (person.name, person.gender, person.location, person.dob)
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, person_tuple)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        id = self.get_latest_row_id()
        return id

    def update_row(self, data):
        query = 'update persons set name = %s, gender = %s, location = %s, dob = %s where id = %s'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def delete_row(self, id):
        query = 'delete from persons where id = %s'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (id,))
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            print(f'Person with id = {id} deleted')
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def search_row(self, id):
        row = None
        query = 'select * from persons where id = %s'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (id,))
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            row = cursor.fetchone()
            print(f'Person details are \n', str(row))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return row

    def list_all_rows(self):
        query = 'select * from persons;'
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'No rows found in the table')
                rows = []
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print(str(row))
            cursor.close()
            self.disconnect_db(connection)
            return rows
        except:
            print('Error in reading rows')

    def get_latest_row_id(self):
        query = 'select max(id) from persons;'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        id = cursor.fetchone()
        cursor.close()
        self.disconnect_db(connection)
        return id[0]

