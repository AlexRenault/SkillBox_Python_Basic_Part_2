# TODO здесь писать код
def user_menu():
    print('1. Посмотреть текущий текст чата.')
    print('2. Отправить сообщение.')
    action = input('Ваш выбор (1 или 2)? ')
    return action


def read_chat():
    try:
        with open('chat.txt', 'r', encoding='utf-8') as chat_file:
            chat = chat_file.read()
            print(chat)
    except FileNotFoundError:
        print('В чате еще нет ни одного сообщения.')


def send_message(user):
    with open('chat.txt', 'a', encoding='utf-8') as chat_file:
        message = input('Введите сообщение: ')
        chat_file.write(' '.join([user, '\t', message]) + '\n')


def main():
    name = input('Введите имя пользователя: ')
    while True:
        user_choice = user_menu()
        try:
            if user_choice == '1':
                read_chat()
            elif user_choice == '2':
                send_message(name)
            else:
                raise ValueError
        except ValueError:
            print('Введите 1 или 2.')
        except Exception as err:
            print('Ошибка.', err, type(err))
        except KeyboardInterrupt:
            print('Прервано пользователем.')
            break


main()
