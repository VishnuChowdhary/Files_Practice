def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f"Original String : {s}")
    print(f"lowercase count : {lowercase}")
    print(f"uppercase count : {uppercase}")


s = "Hello Mr Vishnu!"
up_low(s)

