'''
Author: Francisco Arenas
Creation Date: October 6th, 2021
Last Modfication Date: October 6th, 2021
File with all the needed functions to obtain the required
analysis.
'''

import pkg_resources
import csv
import os

PATH = pkg_resources.resource_filename(__name__, 
    os.path.join(os.pardir, 'data', 'synergy_logistics_database.csv'))


def example():
    rows = []
    toSend = "s"
    with open(PATH, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        toSend = reader

    return toSend

def ex2():
    print(example())

    
        
ex2()

#example()
