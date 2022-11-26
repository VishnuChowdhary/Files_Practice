# Rock,paper,scissor game
"""

"""
import random
li = ['Rock', 'Paper', 'Scissors']
user_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
you_Choose = li[user_Choice]
print(f"You Chose - {you_Choose}")
com_Choice = random.randint(0,2)
com_Choose = li[com_Choice]
print(f"Computer Chose - {com_Choose}")

if user_Choice >= 3 or user_Choice < 0:
    print("You typed an invalid number, You lose!")
elif user_Choice == 0 and com_Choice == 2:
    print("You win")
elif com_Choice == 0 and user_Choice == 2:
    print("You lose")
elif com_Choice > user_Choice:
    print("You lose")
elif user_Choice > com_Choice:
    print("You win")
elif com_Choice == user_Choice:
    print("It's a Draw")
