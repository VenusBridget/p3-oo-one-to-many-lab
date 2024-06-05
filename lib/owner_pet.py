class Pet:
    pass

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
        if pet_type not in Pet.PET_TYPES:
            raise ('Invalid pet type')

    @property
    def owner (self):
        return self._owner

    @owner.setter
    def owner (self, value):
        if isinstance (value, Owner):
            self._owner = value
        else:
            raise TypeError ('Owner must be an instance of Owner class')

class Owner:
    pass
    def __init__(self, name):
        self.name = name

    def pets (self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self,pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError ("Pet must be an instance of Pet class")

    def get_sorted_pets(self):
        return sorted (self.pets(), key=lambda pet: pet.name)
