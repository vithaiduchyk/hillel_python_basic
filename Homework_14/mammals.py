from abc import abstractmethod

from animals import Animal


class Mammal(Animal):
    def __init__(self, species, habitat, sound):
        super().__init__(species, habitat)
        self.sound = sound

    @abstractmethod
    def give_birth(self):
        pass

    @abstractmethod
    def feed_young(self):
        pass
