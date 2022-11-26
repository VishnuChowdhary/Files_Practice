# Linear Search
"""
Step 1 : Get Input list from the user
Step 2 : Get the input key from user
Step 3 : Now check whether the key present in given list by using linear search
Step 4 : By using for loop iterate the list and check one by one whether it is equal to key by using i condition
Step 5 : When the condition meets then it will print the index of the element which is matched
Step 6 : Print the element to the console
"""
li = [1, 23, 4, 5, 9, 7, 2, 3, 98]
key = 2

for i in range(0, len(li)):
    if li[i] == key:
        print(f"The key present in {i} Index")