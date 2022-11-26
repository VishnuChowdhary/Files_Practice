def lesser_of_two_numbers(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


small_number = lesser_of_two_numbers(2, 5)
print(small_number)
