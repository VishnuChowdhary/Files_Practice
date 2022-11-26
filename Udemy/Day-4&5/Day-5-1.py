# Average Height Calculation
"""
Step 1 : Take the heights of the students from user
Step 2 : Convert the String of input into the integers
Step 3 : iterate the list and sum the heights in the list
Step 4 : iterate the list and count the number of students
Step 5 : Now calculate the average height of the students
"""
Students_Heights = input("Input a list of students heights : ").split()
for i in range(0, len(Students_Heights)):
    Students_Heights[i] = int(Students_Heights[i])
print(Students_Heights)

total_height = 0
for height in Students_Heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in Students_Heights:
    number_of_students += 1
print(number_of_students)

average_height = total_height // number_of_students
print(f"Average height among the students is : {average_height}")
