from pony.orm import *


class Power:
    db = Database()
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

    class PowerEntity(db.Entity):
        name = Required(str)
        characters = Required(str)
        numFemales = Required(int)
        numMales = Required(int)

    db.generate_mapping(create_tables=True)

    def __init__(self, name):
        self.name = name if name else 'No Name'

    def add_character(self):
        self.characters.insert(character)

    @db_session
    def save(self):
        powers = '|'.join(self.powers)
        powers = 'No Powers' if not powers else powers
        return Character.CharacterEntity(name=self.name, gender=self.gender, origin=self.origin, powers=powers)

    @staticmethod
    def show_all_characters():
        with db_session:
            query = select(character for character in Character.CharacterEntity)
            query.show()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'name: {}, gender: {}, origin: {}\npowers: {}'.format(self.name, self.gender, self.origin, self.powers)