result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

character_counts = {}

for char in result_link:
    if char not in character_counts:
        character_counts[char] = result_link.count(char)

print(f'Here is result: {character_counts}')
