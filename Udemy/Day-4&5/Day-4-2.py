# Treasure Map
"""
Step 1 : create the 3 by 3 matrix structured lists
Step 2 : insert those all into one linked list
Step 3 : Get input from user to where do you want to place treasure
Step 4 : And divide the number into horizontal and vertical indexes and also covert strings into integers
Step 5 : Now specify the place by using the horizontal and vertical indexes
Step 6 : Now place x in the position
Step 7 : Print final output to console
"""
row1 = ["😃", "😃", "😃"]
row2 = ["😃", "😃", "😃"]
row3 = ["😃", "😃", "😃"]

map = [row1, row2, row3]
place = input("Enter the which place do you want to place treasure : ")
horizontal = int(place[0])
vertical = int(place[1])

map[vertical -1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")