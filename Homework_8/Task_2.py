
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
query_string = ''

for key, value in params.items():
    query_string += f'{key}={value}&'

query_string = query_string[:-1]
result = initial_str + query_string

print(f'Here is result: {result}')
