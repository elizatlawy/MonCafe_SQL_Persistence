import os
import sqlite3
import sys
import operator
from persistence import *


def print_db():
    print("Activities")
    for activity in repo.Activities.find_all_ordered_by('date'):
        activity_tuple = (activity.product_id, activity.quantity, activity.activator_id, activity.date)
        print(activity_tuple)
    print("Coffee stands")
    for stand in repo.Coffee_stands.find_all_ordered_by('id'):
        stand_tuple = (stand.id, stand.location, stand.number_of_employees)
        print(stand_tuple)
    print("Employees")
    for employee in repo.Employees.find_all_ordered_by('id'):
        employee_tuple = (employee.id, employee.name, employee.salary, employee.coffee_stand)
        print(employee_tuple)
    print("Products")
    for product in repo.Products.find_all_ordered_by('id'):
        product_tuple = (product.id, product.description, product.price, product.quantity)
        print(product_tuple)
    print("Suppliers")
    for supplier in repo.Suppliers.find_all_ordered_by('id'):
        supplier_tuple = (supplier.id, supplier.name, supplier.contact_information)
        print(supplier_tuple)
    print()
    employees = repo.Employees.find_all_ordered_by('name')
    # print the Employees report if there are Employees
    if employees is not None:
        print("Employees report")
        for employee in employees:
            total_sales = 0
            for activity in repo.Activities.find_all():
                if (int(activity.quantity) < 0) and (activity.activator_id == employee.id):
                    curr_product = repo.Products.find(id=activity.product_id)[0]
                    total_sales = total_sales + (-activity.quantity * curr_product.price)
            bld_name = repo.Coffee_stands.find(id=employee.coffee_stand)[0].location
            print(employee.name, employee.salary, bld_name, total_sales)
    # print the Activities report if there are activities
    cursor = repo._conn.cursor()
    cursor.execute("""SELECT Activities.date, Products.description, Activities.quantity, Employees.name, Suppliers.name 
                              FROM Activities INNER JOIN Products ON Activities.product_id = Products.id
                              LEFT OUTER JOIN Employees ON Activities.activator_id = Employees.id
                              LEFT OUTER JOIN Suppliers ON Activities.activator_id = Suppliers.id
                              ORDER BY Activities.date ASC """)
    activities_tuple = cursor.fetchall()
    if len(activities_tuple) > 0:
        print()
        print("Activities")
        for activity in activities_tuple:
            print(activity)


if __name__ == '__main__':
    print_db()
