# TODO здесь писать код
from random import choice
class Stack:
    count = 0

    def __init__(self):
        self.items = []

    def add_item(self, value):
        self.items.insert(0, value)
        self.count += 1

    def del_items(self):
        self.items.pop(0)

    def info(self):
        print(self.items)


class TaskManager:
    stack = Stack()

    def info(self):
        for item in self.stack.items:
            for idx, val in enumerate(item):
                if isinstance(val, int):
                    print(val, '.', end=' ')
                elif isinstance(val, str) and idx < len(item) - 1:
                    print(val, end='; ')
                else:
                    print(val, end='.')
            print()

    def new_task(self, task, prior):
        flag = True
        for item in self.stack.items:
            if item[0] == prior:
                item.append(task)
                flag = False
        if flag:
            self.stack.add_item([prior, task])

    # удаление задач по приоритету
    def del_task(self, prior):
        for item in self.stack.items:
            if item[0] == prior:
                self.stack.items.remove(item)

    # Удаление задач по принципу стека
    def del_steck(self):
        self.stack.items.pop(0)

    def sort_task(self):
        self.stack.items.sort()


manager = TaskManager()
for idx in range(5):
    task_str = ''.join(('Задача_', str(idx)))
    priority = choice(range(1, 5))
    manager.new_task(task_str, priority)

manager.info()
manager.sort_task()
print()
manager.info()
print()
manager.del_steck()
manager.info()
print()
priority = int(input('Задайте приоритет удаляемой задачи.'))
manager.del_task(priority)
manager.info()


