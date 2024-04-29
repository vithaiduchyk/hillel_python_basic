# Inheritance
# IS-A
# Multi-inheritance

class Human:
    def __init__(self, name):
        self.name = name

    def breath(self):
        return f'{self.name} can be breath'


class Employee(Human):
    def __init__(self, salary, bonus, name):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self._calculate_bonus()

    def _calculate_bonus(self) -> float:
        return self.salary * self.bonus // 100


class Developer(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary, 10)

    def developing(self):
        return 'I developing'


class AQA(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary, 5)

    def do_testing(self):
        return 'I do test'


class Manager(Employee):

    def __init__(self, name, salary, bonus=50):
        super().__init__(name, salary, bonus)

    def calculate_salary(self):
        return self.salary + 10_000 + self._calculate_bonus()

    def create_report(self):
        return 'I create report'


if __name__ == '__main__':
    maryna = AQA("Maryna", 5_000)
    oleg = Developer("Oleg", 7_000)
    nastya = Manager("Nastya", 10_000, 10)
    print(maryna.calculate_salary())
    print(oleg.calculate_salary())
    print(nastya.calculate_salary())
