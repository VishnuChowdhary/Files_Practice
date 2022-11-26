# python code for temperature converter

x = input("Enter the temperature type(C OR K OR F) : ")
y = float(input("Enter the temperature value : "))
z = input("Enter the temperature type to convert(C OR K OR F) : ")

if x == "C" and z == "F":
    print(y*(9/5)+32)
elif x == "C" and z == "K":
    print(y + 273.15)
elif x == "F" and z == "C":
    print((y - 32) * (5 / 9))
elif x == "F" and z == "K":
    print((y + 459.67) * (5 / 9))
elif x == "K" and z == "C":
    print(y - 273.15)
else:
    print(y * (9 / 5) - 459.67)




