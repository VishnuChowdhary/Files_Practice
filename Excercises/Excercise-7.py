# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 , between 2000
# and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: Consider use range(#begin, #end) method

"""
Step 1 : create a list to store the numbers which are met the condition
Step 2 : now iterate the range between 2000 and 3200 by using for loop
Step 3 : Check the condition which is meet append the number into list by using append function
Step 4 : let us print the output to console
"""

List = []

for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        final_List = List.append(str(i))

print(','.join(List))
