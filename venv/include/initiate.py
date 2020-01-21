import sqlite3
import sys
import os


def delete_db():
    try:
        os.remove('moncafe.db')
    except OSError:
        pass


def insert_to_tables(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            data = line.split(', ')
            if data[0] == 'E':
                curr_employee = Employee(data[1], data[2], data[3], data[4])
                repo.Employees.insert(curr_employee)
            elif data[0] == 'S':
                curr_supplier = Supplier(data[1], data[2], data[3])
                repo.Suppliers.insert(curr_supplier)
            elif data[0] == 'P':
                curr_product = Product(data[1], data[2], data[3], 0)
                repo.Products.insert(curr_product)
            elif data[0] == 'C':
                curr_coffee_stand = Coffee_stand(data[1], data[2], data[3])
                repo.Coffee_stands.insert(curr_coffee_stand)


if __name__ == '__main__':
    # delete the db if it is already exist
    delete_db()
    # the import is here so the connection only happens after you delete the old db
    from persistence import *
    import printdb
    repo.create_tables()
    insert_to_tables(sys.argv[1])
    printdb.print_db()
