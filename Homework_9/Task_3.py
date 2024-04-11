course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

user_input = input("Enter key: ")
try:
        print(f'Your result is {course[user_input]}')
except KeyError:
    print(f'Wrong key name!')

