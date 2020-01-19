import os
import sqlite3
import sys
from persistence import *


def update_db(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            data = line.split(', ')
            curr_product = repo.Products.find(id=data[0])[0]
            if int(data[1]) < 0:
                if curr_product.quantity >= int(data[1]):
                    repo.Products.update_quantity(data[0], data[1])
                    curr_act = Activitie(data[0], data[1], data[2], data[3])
                    repo.Activities.insert(curr_act)
            else:
                repo.Products.update_quantity(data[0], data[1])
                curr_act = Activitie(data[0], data[1], data[2], data[3])
                repo.Activities.insert(curr_act)



if __name__ == '__main__':
    update_db(sys.argv[1])
