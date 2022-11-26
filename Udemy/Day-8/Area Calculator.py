"""
Step 1 : Get height and width of the wall from user
Step 2 : create the variable to store how many liters of paint require per square feet
Step 3 : Lets create the function with parameter(Height,Width,Cover)
Step 4 : Lets calculate the number of cans req to paint the wall
Step 5 : finally call the function
"""
import math
H = float(input("Enter the height of the wall : "))
W = float(input("Enter the width of the wall : "))
paint_Req = 5

def paint_Cal(Height, Width, cover):
    numb_of_cans_req = math.ceil((Height * Width) / cover)
    print(f"you'll need {numb_of_cans_req} cans of paint")

paint_Cal(Height = H, Width = W, cover = paint_Req)
