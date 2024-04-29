class A:
    pass


class B(A):
    pass


class C(B):
    pass


class D(C, B):
    pass


class E(D):
    pass


if __name__ == '__main__':
    test = E()

