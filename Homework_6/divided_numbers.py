numbers = [1, 41, 156, 12, 51, 52, 5, 62, 65, 3, 78, 21, 134]
divide_on = int(input("Enter number: "))
divided_numbers = []

for number in numbers:
    if number % divide_on == 0:
        divided_numbers.append(number)

print(divided_numbers)

