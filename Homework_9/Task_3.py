course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

user_input = input("Enter key: ")
try:
    if user_input == 'title' or 'language' or 'level' or 'frame':
        print(course[user_input])
except KeyError:
    print(f'Wrong key name!')

