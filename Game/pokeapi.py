import requests

def get_pokemon(n):
    pokestat = {}
    ROOT = 'https://pokeapi.co/api/v2/'

    for i in range(1, n+1):
        link = f'pokemon/{i}'
        r = requests.get(ROOT+link)
        pname = r.json()['name']
        pokestat[pname] = {'hp':None, 'attack':[], 'defense':[], 'elemental_type':[]}

        for n in range(0,3):
            stat = r.json()['stats'][n]['base_stat']
            stat_type = r.json()['stats'][n]['stat']['name']
            pokestat[pname][stat_type] = stat
        pokestat[pname]['elemental_type'] = r.json()['types'][0]['type']['name']
    return pokestat

def get_pokemon_byName(x):
    pokename = x.lower()
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokename)
    pokestat = {}
    pokestat[pokename]= {'hp':None, 'attack':[], 'defense':[], 'elemental_type':[]}

    for n in range(0,3):
        stat = r.json()['stats'][n]['base_stat']
        stat_type = r.json()['stats'][n]['stat']['name']
        pokestat[pokename][stat_type] = stat
    pokestat[pokename]['elemental_type'] = r.json()['types'][0]['type']['name']

    return pokestat