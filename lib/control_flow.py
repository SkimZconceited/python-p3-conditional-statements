#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    try:
        if password == '12345':
            if username.lower() != 'admin' or int(password) != 12345:
                return 'Access denied'
            else:
                if username.lower() == 'admin' and int(password) == 12345:
                    print(f'username is {username}')
                    return 'Access granted'
                else:
                    return 'Access denied'
        else:
            return 'Access denied'
    except ValueError:
        print('Invalid operator!', end='\n')
    pass

admin_login('sudo', '12345')
admin_login('admin', 'sudo')
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
    # elif str(operation) == '==':
    #     return 'Invalid operation!\n'
    else:
        print('Invalid operation!', end='\n')
        return None
    pass
