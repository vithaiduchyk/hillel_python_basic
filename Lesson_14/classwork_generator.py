def square():
    print("Generator ")
    for e in range(1, 11, 2):
        yield e ** 2


gen = square()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  # StopIteration
