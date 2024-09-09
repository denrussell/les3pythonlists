'''
Objective: The aim of this assignment is to use Python list slicing.

Problem Statement: You have a list of daily temperatures for one month, 
and you'd like to extract specific data from it.
'''
# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures for the second week (7 days) of the month 
# (index 7 to index 14). Expected Outcome:

83, 85, 86, 87, 88, 89, 90,

temp_second_week = temperatures[7:14]
print(temp_second_week)

# Task 2: Extract all the temperatures above 100. HINT: add the temperatures
# over 100 to a new list, or use list slicing to get the temperatures.

temp_above_100 = []
# highest_temp = max(temperatures) - to determine what is the highest temp
# print(highest_temp)

if 101 in temperatures:
    temp_above_100.append(101)
if 102 in temperatures:
    temp_above_100.append(102)
if 103 in temperatures:
    temp_above_100.append(103)
if 104 in temperatures:
    temp_above_100.append(104)
if 105 in temperatures:
    temp_above_100.append(105)
if 106 in temperatures:
    temp_above_100.append(106)
if 107 in temperatures:
    temp_above_100.append(107)

print(temp_above_100)