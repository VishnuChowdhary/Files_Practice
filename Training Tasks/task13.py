# Reverse the digit by using exception handling
"""
Step 1 : Get the integer number to reverse that
Step 2 : Create try block to handle the exception
Step 3 : in try block check whether given input is integer type or other type
Step 4 : if the number is integer type then execute the if block of code
Step 5 : if the number is other than the integer type execute the catch block and re ask for the valid input
Step 6 : By using the index concept reverse the string
Step 7 : And print the reversed number to the console
"""

while True:
    try:
        number = int(input("Enter the number to reverse the number : "))
        if type(number) == int:
            while number != 0:
                reversed_Number = str(number)[::-1]
                print(f"The number has been reversed : {reversed_Number}")
                break
    except:
        print("Enter the valid number")