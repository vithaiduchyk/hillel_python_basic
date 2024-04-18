a, *c, b = 'abcdrf'


def custom_sum(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    print(kwargs)
    return result


if __name__ == '__main__':
    # print(**({'a' : 1,  'b' : 2]}))
    # print(custom_sum(1, 2, 3, a=10, b=12))
    my_dict = {'sep': '+', 'end': '$'}
    print('Hello World', 'test', **my_dict)
