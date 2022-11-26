# Binary Search method
"""
Step 1 : Create the list
Step 2 : lets select element to be searched
Step 3 : lets set two points low and high at the lowest and highest
Step 4 : Now iterate the list to get the index of the x
Step 5 :
"""
li = [6, 12, 17, 23, 38, 45, 77, 84, 90]
x = 77

low = 0
high = len(li)-1
mid = 0

while low < high:
    mid = (low + high) // 2
    if li[mid] == x:
        print(mid)
    elif li[mid] < x:
        low = mid + 1
    else:
        high = mid - 1


