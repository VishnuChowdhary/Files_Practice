# Check the armstrong number by using Exception handling
"""
Step 1 :
"""

while True:
    try:
        number = int(input("Enter the number to check is it armstrong number : "))
        Sum = 0
        temp = number
        if type(number) == int:
            while number >= 0:
                digit = temp % 10
                Sum += digit ** 3
                temp //= 10
                if number == Sum:
                    print(f"{number} is an armstrong number")
                else:
                    print(f"{number} is not an armstrong number")
                break
    except:
        print("Enter the valid number")

