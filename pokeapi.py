import requests
import pprint

def get_pokemon():
    ROOT = 'https://pokeapi.co/api/v2/'
    pokemon_ls = []
    for i in range(1,3):
        pokemon = requests.get(ROOT + f'pokemon/{i}')
        pokemon_ls.append(pokemon)
    
    return pokemon_ls

if __name__ == '__main__':
    pokemon_ls = get_pokemon()
    print(pokemon_ls[0].json().keys())
    print(pokemon_ls[0].json()['name'])
    print(pokemon_ls[0].json()['types'][0]['type']['name'])
    print(pokemon_ls[0].json()['stats'][4]['stat'])