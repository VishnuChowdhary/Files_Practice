print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 127:
    print("You can ride the rollercoatser!")
    if age < 12:
        bill = 5
        print("You need to pay $5 for Ride")
    elif age <= 18:
        bill = 7
        print("Yo need to pay $7 for Ride")
    else:
        bill = 12
        print("You need to pay $12 for Ride")
    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill {bill}")
else:
    print("Sorry, your height is under ")