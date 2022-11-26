"""
Options
Step 1 : Get the options between signup and login
Step 2 : if the user selected signup go with Sign UP
Step 3 : elif go with log in
Step 4 : else print choose correct options
Sign UP
Step 5 : Create a text file
Step 6 : Take the user details from input function(User_First_Name,User_Second_Name,User_Mail,User_password)
Step 7 : Keep the details under text file in the form of dictionary
Step 8 : Store dictionary in file
Log IN
Step 9 : Get the Email_ID from user and Password
Step 10 : Now take the User_Details from text file and compare with details in file
Step 11 : If the username and password matched then everything file
Step 12 : Else get the correct username and password still it is matched
"""
import ast
Options = input("Choose options(signup , login) : ")
if Options == 'signup':
    First_Name = input("Enter the first name : ")
    Last_Name = input("Enter the Last name : ")
    Mail_ID = input("Enter the mail_id : ")
    Password = input("Enter the Password : ")

    User_Details = {"User_First_Name": First_Name, "User_Last_Name": Last_Name,
                    "User_Mail_ID": Mail_ID, "User_Password": Password}
    print(User_Details)

    with open("User_Details.txt", 'w') as f:
        f.write(str(User_Details))

elif Options == 'login':
    User_Email_ID = input("Enter the Email_ID : ")
    User_Password = input("Enter the Password : ")

    f = open('User_Details.txt', 'r')
    temp = f.readline()
    result = ast.literal_eval(temp)

    if result["User_Mail_ID"] == User_Email_ID and result["User_Password"] == User_Password:
        print("Your authorised")
    else:
        print("Enter the correct mail or password")
else:
    print("Choose the correct options")
