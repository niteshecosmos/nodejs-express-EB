#You are going to write a program that calculates the average student height from a List of heights.

#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

#e.g.

#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

#There are a total of 7 heights in student_heights

#1146 ÷ 7 = 163.71428571428572

#Average height rounded to the nearest whole number = 164


students_heights = input().split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

total_height = 0
for height in students_heights:
    total_height += height
print(f"total height ={total_height}")

number_of_students = 0
for student in students_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height/number_of_students)
print(f"average height = {average_height}")       
