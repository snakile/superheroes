from pony.orm import *


class Character:
    db = Database()
    db.bind(provider='sqlite', filename=':memory:')

    class CharacterEntity(db.Entity):
        name = Required(str)
        gender = Required(str)
        origin = Required(str)
        powers = Required(str)

    db.generate_mapping(create_tables=True)

    def __init__(self, name, gender, origin, powers):
        self.name = name
        self.gender = gender
        self.origin = origin
        self.powers = powers

    @db_session
    def save(self):
        powers = '|'.join(self.powers)
        return Character.CharacterEntity(name=self.name, gender=self.gender, origin=self.origin, powers=powers)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'name: {}, gender: {}, origin: {}\npowers: {}'.format(self.name, self.gender, self.origin, self.powers)


def main():
    powers = ['Flight', 'Force Field', 'Magnetism', 'Gadgets', 'Electronic interaction', 'Power Item', 'Leadership']
    cosmic_boy = Character(name='Cosmic Boy', gender='male', origin='Alien', powers=powers)
    cosmic_girl = Character(name='Cosmic Girl', gender='female', origin='Female Alien', powers=powers[:3])
    cosmic_boy.save()
    cosmic_girl.save()
    with db_session:
        query = select(character for character in Character.CharacterEntity)
        query.show()


if __name__ == '__main__':
    main()
