first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

not_in_second = []

for x in first:
    if x not in second:
        not_in_second.append(x)

print(f'Here is elements of {first} list what {second} does not have: {not_in_second}')

