"""
Options
Signup
Step 1 : First create the dictionary to store the details of the user
Step 2 : Ask user details and store it in to the dictionary
Step 3 : create a folder by using file handling
Step 4 : store the data in the file which has been created
Login
Step 1 : now ask the user for username and password
Step 2 : then retrieve the data from file by using the ast package
Step 3 : Now check whether username and password matches with which is already available in the file
Step 4 : If the username and password matches print your authorized
Step 5 : Else print the re-verify your username and password

Edit Details
Step 1 :

Remove Details
Step 1 :
"""
import ast
def sign_UP():
    First_Name = input("Enter the first name : ")
    Last_Name = input("Enter the Last name : ")
    Mail_ID = input("Enter the mail_id : ")
    Password = input("Enter the Password : ")

    User_Details = {"User_First_Name": First_Name, "User_Last_Name": Last_Name,
                    "User_Mail_ID": Mail_ID, "User_Password": Password}
    print(User_Details)

    with open("User_Details.txt", 'w') as f:
        f.write(str(User_Details))

def log_IN():
    User_Email_ID = input("Enter the Email_ID : ")
    User_Password = input("Enter the Password : ")

    f = open('User_Details.txt', 'r')
    temp = f.readline()
    result = ast.literal_eval(temp)

    if result["User_Mail_ID"] == User_Email_ID and result["User_Password"] == User_Password:
        print("Your authorised")
    else:
        print("Enter the correct mail or password")

def edit_Details():
    edit_Details = input("Enter the key to change its value : ")

def remove_Details():
    remove_Element = input("Enter the element to remove from dictionary : ")
