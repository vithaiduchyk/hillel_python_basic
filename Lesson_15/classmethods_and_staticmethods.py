# @classmethod @staticmethod
from datetime import datetime


class Car:
    count = 0
    wheel = 4
    marks = []

    def __init__(self, mark, model, year=datetime.now().year):
        self.mark = mark
        self.model = model
        self.year = year
        # Car.marks.append(mark)
        Car.increment_count()

    def __repr__(self):
        return f'Car{self.mark, self.model, self.year}'

    @classmethod
    def add_mark(cls, mark):
        cls.marks.append(mark)

    @staticmethod
    def change_wheels():
        return "I change wheels"

    def move(self):
        return f'{self.mark} is moving'

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def verify_year(cls, mark, model, year):
        if year < 2020:
            raise ValueError("Too old")
        else:
            return cls(mark, model)


if __name__ == '__main__':
    bmw = Car('Bmw', 'M5')
    audi = Car('Audi', 'A6', 2023)
    fiat = Car('Fiat', '500', 2023)
    reno = Car.verify_year("Reno", "Megan", 2023)
    print(reno.move())
