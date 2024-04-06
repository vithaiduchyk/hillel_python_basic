roles = {'admin': ['Vitalii', 'Oleh'], 'maintainer': ['Jeremy', 'Josh'], 'manager': ['Oscar', 'Will'],
         'developer': ['Tony', 'Steve']}
user_name = input('Enter name: ')

found_role = None
for role, users in roles.items():
    if user_name in users:
        found_role = role
        break

if found_role:
    print(f'Hello, {found_role}')
else:
    print('Hello, Guest!')
