print("Enter string for compare\n")
first_string = input("Enter first string: ")
second_string = input("Enter second string: \n ")

if len(first_string) > len(second_string):
    print(f"The first_string is bigger!")
elif len(second_string) > len(first_string):
    print(f"The second_string is bigger")
elif len(first_string) == len(second_string):
    print("The two lines have the same length!")
