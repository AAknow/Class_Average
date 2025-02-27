## CST-16163 Intro to Computer Programming
## By: Aaron Knowles

## Initialize variables
classGrades = [87, 74, 39, 93, 82, 68]
studentTotal = 0
gradeTotal = 0

## Calculate the grade total and number of students
for grade in classGrades:
    gradeTotal += grade
    studentTotal += 1

## Display the result 
print("The Class Average is: " + str(gradeTotal / studentTotal))
