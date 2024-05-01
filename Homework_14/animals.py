from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass