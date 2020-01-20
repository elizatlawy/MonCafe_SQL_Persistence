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
    employees = repo.Employees.find_all()
    # employees.sort(key=operator.itemgetter(1))
    print(employees)
    for employee in employees:
        total_sales = 0
        for activity in repo.Activities.find_all():
            if (int(activity.quantity) < 0) and (activity.activator_id == employee.id):
                curr_product = repo.Products.find(id=activity.product_id)[0]
                total_sales = total_sales + (-activity.quantity * curr_product.price)
        employee_tuple = (employee.id, employee.name, employee.salary, total_sales)
        print(employee_tuple)

    print("Activities")
    cursor = repo._conn.cursor()
    for activity in repo.Activities.find_all():
        cursor.execute(""" SELECT Products.description
        FROM Products WHERE Products.id = ? """, (activity.product_id,))
        product_name = cursor.fetchone()
        cursor.execute(""" SELECT Employees.name
                FROM Employees WHERE Employees.id = ? """, (activity.activator_id,))
        employee_name = cursor.fetchone()
        cursor.execute(""" SELECT Suppliers.name
                        FROM Suppliers WHERE Suppliers.id = ? """, (activity.activator_id,))
        supplier_name = cursor.fetchone()
        if int(activity.quantity) > 0:
            supplier_name = supplier_name[0]
        else:
            employee_name = employee_name[0]
        activity_tuple = (activity.date, product_name[0], activity.quantity, employee_name, supplier_name)
        print(activity_tuple)







if __name__ == '__main__':
    print_db()
