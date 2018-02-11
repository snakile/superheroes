from pony.orm import *


class Character:
    db = Database()
    db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

    class CharacterEntity(db.Entity):
        name = Required(str)
        gender = Required(str)
        origin = Required(str)
        powers = Required(str)

    db.generate_mapping(create_tables=True)

    def __init__(self, name, gender, origin, powers):
        self.name = name if name else 'No Name'
        self.gender = gender if gender else 'No Gender'
        self.origin = origin if origin else 'No Origin'
        self.powers = powers

    @staticmethod
    def create_character(character_entity):
        return Character(character_entity.name, character_entity.gender, character_entity.origin, character_entity.powers)

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


def main():
    powers = ['Flight', 'Force Field', 'Magnetism', 'Gadgets', 'Electronic interaction', 'Power Item', 'Leadership']
    cosmic_boy = Character(name='Cosmic Boy', gender='male', origin='Alien', powers=powers)
    cosmic_girl = Character(name='Cosmic Girl', gender='female', origin='Female Alien', powers=powers[:3])
    powerless = Character(name='John Smith', gender='male', origin='Human', powers=[])
    cosmic_boy.save()
    cosmic_girl.save()
    powerless.save()
    Character.show_all_characters()


if __name__ == '__main__':
    main()
    # with db_session:
    #     delete(character for character in Character.CharacterEntity if character.name == 'Kroosh')
    #     Character.show_all_characters()
