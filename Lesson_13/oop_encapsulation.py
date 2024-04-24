class Human:
    def __init__(self, name, age, gender=None):
        self._name = name
        self.__age = age
        self.__gender = gender

    def __str__(self):
        return f'{self.__class__.__name__} with name: {self._name} and age: {self.__age}'

    @property
    def name(self):
        return self._name

    # def get_name(self):
    #     return self._name

    @property
    def age(self):
        return self.__age

    # def get_age(self):
    #     return self.__age

    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            raise ValueError("Name should contain only letters")
        self._name = new_name

    @age.setter
    def age(self, new_age):
        if 0 > new_age > 100:
            raise ValueError("Invalid age")

        self.__age = new_age

    @name.deleter
    def name(self):
        raise PermissionError("To can't delete attribute")

    def __calculate_salary_according_to_gender(self):
        return ''


    # def set_age(self, new_age):
    #     if 0 > new_age > 100:
    #         raise ValueError("Invalid age")
    #
    #     self.__age = new_age
    #
    # def __set_name__(self, new_name: str):
    #     if new_name.isalpha():
    #         raise ValueError("Name should contain only letters")
    #     self._name = new_name


if __name__ == '__main__':
    tom = Human("Tom", 32)
    print(tom)
    tom.name = 'John'
    print(tom)
