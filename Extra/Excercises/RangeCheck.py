def ran_check(num, low, high):
    if num in range(low, high + 1):
        return True
    else:
        return False


result = ran_check(10, 1, 10)
print(result)
