"""
step 1 : Take input from user to get Table
step 2 : iterate the loop
step 3 : multiply the table and display
"""

num = int(input("Enter the table you required number : "))

for i in range(1,11,1):
    result = num * i
    print(f"{num} * {i} = {result}")