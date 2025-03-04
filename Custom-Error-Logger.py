#!/usr/bin/env python3
from datetime import datetime

class Calculator:

    def Addition(self,*args):
        return sum(args)

    def Subtraction(self,*args):
        if not args:
            return "Error: No Numbers provided."
        sub = args[0]
        for num in args[1:]:
            sub -= num
        return sub
    
    def Multiplication(self,*args):
        if not args:
            return "Error: No number Provided."
        mul = 1
        for num in args:
            mul*=num
        return mul

    def Division(self,*args):
        if not args:
            return "Error: No Numbers Provided."
        div = args[0]
        for num in args[1:]:
            if num ==0:
                return "Error:Division by Zero is not allowed."
            div /= num
        return div

#Instantiate the  calculator class
calc = Calculator()

#Create Log file
log_file = open('error_log.txt','a')
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

operation = input("Enter operation to be Performed (add/sub/div/mul): ").lower()
if operation in ['add', 'sub', 'div', 'mul']:
    try:
        raw_numbers = input("Enter the numbers to be calculated, separated by space: ")
        numbers = [float(num) for num in raw_numbers.split()]
        if operation == 'add':
            result = calc.Addition(*numbers)
        elif operation == 'sub':
            result = calc.Subtraction(*numbers)
        elif operation == 'div':
            result = calc.Division(*numbers)
        elif operation == 'mul':
            result = calc.Multiplication(*numbers)
        if "Error" in str(result):
            print(result)
            log_file.write(f"{formatted_time}: {result} for operation '{operation}'.\n")
        else:
            print(f'Result: {result}')

    except ValueError:
        print("Invalid Input. Please Enter Numeric Values.")
        log_file.write(f"{formatted_time} Value Error for operation '{operation}'.\n") 
else:
    print("Invalid Input. please choose from add, sub, mul, div.")
    log_file.write(f"{formatted_time} Invalid operation '{operation}' selected.\n")

log_file.close()
