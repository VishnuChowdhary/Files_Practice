# BMI calculator and comment
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

BMI = round(weight / (height ** 2))

if BMI <= 18.5:
    print("Underweight.")
elif BMI > 18.5 and BMI <= 25:
    print("Normalweight")
elif BMI > 25 and BMI <= 30:
    print("overwight")
elif BMI > 30 and BMI <= 35:
    print("obese")
else:
    print("clinically obese")