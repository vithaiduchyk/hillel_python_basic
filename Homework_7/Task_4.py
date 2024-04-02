elements = [1, 5, 68, 0]
min_value = None

for element in elements:
    if min_value is None:
        min_value = element
    elif element < min_value:
        min_value = element

print(f"Min value in list is: {min_value}")

