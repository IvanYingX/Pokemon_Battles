from Pokemon import Pokemon
from Pokemon import Attack
import time

pound = Attack('Pound', 40, 30, 'Normal')
ember = Attack('Ember', 40, 20, 'Fire')
vine_whip = Attack('Vine Whip', 45, 25, 'Grass')
charmander_moveset = [pound, ember]
bulbasaur_moveset = [pound, vine_whip]

charmander = Pokemon(200, 'Charmander', 30, 20, 'Fire', moves=charmander_moveset)
bulbasaur = Pokemon(200, 'Bulbasaur', 30, 20, 'Grass', moves=bulbasaur_moveset)

while True:
    flag = charmander.fight(bulbasaur)
    if flag == False:
        break
    print(f'{bulbasaur.name} has {bulbasaur.hp} points left\n')
    time.sleep(2)
    flag = bulbasaur.fight(charmander)
    if flag == False:
        break
    print(f'{charmander.name} has {charmander.hp} points left\n')
    