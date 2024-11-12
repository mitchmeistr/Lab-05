#!/usr/bin/env python3
# Author: Mitch Gregoris
# Author ID: 133349191
# Date Created: 2023-11-11
from lab5a import *

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, 
    # adds line number to new file
    f = open(file_name_read, 'r')
    file_lines = f.read().splitlines()
    f.close()

    f = open(file_name_write, 'w')
    line_number = 1
    for line in file_lines:
        f.write(str(line_number) + ":" + str(line) + "\n")
        line_number = line_number + 1
    f.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))