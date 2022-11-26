def count_primes(num):
    if num < 2:
        return 0

    count = [2]
    x = 3
    while x <= num:
        for y in count:
            if x % y == 0:
                x += 2
                break
        else:
            count.append(x)
            x += 2
    print(count)
    return len(count)


final_count = count_primes(100)
print(final_count)
