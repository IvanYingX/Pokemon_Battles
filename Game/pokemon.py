class Pokemon:
    def __init__(self, name, hp, attack, defense, elemental_type, moves=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.elemental_type = ElementalType(elemental_type)
        self.moves = []
        if moves is None:
            self.moves.append(Attack('Pound', 40, 30, 30, 'Normal'))
        elif type(moves)=='list':
            self.moves.extend(moves)
        else:
            self.moves.append(moves)
        self.move_names = [x for x in self.moves]

    def fight(self, other):
        print(f'{self.name} has the following moves')
        for i in range(0,len(self.move_names)):
            print(self.move_names[i], 'pp: ', self.moves[i].pp)
        move = input(f"What should {self.name} use? \n")
        idx = self.move_names.index(move)
        move = self.moves[idx]
        if move.name not in self.move_names:
            print(f'{self.name} doesn\'t know that move')
        elif self.moves[idx].pp==0:
            print("f'{self.name}' cannot use f'{move.name}' anymore")
    
        if move.elemental_type != 'Normal':
            print('is normal')
            if move.elemental_type > other.elemental_type:
                other.hp -= 2*self.attack + move.power - other.defense
                print("It's very effective!")
            elif move.elemental_type <= other.elemental_type:
                other.hp -= self.attack/2 + move.power - other.defense
                print("It's not very effective...")
        else:
            other.hp -= self.attack + move.power - other.defense
            move.pp -= 1
            print(f'{other.name} has {other.hp} hp left.')
                
    def __repr__(self):
        return self.name



class Attack:
    def __init__(self, name, power, pp, max_pp, elemental_type):
        self.name = name
        self.power = power
        self.pp = pp
        self.max_pp = max_pp
        self.elemental_type = ElementalType(elemental_type)
    def __repr__(self):
        return self.name
    def __iter__(self):
        return self.name
    def __len__(self):
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
        return (self.element == other.element)
    
    def __lt__(self, other):
        return (other > self)

    def __le__(self, other):
        return ((other > self) or (self == other))
    
    def __ge__(self, other):
        return ((self > other) or (self == other))

    def __ne__(self, other):
        return (self.element != other)



if __name__ == '__main__':

    fire = ElementalType('Fire')
    grass = ElementalType('Grass')
    water = ElementalType('Water')
    #print(grass <= fire)
