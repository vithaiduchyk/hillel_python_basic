from Lesson_14.classwork import Employee


class Developer(Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary, 10)
