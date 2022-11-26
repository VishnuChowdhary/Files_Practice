"""
Step 1 : take the numerator and denominator lists from user
Step 2 : and convert the series of string values to list by using split function
Step 3 : and convert the all string values in list into integer type
Step 4 : iterate the denominator values by numerator values
Step 5 : check the condition whether the // == % .if condition is true print numerator and denominator values
Step 6 : Print the list of numerator and denominator
"""
Numerator = input('Enter the numerator values separated by comma : ')
Numerator_List = Numerator.split()
Denominator = input('Enter the denominator values separated by comma : ')
Denominator_List = Denominator.split()
for i in range(len(Numerator_List)):
    Numerator_List[i] = int(Numerator_List[i])
for j in range(len(Denominator_List)):
    Denominator_List[j] = int(Denominator_List[j])
print(Numerator_List)
print(Denominator_List)
for x in Denominator_List:
    for y in Numerator_List:
        if y // x == y % x:
            print(y, " ", x)
