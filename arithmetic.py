def multiply(*numbers):
    total = 1
    print(numbers)
    for number in numbers:
        total = total * number
    return total
