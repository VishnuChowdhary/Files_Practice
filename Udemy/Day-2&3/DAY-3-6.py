# lOVE CALCULATOR

name1 = input("Enter the name : ")
name2 = input("Enter the name : ")

combined_String = name1 + name2
final_String = combined_String.lower()

t = final_String.count("t")
r = final_String.count("r")
u = final_String.count("u")
e = final_String.count("e")

true = t + r + u + e

l = final_String.count("l")
o = final_String.count("o")
v = final_String.count("v")
e = final_String.count("e")

love =  l + o + v + e

final = str(true) + str(love)

print(f"Your Love Score = {final}")

if (final < 10) or(final > 90):
    print(f"Your love score {final}")
elif (final >= 40) and (final <= 50):
    print(f"Your love score {final}")
else:
    print(f"Your Love score {final_String}")

