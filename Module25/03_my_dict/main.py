# TODO здесь писать код
class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


control = MyDict({i: i * 2 for i in range(10)})
print(control)
print()
for idx in range(len(control)):
    print('Если ключ есть: ', control.get(idx),
          '\t Если ключа нет: ', control.get(idx + 10))

