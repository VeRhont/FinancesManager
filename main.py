from colorama import Fore, init
from data_manager import get_data, save_entry, save_balance


def print_entries(entries):
    print('Дата\t\tСумма')
    for date, amount in entries.items():
        print(f'{date}\t{amount}')


def get_balance():
    account_data = get_data()
    balance = account_data[0]['balance']

    print(f'Текущий баланс: {Fore.LIGHTBLUE_EX}{balance} р.')
    print()


def add_entry():
    balance = get_data()[0]['balance']

    user_input = input('Выберите: расходы (р) или доходы (д): ').strip().lower()
    date_input = input('Введите дату в формате дд.мм.гггг: ').strip().lower()
    amount_input = int(input('Введите сумму: ').strip().lower())

    category = input('Введите категорию: ').strip().lower()

    if user_input == 'р':
        new_balance = balance - amount_input

        save_balance(new_balance)
        save_entry('expenses', date_input, amount_input, category)

    elif user_input == 'д':
        new_balance = balance + amount_input

        save_balance(new_balance)
        save_entry('income', date_input, amount_input, category)

    else:
        print('Неверная команда')

    print('Запись добавлена!')
    print()


def delete_entry():
    print('Запись удалена')
    print()


def show_all_entries():
    account_data = get_data()

    user_input = input('Выберите: все записи (в), расходы (р) или доходы (д): ').strip().lower()

    if user_input == 'р':
        incomes = account_data[0]['income']
        print_entries(incomes)

    elif user_input == 'д':
        expenses = account_data[0]['expenses']
        print_entries(expenses)

    elif user_input == 'в':
        print(account_data[0]['income'])
        print(account_data[0]['expenses'])

    else:
        print('Неверная команда')

    print()


def interactions():
    print('Finances')

    while True:
        user_input = input('Выберите действие:'
                               '\n1 - Просмотр баланса'
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
    init(autoreset=True)
    interactions()


if __name__ == '__main__':
    main()
