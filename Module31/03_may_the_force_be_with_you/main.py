# TODO здесь писать код
import requests
import json
from typing import Any


def find_key(struct, key) -> Any:
    """ поиск заданного ключа key в структуре struct"""
    if key in struct:
        return struct[key]
    else:
        for sub in struct.values():
            if isinstance(sub, dict):
                res = find_key(sub, key)
                if res:
                    break
        else:
            res = None
    return res


def get_website(address) -> Any:
    """получение информации с сайта address"""
    result = requests.get(address)
    if result == 200:
        return json.loads(result.text)
    return None


address = 'https://swapi.dev/api/starships/'
dict_starships = get_website(address)

ship_list = find_key(dict_starships, 'results')

star_ship = list((filter(lambda x: x['name'] == 'Millennium Falcon', ship_list)))
star_ship = star_ship[0]

ship_dict = dict()
ship_dict['StarShip'] = {'Name': star_ship['name'],
                         'Max speed': star_ship['max_atmosphering_speed'],
                         'Class': star_ship['starship_class']}

pilots_dict = dict()
for item in star_ship['pilots']:
    pilot = get_website(item)
    home_world = get_website(pilot['homeworld'])
    pilots_dict[pilot['name']] = {'Height': pilot['height'], 'Mass': pilot['mass'],
                                  'Home World': home_world['name'],
                                  'Website address': pilot['homeworld']}

ship_dict['Pilots'] = pilots_dict

print(json.dumps(ship_dict, indent=4))
with open('falcon.json', 'w') as file:
    json.dump(ship_dict, file, indent=4)
