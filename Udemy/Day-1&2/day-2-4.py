# Program for Tip Calculator

print("Welcome to the tip calculator.")
total_Bill = float(input("What was the total bill? "))
tip_Percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_persons = int(input("How many people to split the bill? "))

tip = tip_Percentage / 100
bill_including_tip = total_Bill * tip
final_Bill = bill_including_tip + total_Bill
each_person = round(final_Bill / total_persons , 2)
print(f"Each person should pay : ${each_person}")