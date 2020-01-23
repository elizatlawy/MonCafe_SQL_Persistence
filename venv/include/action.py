import os
import sqlite3
import sys
from persistence import *
import printdb


def update_db(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            data = line.split(', ')
            curr_product = repo.Products.find(id=data[0])[0]
            if int(data[1]) < 0:  # it is a sale
                if curr_product.quantity >= (- int(data[1])):  # check if the quantity is enough to sell
                    repo.Products.update_quantity(data[0], data[1])
                    curr_act = Activitie(data[0], data[1], data[2], data[3])
                    repo.Activities.insert(curr_act)
            else:  # it is a supply
                repo.Products.update_quantity(data[0], data[1])
                curr_act = Activitie(data[0], data[1], data[2], data[3])
                repo.Activities.insert(curr_act)


if __name__ == '__main__':
    update_db(sys.argv[1])
    printdb.print_db()
