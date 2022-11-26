"""
step 1 : greeting message display
step 2 : take input whether choose right or left
step 3 : if it is right game over or else forward
step 4 : take input whether swim or wait
step 5 : if it is swim game over or else forward
step 6 : select the color (Red , Blue , Yellow)
step 7 : if it is red and blue game will end if it is yellow display you won
"""

print("Welcome to treasure island")

direction = input("Choose Right or Left? ")
if direction == "left":
    choose = input("Choose swim or wait? ")
    if choose == "wait":
        color = input("Choose the color (Red or Blue or Yellow? )")
        if color == "yellow":
            print("Your Won")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
