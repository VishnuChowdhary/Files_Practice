def makes_twenty(a, b):
    if a == 20 or b == 20:
        return True
    else:
        if a + b == 20:
            return True
        else:
            return False


output = makes_twenty(30, 10)
print(output)
