from pony.orm import *

from character import Character


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
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    @db_session
    def save(self):
        characters = '|'.join(f"{character.name} ({character.gender})" for character in self.characters)
        num_females = sum(character.gender == 'female' for character in self.characters)
        num_males = len(characters) - num_females
        return Power.PowerEntity(name=self.name, characters=characters, numFemales=num_females, numMales=num_males)

    @staticmethod
    def show_all_powers():
        with db_session:
            query = select(power for power in Power.PowerEntity)
            query.show()

    @staticmethod
    def generate_all_powers():
        all_powers = {}
        with db_session:
            all_characters = select(character_entity for character_entity in Character.CharacterEntity)
            for character_entity in all_characters:
                character = Character.create_character(character_entity)
                for power_name in character.powers.split('|'):
                    if power_name == 'No Powers':
                        continue
                    if power_name not in all_powers.keys():
                        all_powers[power_name] = Power(power_name)
                    all_powers[power_name].add_character(character)
            return all_powers

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.name}:\n{self.characters}"


def main():
    for power in Power.generate_all_powers().values():
        print(power)
        power.save()


if __name__ == '__main__':
    main()
