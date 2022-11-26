# Lucky number finder from DOB
"""
Step 1 : Get the DOB from user separated by space
Step 2 : Now Convert the user given string into list
Step 3 : Then iterate the each element in the list and convert into integers and sum all elements
Step 4 : Now check whether the sum is less than 10 if it is print the sum as a lucky number
Step 5 : Else covert the sum into string and access the elements by indexing and add each digit in sum
Step 6 : After getting single digit number print it as a lucky number
Step 7 : Print the DOB and lucky number in the format of Dictionary to console by adding the key and values
"""
DOB = input("Enter the date of birth separated each number by space : ")
DOB_list = DOB.split()
Sum = 0
add = 0
for num in DOB_list:
    Sum += int(num)
if Sum < 10:
    print(f"Your lucky number = {Sum}")
    X = {}
    X["Date of Birth"] = DOB
    X["Lucky number"] = Sum
    print(X)
else:
    sum_str = str(Sum)
    add = int(sum_str[0]) + int(sum_str[1])
    print(f"Your lucky number = {add}")
    X = {}
    X["Date of Birth"] = DOB
    X["Lucky number"] = add
    print(X)

