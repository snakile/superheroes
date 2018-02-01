class Character:
    def __init__(self, name, gender, origin, powers):
        self.name = name
        self.gender = gender
        self.origin = origin
        self.powers = powers

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'name: {}, gender: {}, origin: {}\npowers: {}'.format(self.name, self.gender, self.origin, self.powers)