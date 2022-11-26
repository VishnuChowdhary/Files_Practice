import random
# Program to generate random card picking
"""
Step 1 : get the every body names from user in string
Step 2 : Convert the string into list by using split function
Step 3 : Print the names in list format to console
Step 4 : import random module to generate the random number
Step 5 : by using index function we are going to get random name
Step 6 : lets generate the random index by calculating len of the list
Step 7 : after creating random number printing the list by calling the random number position in the list 
"""
names_String = input("Give the everybody names separated by comma : ")
names = names_String.split(",")
len_list = len(names)
random_index = random.randint(0, len_list - 1)
print(names[random_index])