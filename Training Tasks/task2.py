# Python program to check the number is armstrong or not
num = int(input("Enter the number : "))
l = len(num)
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** l
    temp //= 10

if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not armstrong number")