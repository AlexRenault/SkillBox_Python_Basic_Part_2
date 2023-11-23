# TODO здесь писать код
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        # Каждый элемент списка соответствует ключу.
        self.key_lst = []

    def print_cache(self) -> None:
        """ Вывод кэш"""
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")
        for idx, key in enumerate(self.key_lst):
            print(f'{idx} - {key}')

    @property
    def cache(self):
        """Получаем значение последнего элемента в списке ключей."""
        return self.key_lst[len(self.key_lst) - 1], len(self.key_lst) - 1

    @cache.setter
    def cache(self, new_elem):
        lst = []
        is_del = False
        if len(self.cache_dict) >= self.capacity:
            # удаляем самый редко вызываемый элемент (последний в словаре)
            del_dict, del_lst = self.cache
            self.cache_dict.pop(del_dict)
            self.key_lst.pop(del_lst)
            is_del = True
        self.cache_dict[new_elem[0]] = new_elem[1]  # добавляем новый элемент
        self.key_lst.append(new_elem[0])
        # Если была замена, то перемещаем ключ нового элемента в начало списка ключей
        if is_del:
            self.key_lst.insert(0, self.key_lst.pop(len(self.key_lst) - 1))

    def get(self, key):
        """Получаем значение по ключу. Перемещаем вызываемый элемент в начало списка ключей."""
        for idx, i_key in enumerate(self.cache_dict.keys()):
            if i_key == key:
                break
        self.key_lst[0], self.key_lst[idx] = self.key_lst[idx], self.key_lst[0]
        return self.cache_dict[key]


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2
cache.print_cache()

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
