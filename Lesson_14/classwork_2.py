class Father:
    def __init__(self):
        self.strength = 40

    def do_worhout(self):
        return f'Do workout with strength {self.strength}'


class Mother:
    def __init__(self):
        self.wisdom = 60

    def read_books(self):
        return f'Read books with wisdom {self.wisdom}'


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
    def play(self):
        return "I playing"


if __name__ == '__main__':
    tom = Child()
    print(tom.do_worhout())
    print(tom.read_books())
    print(tom.play())
