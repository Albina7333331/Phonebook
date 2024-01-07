# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки,
# которую необходимо перенести из одного файла в другой.

def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)


def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
    for contact in enumerate(contacts_list,1):
        print(*contact)

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу\n'
    )
    var_search = input('Выберите вариант поиска: ')

    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорректные данные, нужно ввести число комманды')
        var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
def copy_contact():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        indata = file.read().rstrip().split('\n\n')
    copy_phonebook=open('copy_phonebook.txt','a')
    number_contact=int(input("Введите номер контакта для копирования: "))
    copy_phonebook.write(indata[number_contact-1])
    copy_phonebook.write('\n')
    copy_phonebook.close
def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия:\n'
              '1. Добавить контакт\n'
              '2. Вывести на экран\n'
              '3. Поиск контакта\n'
              '4. Выход из программы\n'
              '5. Копирование '
              )

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4','5'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_contact()
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print('Всего хорошего!')
            case '5':
                copy_contact()

interface()

