# Task 1: Given the list of grades, Sort the list in descending order and print

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]


grades.sort()  # First, sort the list in order
grades.reverse()  # Then reverse the list
print(grades)

# Task 2: Calculate the average grade and print

average_grade = sum(grades)/len(grades)
print(average_grade)