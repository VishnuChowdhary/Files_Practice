"""
step 1 : take the list of numbers
step 2 : convert the list of values into list
step 3 : convert the list of values into tuple
step 4 : print to console
"""

values = input("Enter the comma separated numbers : ")

list = values.split(",")
tuple = tuple(list)

print('list : ' , list)
print('tuple : ' , tuple)