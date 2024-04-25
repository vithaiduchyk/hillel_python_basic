class Employee:

    def __init__(self, name, age, position, salary):
        self._name = name
        self.__age = age
        self.position = position
        self.__salary = salary


    def __str__(self):
        return f'{self.__class__.__name__} with name: {self._name} and age: {self.__age}'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @age.setter
    def age(self, new_age):
        self.__age = new_age


    def calculate_bonus_pay(self):
        return ''