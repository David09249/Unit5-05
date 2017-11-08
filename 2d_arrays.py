# Created by: David Wang
# Created on: 21-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit5-05
# This program finds the average of randomly generated numbers in a 2-Dimensional array

from numpy import random

def add_elements(array):
    average = 0
    for find_row_number in array:
        for find_column_number in find_row_number:
            average = average + find_column_number
    average = average / (len(array[0]) * len(array))
    return average

number_of_rows = raw_input("Enter the number of rows you would like: ")
number_of_rows = int(number_of_rows)
number_of_columns = raw_input("Enter the number of columns you would like: ")
number_of_columns = int(number_of_columns)
table = []
for rows in range(0, number_of_rows):
    table.append([])
    for columns in range(0, number_of_columns):
        table[rows].append(random.randint(1, 101))
print(table)
table_values_average = add_elements(table)
print("The average of the numbers are: " + str(table_values_average))
