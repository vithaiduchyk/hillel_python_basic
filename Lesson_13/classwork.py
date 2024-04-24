# lambda

def square(number: int):
    return number ** 2


square_2 = lambda number: number ** 2


def even_odd(number):
    return "EVEN" if number % 2 == 0 else "ODD"


even_odd_2 = lambda number: "EVEN" if number % 2 == 0 else "ODD"

if __name__ == '__main__':
    def even_numbers(num):
        return num % 2 == 0


    # number = list(range(10))
    # # print(number)
    # result = list(filter(even_numbers, number))
    # # print(result)
    #
    # result_map = list(map(lambda number: number ** 2, result))
    # print(result_map)
    #
    # res = map(lambda number: number ** 2,list(filter(even_numbers, number)))

    my_dict = {'d': 1, 'a': 4, 'b': 2}
    print(my_dict.items())
    sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
    print(sorted_dict)
    # x = 2
    # result = lambda n=x: n ** 2
    # x = 3
    # result_2 = lambda n=x: n ** 2
    # print(result())
    # print(result_2())
