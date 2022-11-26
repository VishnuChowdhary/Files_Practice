"""
Step 1 : First create the file
Step 2 : add text into the text file
Step 3 : 
"""
f = open("intro.txt","w")
text = input("Enter the text : ")
f.write(text)
f.close()