# calculator console app
number_1 = float(input('Enter first number: '))
number_2 = float(input('Enter second number: '))
operation = input('Enter what do you want to do (+, -, / or *): ')

if operation == "+":
    result = number_1 + number_2

elif operation == "-":
    result = number_1 - number_2

elif operation == "/":
    result = number_1 / number_2

elif operation == "*":
    result = number_1 * number_2

else:
    print('not supported operation')

print(result)
