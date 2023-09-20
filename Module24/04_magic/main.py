# TODO здесь писать код
import Elements
import random

elements = [Elements.Water(), Elements.Air(),  Elements.Fire(), Elements.Earth()]
count = 0

while count <= 20:
    pair = random.choices(elements, k=2)
    new_element = pair[0] + pair[1]
    print(f'{pair[0].name} + {pair[1].name} = {new_element}')
    count += 1
