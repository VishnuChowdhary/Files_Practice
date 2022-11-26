#Adding Evens
n = int(input("Enter the ending number of the range : "))
Sum = 0
for i in range(1, n):
    if i % 2 == 0:
        Sum += i
print(Sum)