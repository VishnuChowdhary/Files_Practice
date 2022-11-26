# Max of three Numbers
def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))


# Find sum of the list by using functions
def Sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


print(sum((8, 2, 3, 0, 7)))


# Reverse a string
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1


print(string_reverse('Vishnu@26'))


# Factorial of the number
def factorial_number(num):
    if num == 0:
        return 1
    else:
        return num * factorial_number(num - 1)


num = int(input("Enter the number to find factorial = "))
print(factorial_number(num))


# Check whether a number of falls in a given range
def test_range(num):
    if num in range(3, 9):
        print(f"{num} is in the range")
    else:
        print("The number is outside the given range.")


test_range(5)