import requests
# import pprint

def get_pokemon(n):
    ROOT = 'https://pokeapi.co/api/v2/'
    pokemon_ls = []
    for i in range(1, n + 1):
        pokemon = requests.get(ROOT + f'pokemon/{i}')
        pokemon_ls.append(pokemon)
    
    return pokemon_ls
    

def get_attack(json):
# Second in the list
    attack = json['stats'][1]['base_stat']
    return attack

def get_hp(json):
# First in the list
    attack = json['stats'][0]['base_stat']
    return attack

def get_defense(json):
# Third in the list
    attack = json['stats'][2]['base_stat']
    return attack


if __name__ == '__main__':
    pokemon_ls = get_pokemon(1)
    # print(pokemon_ls[0].json())
    # print(pokemon_ls[0].json().keys())
    # print(pokemon_ls[0].json()['name'])
    # print(pokemon_ls[0].json()['types'][0]['type']['name'])
    for item in pokemon_ls[0].json()['stats']:
        print(item)
    # print(pokemon_ls[0].json()['stats'])
    # print(pokemon_ls[0].json()['stats'][0]['stat']['name'])