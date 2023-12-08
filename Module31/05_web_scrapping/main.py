# TODO здесь писать код
import requests, re

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки

pattern = r'(?<=>).+(?=</h3>)'
print(re.findall(pattern, text))

result = requests.get('https://ru.wikipedia.org/wiki/Яндекс_Маркет')
print(re.findall(pattern, result.text))