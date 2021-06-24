from Pokemon import Pokemon
from Pokemon import Attack

doubleslap = Attack('Doubleslap', 350, 450, 15, 'Fire')
thunder = Attack('Thunder',150,5,5,'Electric')
pound = Attack('Pound',40,30,30,'Normal')
pikachu_moveset = [pound,thunder, doubleslap]
pikachu = Pokemon(500, 'Pikachu', 30, 20, 'Electric', moves=pikachu_moveset)
bulbasaur = Pokemon(300, 'Bulbasaur', 30, 20, 'Grass')
#pikachu.fight(bulbasaur)
#print(bulbasaur.hp)

while pikachu.hp > 0:
    
    pikachu.fight(bulbasaur)

    bulbasaur.fight(pikachu)
    print('Fight is ongoing', bulbasaur.hp, pikachu.hp)

    
