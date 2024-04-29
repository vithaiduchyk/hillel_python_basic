# Abstraction
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, salary, bonus, name):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    @abstractmethod
    def do_work(self):
        pass

    def calculate_salary(self):
        return self.salary + self.__calculate_bonus()

    def __calculate_bonus(self) -> float:
        return self.salary * self.bonus // 100


class Cleaner(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary, 3)

    def do_work(self):
        return "I do work like cleaner"


class Manager(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary, 3)

    def do_work(self):
        return "I do work like manager"


if __name__ == '__main__':
    olga = Cleaner("Olga", 1500)
    print(olga.calculate_salary())
    print(olga.do_work())
