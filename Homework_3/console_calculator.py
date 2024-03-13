# calculator console app
number_1 = input('Enter first number: ')
number_2 = input('Enter second number: ')
operation = input('Enter what do you want to do (+, -, / or *): ')

if operation == "+":
    result = float(number_1) + float(number_2)
    print(result)
elif operation == "-":
    result = float(number_1) - float(number_2)
    print(result)
elif operation == "/":
    result = float(number_1) / float(number_2)
    print(result)
elif operation == "*":
    result = float(number_1) * float(number_2)
    print(result)
else:
    print('not supported operation')

