from Pokemon import Pokemon
from Pokemon import Attack
import time

thunder = Attack('Thunder', 150, 5, 5, 'Electric')
pound = Attack('Pound', 40, 30, 30, 'Normal')
ember = Attack('Ember', 40, 20, 20, 'Fire')
vine_whip = Attack('Vine Whip', 45, 25, 25, 'Grass')
pikachu_moveset = [pound, thunder, ember]
bulbasaur_moveset = [pound, vine_whip]

pikachu = Pokemon(200, 'Pikachu', 30, 20, 'Electric', moves=pikachu_moveset)
bulbasaur = Pokemon(200, 'Bulbasaur', 30, 20, 'Grass', moves=bulbasaur_moveset)

while True:
    flag = pikachu.fight(bulbasaur)
    if flag == False:
        break
    print(f'{bulbasaur.name} has {bulbasaur.hp} points left\n')
    time.sleep(2)
    flag = bulbasaur.fight(pikachu)
    if flag == False:
        break
    print(f'{pikachu.name} has {pikachu.hp} points left\n')
    