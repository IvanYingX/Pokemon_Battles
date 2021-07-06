from .Pokemon import Pokemon, Attack

class Trainer:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def __getitem__(self, n):
        return self.pokemon[n]

if __name__ == '__main__':
    pound = Attack(name='Pound', power=20, max_pp=40, elemental_type='Normal')
    pikachu = Pokemon(hp = 250, name='Pikachu', attack=20, defense=20, elemental_type='Normal', moves=[pound])
    ash = Trainer([pikachu, pikachu, 'Charizard'])
    print(ash[0])
