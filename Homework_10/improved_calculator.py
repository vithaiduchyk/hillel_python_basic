def addition(number_1, number_2, operataion):
    if operataion == '+':
        result = number_1 + number_2
        return print(result)


def deduction(number_1, number_2, operataion):
    if operataion == '-':
        result = number_1 - number_2
        return print(result)


def multiplication(number_1, number_2, operataion):
    if operataion == '*':
        result = number_1 * number_2
        return print(result)


def division(number_1, number_2, operataion):
    if operataion == '/':
        result = number_1 / number_2
        return print(result)


number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))
operation = input('Enter what do you want to do (+, -, / or *): ')

try:
    addition(number_1, number_2, operation)
    deduction(number_1, number_2, operation)
    multiplication(number_1, number_2, operation)
    division(number_1, number_2, operation)
except ValueError:
    print("Wrong operation")


