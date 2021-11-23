from pet import Pet
from pet import Dog
from pet import Cat

class PetBuilder:
    legs: int = 0
    heads: int = 0
    tails: int = 0
    name: str = ""
    sex: str = ""
    species = ""

    def __init__(self):
        self.cat = Cat()
        self.dog = Dog()

    def a(self, species):
        species.lower()
        self.species = species
        return self

    def with_name(self, name):
        self.name = name
        return self

    def of_sex(self, sex):
        self.sex = sex
        return self

    def with_heads(self, heads):
        self.heads = heads
        return self

    def with_legs(self, legs):
        self.legs = legs
        return self

    def with_tails(self, tails):
        self.tails = tails
        return self

    def build(self):
        if(self.species == "dog"):
            self.dog.set_species(self.species)
            self.dog.set_name(self.name)
            self.dog.set_sex(self.sex)
            self.dog.set_nbr_of_heads(self.heads)
            self.dog.set_nbr_of_legs(self.legs)
            self.dog.set_nbr_of_tails(self.tails)
            return self.dog
        if(self.species == "cat"):
            self.cat.set_species(self.species)
            self.cat.set_name(self.name)
            self.cat.set_sex(self.sex)
            self.cat.set_nbr_of_heads(self.heads)
            self.cat.set_nbr_of_legs(self.legs)
            self.cat.set_nbr_of_tails(self.tails)
            return self.cat
