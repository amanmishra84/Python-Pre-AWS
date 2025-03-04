#!/usr/bin/env python3

#In terms of memory-efficient
'''
Generators are more memory-efficient than a list because they generate items one at a time,on demand, rather than storing the entire sequence in memory.
'''

#In terms of speed
'''
In terms of speed,Lists are faster than generators for small datasets, but difference becomes noticeable for larger datasets or memory-intensive operations.
'''

#Using List Comprehension
last_number = int(input("last Square Number will be ?: "))
Square_Number = [num**2 for num in range(1,last_number+1)]
print("Using List Comprehension ")
print(Square_Number)

#Using Generator
def Square_Number():
    for num in range(1,last_number+1):
        yield num**2
squares = Square_Number()
print("Using Generator")
for square in squares:
    print(square,end=' ')

