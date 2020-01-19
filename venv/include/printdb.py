import os
import sqlite3
import sys
from persistence import *


def print_db():
    print("Coffee stands")
    for stand in repo.Coffee_stands.find_all():
        stand_tuple = (stand.id, stand.location, stand.number_of_employees)
        print(stand_tuple)
    print("Employees")
    for employee in repo.Employees.find_all():
        employee_tuple = (employee.id, employee.name, employee.salary, employee.coffee_stand)
        print(employee_tuple)
    print("Products")
    for product in repo.Products.find_all():
        product_tuple = (product.id, product.description, product.price, product.quantity)
        print(product_tuple)
    print("Suppliers")
    for supplier in repo.Suppliers.find_all():
        supplier_tuple = (supplier.id, supplier.name, supplier.contact_information)
        print(supplier_tuple)
    print("Employees report")


    print("Activities")


if __name__ == '__main__':
    print_db()
