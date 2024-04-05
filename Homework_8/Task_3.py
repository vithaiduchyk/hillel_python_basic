result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

character_counts = {}

for char in result_link:
    if char in character_counts:
        character_counts[char] += 1
    else:
        character_counts[char] = 1

print(f'Here is result: {character_counts}')
