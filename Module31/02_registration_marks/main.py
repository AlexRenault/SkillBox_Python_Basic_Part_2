# TODO здесь писать код
import re

number = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

person_pattern = (r'\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]\d{3}'
                  r'[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{2,3}')
print('Список номеров частных автомобилей: ')
print(re.findall(person_pattern, number))

print('\nСписок номеров такси: ')
taxi_pattern = r'\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{5,6}'
print(re.findall(taxi_pattern, number))
