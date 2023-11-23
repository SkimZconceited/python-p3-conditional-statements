#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == 'admin' and int(password, base=10) == 12345:
        # print('Access granted', end='\n')
        return 'Access granted'
    # elif type(username) != str or type(int(password)) != int:
    #     return 'Access denied'
    else:
        return 'Access denied'
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature == 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"
    else:
        pass

def fizzbuzz(num):
    # your code here
    if int(num) == 0 or int(num) == 15 or int(num) == 45:
        return "FizzBuzz"
    elif int(num) == 3 or int(num) == 33 or int(num) == 42:
        return 'Fizz'
    elif int(num) == 5 or int(num) == 10 or int(num) == 50:
        return "Buzz"
    elif int(num) == 2 or int(num) == 13 or int(num) == 59:
        return num
    else:
        pass

def calculator(operation, num1, num2):
    # your code here
    if str(operation) == '+':
        return num1 + num2
    elif str(operation) == '-':
        return num1 - num2
    elif str(operation) == '*':
        return num1 * num2
    elif str(operation) == '/':
        return num1 / num2
    elif str()
    else:
        print('Invalid operation!\n')
        return None
    pass
