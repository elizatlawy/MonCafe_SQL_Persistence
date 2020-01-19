import sqlite3
import atexit
from dbtools import Dao
import os
import sys


# Data Transfer Objects:
class Employee(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier(object):
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information


class Product(object):
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


class Coffee_stand(object):
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# Repository
class Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = Dao(Employee, self._conn)
        self.Suppliers = Dao(Supplier, self._conn)
        self.Products = Dao(Product, self._conn)
        self.Coffee_stands = Dao(Coffee_stand, self._conn)
        self.Activities = Dao(Activitie, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
                        CREATE TABLE Employees (
                            id              INT         PRIMARY KEY,
                            name            TEXT        NOT NULL,
                            salary          REAL        NOT NULL,
                            coffee_stand    INT REFERENCES Coffee_stands(id)    
                        );

                        CREATE TABLE Suppliers (
                            id                    INT         PRIMARY KEY,
                            name                  TEXT        NOT NULL,
                            contact_information   TEXT
                        );

                        CREATE TABLE Products (
                            id                    INT         PRIMARY KEY,
                            description           TEXT        NOT NULL,
                            price                 REAL        NOT NULL,
                            quantity              INT         NOT NULL
                        );

                        CREATE TABLE Coffee_stands (
                            id                     INT       PRIMARY KEY,
                            location               TEXT      NOT NULL,
                            number_of_employees    INT   
                        );

                        CREATE TABLE Activities (
                            product_id             INT     REFERENCES Products(id),
                            quantity               INT     NOT NULL,
                            activator_id           INT     NOT NULL,
                            date                   DATE    NOT NULL 
                        ); 
                """)


# singleton
repo = Repository()
atexit.register(repo._close)


