#!/usr/bin/env python3
try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    print(f'Divison is: {num1/num2}')
except ZeroDivisionError:
    print("Can't divide zero with number")
except TypeError:
    print("Type Error, Check Number Datatype")
except ValueError:
    print("Entered Number should be integer")

