from data_manager import get_data, save_data


def get_balance():
    account_data = get_data()
    balance = account_data[0]['balance']

    print(balance)
    print()


def add_entry():
    print('Запись добавлена')
    print()


def delete_entry():
    print('Запись удалена')
    print()



def show_all_entries():
    print('Все записи')
    print()


def interactions():
    print('Finances')

    while True:
        user_input = input('Выберите действие:'
                               '\n1 - Баланс'
                               '\n2 - Добавить запись'
                               '\n3 - Удалить запись '
                               '\n4 - Просмотр всех записей'
                               '\nQ - Выход из приложения'
                               '\n--> ')

        if user_input == '1':
            get_balance()

        elif user_input == '2':
            add_entry()

        elif user_input == '3':
            delete_entry()

        elif user_input == '4':
            show_all_entries()

        elif user_input == 'Q':
            quit()


def main():
    interactions()


if __name__ == '__main__':
    main()
