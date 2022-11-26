"""
Step 1 :
"""
num = int(input("Enter the number to check prime number : "))

def prime_Checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_Checker(number = num)