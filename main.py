from Game import *
import pokeapi
import os

pokemon_ls = pokeapi.get_pokemon(3)
pokemon_dict = {}

for pokemon in pokemon_ls.json():
    pokeapi.get_defense(pokemon)

# pound = Pokemon.Attack('Pound', 40, 30, 'Normal')
# ember = Pokemon.Attack('Ember', 40, 20, 'Fire')
# vine_whip = Pokemon.Attack('Vine Whip', 45, 25, 'Grass')
# charmander_moveset = [pound, ember]
# bulbasaur_moveset = [pound, vine_whip]

# charmander = Pokemon.Pokemon(200, 'Charmander', 30, 20, 'Fire')
# bulbasaur = Pokemon.Pokemon(200, 'Bulbasaur', 30, 20, 'Grass')

# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(f'What will {charmander.name} do?')
#     flag = charmander.fight(bulbasaur)
#     if flag == False:
#         break
#     Pokemon.slow_print(f'{bulbasaur.name} has {bulbasaur.hp} points left\n')
#     input('Press Enter to continue')
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(f'What will {bulbasaur.name} do?')
#     flag = bulbasaur.fight(charmander)
#     if flag == False:
#         break
#     Pokemon.slow_print(f'{charmander.name} has {charmander.hp} points left\n')
#     input('Press Enter to continue')
