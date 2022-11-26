# program to find whether year is leap year or not

year = int(input("Enter the year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap Year.")