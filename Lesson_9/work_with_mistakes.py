first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

# result = first // second

# try:
#     if isinstance(first, int) and isinstance(second, int):
#         result = first // second
# except ZeroDivisionError:
#     result = 'Error!'
# except TypeError:
#     result = 'Typeerror'
# else:
#     print(result)
# finally:
#     print('End')

if isinstance(first, str):
    raise TypeError

assert  isinstance(first, int), f'Invalid datatype {type(first)}'


