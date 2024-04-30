from mammals import Mammal


class Predator(Mammal):
    def __init__(self, species, habitat, sound, prey):
        super().__init__(species, habitat, sound)
        self.prey = prey

    def hunt(self):
        print(f"{self.species} is hunting {self.prey}")

    def eat(self):
        print(f"{self.species} is eating {self.prey}")

    def move(self):
        print(f"{self.species} is moving silently to hunt")
