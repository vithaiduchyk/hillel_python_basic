class Car:

    def __init__(self, mark, age, model):
        self.mark = mark
        self.age = age
        self.model = model

    def move(self):
        return f'{self.mark} is going'

    def turn_left(self):
        pass

    def check_age(self):
        if self.age < 10:
            return 'Too old'
        else:
            return 'Good'

    def go_straight(self):
        pass

    def go(self):
        self.move()
        self.go_straight()
        self.turn_left()

if __name__ == '__main__':
    bmw = Car()