# import sqlite3
# import atexit
#
#
# # Data Transfer Objects:
# class Employee(object):
#     def __init__(self, id, name, salary, coffee_stand):
#         self.id = id
#         self.name = name
#         self.salary = salary
#         self.coffee_stand = coffee_stand
#
#
# class Supplier(object):
#     def __init__(self, id, name, contact_information):
#         self.id = id
#         self.name = name
#         self.contact_information = contact_information
#
#
# class Product(object):
#     def __init__(self, id, description, price, quantity):
#         self.id = id
#         self.description = description
#         self.price = price
#         self.quantity = quantity
#
#
# class Coffee_stand(object):
#     def __init__(self, id, location, number_of_employees):
#         self.id = id
#         self.location = location
#         self.number_of_employees = number_of_employees
#
#
# class Activitie(object):
#     def __init__(self, product_id, quantity, activator_id, date):
#         self.product_id = product_id
#         self.quantity = quantity
#         self.activator_id = activator_id
#         self.date = date
#
#
# # Data Access Objects:
# # All of these are meant to be singletons
# class Employees:
#     def __init__(self, conn):
#         self._conn = conn
#
#     def insert(self, employee):
#         self._conn.execute("""
#                INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
#            """, [employee.id, employee.name, employee.salary, employee.coffee_stand])
#
#     def find(self, employee_id):
#         c = self._conn.cursor()
#         c.execute("""
#             SELECT id, name FROM Employees WHERE id = ?
#         """, [employee_id])
#
#         return Employee(*c.fetchone())

