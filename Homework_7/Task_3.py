numbers = input("Enter numbers by space: ").split()

all_unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            all_unique = False
            break
    if not all_unique:
        break

if all_unique:
    print("All numbers is unique")
else:
    print("Numbers not unique")

