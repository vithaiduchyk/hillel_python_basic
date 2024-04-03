numbers = input("Enter numbers by space: ").split()

if len(numbers) == len(set(numbers)):
    print(f'{numbers}' list is unique!)
else:
    print(f'{numbers} list is not unique')
