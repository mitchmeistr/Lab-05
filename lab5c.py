#!/usr/bin/env python3
# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-11-11
from lab5a import *

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        sum = int(number1) + int(number2)
        #return sum
        #return (int(number1) = int(number2))
        return int(sum)
    except:
        return ("error: could not add numbers")

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        file_lines = f.readlines()
        f.close()
        return (file_lines)
    except OSError:
        return ("error: could not read file")



if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
