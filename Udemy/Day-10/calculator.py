# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Division
def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}


def calculation():
    num1 = int(input("What is the first number?\n"))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick operation from above line?\n")
        num2 = int(input("What is the second number?\n"))
        result = 0
        if operation_symbol == "+":
            result = add(num1, num2)
            print(result)
        elif operation_symbol == "-":
            result = subtract(num1, num2)
            print(result)
        elif operation_symbol == "*":
            result = multiply(num1, num2)
            print(result)
        elif operation_symbol == "/":
            result = division(num1, num2)
            print(result)

        next_operation = input(f"Type 'y' to continue calculating with answer, Type 'n' to start new calculation.")
        if next_operation == "y":
            num1 = result
        else:
            should_continue = False
            calculation()


calculation()
