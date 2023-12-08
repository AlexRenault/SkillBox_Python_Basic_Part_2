# TODO здесь писать код
import requests, re
import json


def find_key(struct, key):
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


address = 'https://swapi.dev/api/starships/'
starships = requests.get(address)
dict_starships = json.loads(starships.text)

ship_list = find_key(dict_starships, 'results')

mill_falcon = list((filter(lambda x: x['name'] == 'Millennium Falcon', ship_list)))
mill_falcon = mill_falcon[0]

ship_dict = dict()
ship_dict['StarShip'] = {'Name': mill_falcon['name'],
                         'Max speed': mill_falcon['max_atmosphering_speed'],
                         'Class': mill_falcon['starship_class']}

pilots_dict = dict()
for item in mill_falcon['pilots']:
    pilot = json.loads(requests.get(item).text)
    home_world = json.loads(requests.get(pilot['homeworld']).text)
    pilots_dict[pilot['name']] = {'Height': pilot['height'], 'Mass': pilot['mass'],
                                  'Home World': home_world['name'],
                                  'Website address': pilot['homeworld']}

ship_dict['Pilots'] = pilots_dict

print(json.dumps(ship_dict, indent=4))
with open('falcon.json', 'w') as file:
    json.dump(ship_dict, file, indent=4)
