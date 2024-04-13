# def say_hello(names):
#     for name in names:
#         print(f'Hello {name.title()}')
#
#
# user_name = ['Maryna', 'dmytro', 'Olga']
# new = ['Test']
# # user_name = input('Enter your name: ')
#
#
# say_hello(user_name)
# say_hello(new)


# def greetings(name: str, is_upper: bool) -> str:
#     if is_upper:
#         name.upper()
#     return f'Hello, {name}!'
#
#
# result = greetings('Maryna')
# print(result)

# languages = {'fr': 'Bonjour', 'en': 'Hello', 'ua': 'Привіт'}


# def greetings(name: str, is_upper=True, language='en') -> str:
#     try:
#
#         word = languages[language]
#     except:
#         word = languages['en']
#
#     return f'{word}, {name.upper()}!'

# def greetings(name: str, is_upper=True, language='en') -> str:
#     word = languages.get(language)
#     return f'{word}, {name.title()}!'
#
#
# print(greetings('Maryna',  language='gfagfdagafdagfd'))
# print(greetings('Dmytro',  language='ua'))
# print(greetings('Test',  language='en'))

# employees = ['Maryna']


# def add_employee(name: str, emp=None):
#     if emp is None:
#         emp = []
#     emp.append(name)
#     return emp
#
#
# developer = add_employee('Ivan')
# print(developer)
# accounter = add_employee('Olha')
# print(accounter)


###############################################
#   LEGB: Local, Enclosed, Global, Builtin
###############################################

# scope = 'global'
#
# def outer():
#     scope = 'enclosed'
#
#     def inner():
#         scope = 'local'
#         print(scope)
#
#     inner()
#
# outer()

counter = 0


def increment() -> int:
    return counter + 1


print(increment())
