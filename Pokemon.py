class Pokemon:
    def __init__(self, hp, name, attack, defense, elemental_type, moves=None):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        self.elemental_type = elemental_type
        if moves is None:
            self.moves = []
            self.moves.append(Attack('Pound', 40, 30, 30, 'Normal'))
        else:
            self.moves = moves
        self.move_names = [x.name for x in self.moves]

    def fight(self, other):
        while True:
            print(f'{self.name} has the following moves')
            print('\t'.join(self.move_names))
            move = input(f"\nWhat should {self.name} use?\t")
            if move not in self.move_names:
                print(f'{self.name} doesn\'t know that move')
            else:
                break
        idx = self.move_names.index(move)
        move = self.moves[idx]
        if move.elemental_type == 'Fire' and other.elemental_type == 'Grass':
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
    def __init__(self, name, power, pp, max_pp, elemental_type):
        self.name = name
        self.power = power
        self.pp = pp
        self.max_pp = max_pp
        self.elemental_type = elemental_type
    def __repr__(self):
        return self.name