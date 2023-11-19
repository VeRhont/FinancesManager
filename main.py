from data_manager import get_data, save_data


def get_balance():
    account_data = get_data()
    balance = account_data[0]['balance']

    print(balance)
    print()


def add_entry():
    account_data = get_data()

    user_input = input('Выберите: расходы (р) или доходы (д): ').strip().lower()
    date_input = input('Введите дату в формате дд.мм.гггг: ').strip().lower()
    amount_input = int(input('Введите сумму: ').strip().lower())

    if user_input == 'р':
        save_data('expenses', date_input, amount_input)

    elif user_input == 'д':
        print(account_data[2]['expenses'])

    else:
        print('Неверная команда')

    print('Запись добавлена!')
    print()


def delete_entry():
    print('Запись удалена')
    print()



def show_all_entries():
    account_data = get_data()

    user_input = input('Выберите: расходы (р) или доходы (д): ').strip().lower()

    if user_input == 'р':
        print(account_data[1]['income'])

    elif user_input == 'д':
        print(account_data[2]['expenses'])

    else:
        print('Неверная команда')

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
