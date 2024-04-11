with open('lorem.txt', 'r') as firstfile, open('lorem_1.txt', 'a') as secondfile:
    for line in firstfile:

        secondfile.write(line)
