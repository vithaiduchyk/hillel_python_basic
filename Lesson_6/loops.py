# print("Meow")
# print("Meow")
# print("Meow")
# print("Meow")

numbers_str = ['one', 'two', 'tree', 'four', 'two']
my_str = 'abcd'
my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[2])
# for loop

for number in numbers_str:
    idx = numbers_str.index(number)     # 0
    if number in numbers_str[idx + 1:]:
        numbers_str.remove(number)

# for i in range(1, number + 1, 2):
#     print(i)

# print(numbers)

# Task 4

# even_numbers = list()
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

# continue break:
# pass - means nichogo


# even_numbers = list()
# for number in numbers:
#     pass
#     if number == 100:
#         # continue
#         break
#     print(f'My number {number}')

# numbers = [1, 10, 100, 1]
# unique_elements = []
# for number in numbers:
#     if numbers.count(number) != 1:
#         print("List contains not unique elements!")
#         break
# else:
#     print("List contain only unique elements")

#   *
#   * *
#   * * *
#   * * * *

# for i in range(1, 5):
#     print('* ' * i)

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# hight = 6
# for i in range(1, hight):
#     print(hight * ' ', '* ' * i)
#     hight -= 1


# numbers = [1, 2, 3]
# letters = 'abc'
# names = ['Anna', 'Olga']
#
# for number in numbers:
#     for letter in letters:
#         for name in names:
#             print(number, letter, name)


# width = int(input("Enter your width: "))
# height = int(input("Enter your height: "))
#
#
# for i in range(1, height + 1):
#     for j in range(1, width + 1):
#         print('*', end=' ')
#     print()

# names = ["Anna", "Olga", "Nadia", "Oleg"]
# filtered = []
# for name in names:
#     if name == 'Oleg':
#         continue
#     filtered.append(name)
#
# # filtered = [name for name in names if name != 'Oleg']
#
# print(filtered)


data = input("Enter your string: ").lower()
vowels = 'aeiou'
count = 0
for letter in data:
    if letter in vowels:
        count += 1
print(f'Count of  vowels letters in {data} string is {count}')



