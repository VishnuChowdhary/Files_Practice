# Program to check whether string is palindrome or not
string = input("Enter the string :")

w = ""

for i in string:
    w = i + w

if string == w:
    print("Yes")
else:
    print("No")
