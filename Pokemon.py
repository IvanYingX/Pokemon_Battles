class Pokemon:
    def __init__(self, hp, name, attack, defense, moves=None):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        if moves is None:
            self.moves = []
            self.moves.append(Attack('Pound', 40, 30, 30, 'Normal'))
        else:
            self.moves = moves
        self.move_names = [x.name for x in self.moves]
    def fight(self, other):
        
        while True:
            print(f'{self.name} has the following moves')
            for i in self.move_names:
                print(i)
            move = input(f"What should {self.name} use? \n")
            if move not in self.move_names:
                print(f'{self.name} doesn\'t know that move')
            else:
                break
        idx = self.move_names.index(move)
        move = self.moves[idx]
        other.hp -= self.attack * move.power
        move.pp -= 1

class Attack:
    def __init__(self, name, power, pp, max_pp, elemental_type):
        self.name = name
        self.power = power
        self.pp = pp
        self.max_pp = max_pp
        self.elemental_type = elemental_type
    def __repr__(self):
        return self.name