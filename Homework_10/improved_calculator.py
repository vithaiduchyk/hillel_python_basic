def addition(number_1: float, number_2: float):
    return number_1 + number_2


def deduction(number_1: float, number_2: float):
    return number_1 - number_2


def multiplication(number_1: float, number_2: float):
    return number_1 * number_2


def division(number_1, number_2: float):
    return number_1 / number_2


def calculator(number_1, number_2, operaion):
    if operation == '+':
        result = addition(number_1, number_2)
        return result
    elif operation == '-':
        result = deduction(number_1, number_2)
        return result
    elif operation == '*':
        result = multiplication(number_1, number_2)
        return result
    elif operation == '/':
        result = division(number_1, number_2)
        return result
    else:
        raise TypeError('Operation must be +, -, / or *')


number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))
operation = input('Enter what do you want to do (+, -, / or *): ')

print(calculator(number_1, number_2, operation))


