
input_string = input("Enter a string: ")

# not sure about this method, it's what i found in stackoverflow
# lower() - this ensures that the comparison for palindromes is case-insensitive.
cleaned_string = ''.join(filter(str.isalnum, input_string.lower()))

if cleaned_string == cleaned_string[::-1]:
    print(f"{input_string} is a palindrome!")
else:
    print(f"{input_string} is not a palindrome!")

