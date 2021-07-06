from Game import *

Pound = pokemon.Attack('Pound', 40, 30, 30, 'normal')
FireBlast = pokemon.Attack('Fire Blast', 100, 10, 10, 'Fire')
Thunder = pokemon.Attack('Thunder', 120, 5, 5, 'fire')
Jump = pokemon.Attack('Jump', 0, 40, 40, 'normal')

pikachu = pokemon.Pokemon(200, 'Pikachu', 30, 20, 'Normal', [Pound, FireBlast, Thunder])
bulbasaur = pokemon.Pokemon(200, 'Bulbasaur', 30, 20, 'Grass')
magikarp = pokemon.Pokemon(150, 'Magikarp', 10, 10, 'Water', Jump)

satoshi = trainer.Trainer([pikachu, bulbasaur, magikarp])

print(satoshi[0])


# while True:
#     if pikachu.hp>0:
#         pikachu.fight(bulbasaur)
#     else:
#         print("Pikachu is incapacitated!")
#     if bulbasaur.hp>0:
#         bulbasaur.fight(pikachu)
#     else:
#         print("Bulbasaur is incapacitated!")
#         break

