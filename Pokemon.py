from gui import attack_gui

class Pokemon:
    def __init__(self, hp: int, name: str,
                 attack: int, defense: int,
                 elemental_type: str, moves: list = None):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        self.elemental_type = ElementalType(elemental_type)
        if moves is None:
            self.moves = []
            self.moves.append(Attack('Pound', 40, 30, 'Normal'))
        else:
            if len(moves) > 4:
                raise ValueError('Pokemon can\'t learn more than four moves')
            else:
                self.moves = moves
        self.move_names = [x.name for x in self.moves]

    def fight(self, other):
        idx = attack_gui(self.move_names)
        # while True:
        #     print(f'{self.name} has the following moves')
        #     print('\t'.join(self.move_names))
        #     move = input(f"\nWhat should {self.name} use?\t")
        #     if move not in self.move_names:
        #         print(f'{self.name} doesn\'t know that move')
        #     else:
        #         break
        # idx = self.move_names.index(move)
        # move = self.moves[idx]
        move = self.moves[idx]
        
        if move.elemental_type > other.elemental_type:
            other.hp -= 2 * (self.attack * move.power) / other.defense
            print("It's super effective!")
        else:
            other.hp -= (self.attack * move.power) / other.defense

        move.pp -= 1
        if other.hp <= 0:
            other.hp = 0
            print(f'{other.name} has fainted')
            return False

        return True


class Attack:
    def __init__(self, name: str, power: int, max_pp: int, elemental_type: str):
        self.name = name
        self.power = power
        self.pp = max_pp
        self.max_pp = max_pp
        self.elemental_type = ElementalType(elemental_type)
    def __repr__(self):
        return self.name


class ElementalType:
    def __init__(self, element: str):
        possible = ['Grass', 'Fire', 'Water', 'Normal']
        if element.capitalize() not in possible:
            raise ValueError(f"{element.capitalize()} not available")
        else:
            self.element = element.capitalize()
        self.winner = [('Grass', 'Water'),
                       ('Fire', 'Grass'),
                       ('Water', 'Fire')]
    
    def __gt__(self, other):
        return (self.element, other.element) in self.winner
    
    def __eq__(self, other):
        return self.element == other.element
    
    def __lt__(self, other):
        return (other.element > self.element)

if __name__ == '__main__':

    fire = ElementalType('Fire')
    grass = ElementalType('Grass')
    water = ElementalType('Water')
    print(water >= grass)
        
