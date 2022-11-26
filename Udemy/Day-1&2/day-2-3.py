# Program for calculating your life in weeks

age = int(input("Enter your current age : "))
overall_life = 90

rem_age = overall_life - age

months = rem_age * 12
weeks = rem_age * 52
days = rem_age * 365

print(f"you have {days} days, {weeks} weeks and , {months} months left...")