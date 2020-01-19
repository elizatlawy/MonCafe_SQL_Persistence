import os
import sqlite3
import sys
from persistence import *


def insert_to_tables(input_file):
    # curr_coffee_stand = Coffee_stand(11, "Bld-90", 1)
    # print(curr_coffee_stand.id, curr_coffee_stand.location, curr_coffee_stand.number_of_employees)
    # repo.Coffee_stands.insert(curr_coffee_stand)
    with open(input_file, 'r') as file:
        for line in file:
            data = line.split(', ')
            if data[0] == 'E':
                curr_employee = Employee(data[1], data[2], data[3], data[4])
                repo.Employees.insert(curr_employee)
            elif data[0] == 'S':
                ## remove the \n
                curr_supplier = Supplier(data[1], data[2], data[3])
                repo.Suppliers.insert(curr_supplier)
            elif data[0] == 'P':
                curr_product = Product(data[1], data[2], data[3], 0)
                repo.Products.insert(curr_product)
            elif data[0] == 'C':
                curr_coffee_stand = Coffee_stand(data[1], data[2], data[3])
                repo.Coffee_stands.insert(curr_coffee_stand)


if __name__ == '__main__':
    # TODO if the db exist need to delete it
    repo.create_tables()
    insert_to_tables(sys.argv[1])
