def factorial(n):
    next_number = 1
    result = 1
    while n:
        yield result
        next_number += 1
        n -= 1
        result *= next_number


for index, el in enumerate(factorial(12), 1):
    print(index, el)
