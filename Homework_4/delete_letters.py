message = input("Enter string: ")
letter_to_delete = input("Enter what letter you want to delete: ")

result = message.replace(letter_to_delete, ' ')

result_message = f"You entered {letter_to_delete}, here is result: {result}"
print(result_message)