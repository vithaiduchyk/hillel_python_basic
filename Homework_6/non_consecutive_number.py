numbers = [1, 5, 68, 0]
prevNum = 0
for number in range(1, len(numbers)):
    if numbers[number] != numbers[number - 1] + 1:
        print(f"The first non-consecutive number in the list: {numbers[number]}")
        break
