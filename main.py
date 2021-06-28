from Pokemon import Pokemon
from Pokemon import Attack

Pound = Attack('Pound', 40, 30, 30, 'normal')
FireBlast = Attack('Fire Blast', 100, 10, 10, 'Fire')
Thunder = Attack('Thunder', 120, 5, 5, 'fire')
pikachu_moves=[Pound, FireBlast, Thunder]

pikachu = Pokemon(200, 'Pikachu', 30, 20, 'Normal', pikachu_moves)
bulbasaur = Pokemon(200, 'Bulbasaur', 30, 20, 'grass')

print(pikachu.__dir__())
while True:
    if pikachu.hp>0:
        pikachu.fight(bulbasaur)
    else:
        print("Pikachu is incapacitated!")
    if bulbasaur.hp>0:
        bulbasaur.fight(pikachu)
    else:
        print("Bulbasaur is incapacitated!")
        break
