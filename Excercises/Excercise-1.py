"""
step 1 : Take number input from user
step 2 : iterate the loop from 1 to user given number
step 3 : sum the all number still user given number
step 4 : display the result
"""

num = int(input("Enter the number : "))
sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)
