#!/usr/bin/env python3

def filter_even_numbers(numbers):
    even_number = []
    for num in numbers:
        if num % 2 == 0 :
            even_number.append(num)
        else:
            continue

    return even_number

numbers = [int(num) for num in input().split()]
print(filter_even_numbers(numbers))

