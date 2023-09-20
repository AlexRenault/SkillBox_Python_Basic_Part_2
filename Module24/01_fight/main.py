# TODO здесь писать код
from battle import Battle

mission = Battle(2)
print('До начала боя:')
mission.print_info()

while mission.end():
    mission.attack()


