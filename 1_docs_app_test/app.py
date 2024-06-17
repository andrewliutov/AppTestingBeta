"""
Необходимые функции для тестирования (добавление, поиск, удаление документов)
"""

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def find_people(number):
    for i in documents:
        if i['number'] == number:
            return i['name']
    else:
        return f'{number}. Номер документа неверен'


def add_doc(type, number, name, shelf_number):
    documents.append({'type': type, 'number': number, 'name': name})
    if shelf_number in directories:
        directories[shelf_number].append(number)
        return f'{type} с номером {number} с именем {name} добавлен в каталог и перечень полок'
    else:
        return f'{shelf_number}. Полки с таким номером нет'


def delete_doc(number):
    for i in documents:
        find = False
        if i['number'] == number:
            documents.remove(i)
            for key, value in directories.items():
                if number in value:
                    shelf = key
                    value.remove(number)
                    find = True
    if find is True:
        return f'Документ с номером {number} удален с полки {shelf}'
    else:
        return 'Документа с таким номером в каталоге нет'


def main():
    print('Поиск имени по номеру документа')
    for number in ['10006', '11-2', '2207 876234', '111']:
        print(find_people(number))
    print()

    print('Добавление документов')
    print(add_doc('паспорт', '123123123', 'Анонимус Опасный', '2'))
    print(add_doc('паспорт', '123456789', 'R2 D2', '4'))
    print()

    print('Удаление документа')
    print(delete_doc('123456789'))


if __name__ == '__main__':
    main()
