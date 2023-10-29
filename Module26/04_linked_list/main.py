# TODO здесь писать код
from typing import Any


class Node:
    """
        Класс описания узла списка
    """
    def __init__(self, date=None, ind=None) -> None:
        """
        :param data[Any]: данные, размещаемые в узле списка
        :param ind: ссылка на следующий элемент списка
        """
        self.data = date
        self.next = ind


class LinkedList:
    """
        Класс создания связанного списка
    """
    count = 0  # Количество созданных элементов

    def __init__(self) -> None:
        self.pointer = Node()  # Указатель на начало списка

    def append(self, value) -> None:
        """
            Добавление узла к списку
        :param value:[Any] Значение узла
        """
        new_node = Node(value)  # Создаем новый узел
        if self.pointer is None:
            # Если список пуст, то добавляем новое значение и возвращаемся
            # к точке вызова метода
            self.pointer = new_node
            return
        # Если список не пуст - идем к началу списка
        current = self.pointer
        self.count += 1  # Увеличиваем количество элементов на 1
        while current.next is not None:
            # Перемещаемся по узлам списка пока не найдем последний
            current = current.next
        # В поле ссылки последнего элемента списка добавляем новый узел
        current.next = new_node

    def print_lst(self) -> None:
        """
            Вывод всего списка на экран
        """
        if self.pointer is None:
            # Если в списке нет элементов
            print('Нет элементов.')
            return
        else:
            # Если список не пуст - идем к началу списка
            curr_node = self.pointer
            # Перемещаемся по узлам списка пока не найдем последний
            while curr_node is not None:
                if curr_node.data is not None:
                    # Если узел содержит данные, то выводим на экран
                    print(curr_node.data, end=' ')
                # Переходим к следующему узлу
                curr_node = curr_node.next

    def remove(self, index) -> None:
        """
            Удаление узла списка с указанным индексом
            :param index:[int] Индекс удаляемого узла
        """
        # На начало списка
        curr_node = self.pointer
        prev_idx = index - 1  # Индекс узла списка перед удаляемым
        for _ in range(prev_idx):
            # Перемещаемся к узлу с индексом prev_idx
            curr_node = curr_node.next
        # Ссылке текущего узла присваиваем ссылку удаляемого узла
        curr_node.next = curr_node.next.next
        # Уменьшаем количество узлов списка на 1
        self.count -= 1
        return

    def get(self, index) -> Any:
        """
            Получение данных узла по указанному индексу
        :param index: [int] индекс узла
        :return: данные узла
        """
        if index not in range(1, self.count + 1):
            # Если задан индекс меньший 1 или больше количества элементов списка
            print('Такого индекса в списке нет.')
            return
        curr_node = self.pointer  # На начало списка
        # Проходим по узлам списка
        for i_node in range(self.count + 1):
            if i_node == index:
                # Как только находим нужный узел - возвращаем его значение
                return curr_node.data
            # Переход к следующему узлу
            curr_node = curr_node.next

    def __iter__(self) -> Any:
        """
            Итерирование связанного списка
        :return: [Any] Данные очередного узла
        """
        # На начало списка
        curr_node = self.pointer
        curr_node = curr_node.next
        # Проходим по узлам списка
        while curr_node is not None:
            # Возвращаем значение
            yield curr_node.data
            # Переход к следующему узлу
            curr_node = curr_node.next


# Формирование связанного списка и вывод его на экран
my_list = LinkedList()
for idx in range(10, 110, 10):
    my_list.append(idx)
print('Текущий список:')
my_list.print_lst()
print('\nКоличество элементов списка - ', my_list.count)

# Итерирование по списку с помощью цикла
for item in my_list:
    print(item)

# Получение элемента по индексу
number = int(input('Укажите индекс: '))
data = my_list.get(number)
print(f'Получение элемента с индексом {number} - {data}')

# Удаление элемента по индексу
number = int(input('Укажите индекс удаляемого элемента: '))
my_list.remove(number)
my_list.print_lst()
print('\nКоличество элементов списка - ', my_list.count)
