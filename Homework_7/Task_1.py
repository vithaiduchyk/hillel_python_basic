first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_elements = list(set(first) & set(second))
print(f"Here is unique elements from {first} and {second} lists: {unique_elements}")