"""
Step 1 : Create the functions for add,subtract,multiply and divide
Step 2 : Ask the user for choice the function(add,subtract,multi[ply,divide)
Step 3 : Based on the choice of the user call the function (add,subtract,multiply,divide)
Step 4 : Ask the user for next calculation if it is true repeat the entire process gain or else break the program
Step 5 : After calling the function result will return to the console
Step 6 : Else print the invalid if something went wrong
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select options 1-add, 2-subtract, 3-multiply, 4-divide")

while True:
    choice = input("Enter the choice(1/2/3/4)")

    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_Calculation = input("Lets do next calculation? (yes/no): ")
        if next_Calculation == "no":
            break

    else:
        print("Invalid Input")