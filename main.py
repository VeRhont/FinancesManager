from colorama import Fore, init
from data_manager import get_data, save_entry, delete_entry, save_balance


def print_entries(entries, color=Fore.WHITE):
    print('Дата\t\t\tКатегория\t\t\tСумма')
    for date in entries.keys():
        for category, amount in entries[date].items():
            print(f'{date}\t\t{category}\t\t\t{color}{amount}')


def get_balance():
    account_data = get_data()
    balance = account_data[0]['balance']

    print(f'Текущий баланс: {Fore.LIGHTBLUE_EX}{balance} р.')
    print()


def add_entry():
    balance = get_data()[0]['balance']

    user_input = input('Выберите: расходы (р) или доходы (д): ').strip().lower()
    if user_input not in ('р', 'д'):
        print(f'{Fore.RED}Неверная команда!')
        print()
        return

    date = input('Введите дату в формате дд.мм.гггг: ').strip().lower()
    try:
        if not ((1 <= int(date.split('.')[0]) <= 31) and
                (1 <= int(date.split('.')[1]) <= 12) and
                ((0 < int(date.split('.')[2]) <= 9999))):
            print(f'{Fore.RED}Несуществующая дата!')
            print()
            return
    except:
        print(f'{Fore.RED}Неверный формат даты!')
        print()
        return

    amount = input('Введите сумму: ')
    if not (amount.isdigit() and int(amount) >= 0):
        print(f'{Fore.RED}Сумма должна быть неотрицательной!')
        print()
        return
    amount = int(amount)

    category = input('Введите категорию: ').strip().lower()

    if user_input == 'р':
        new_balance = balance - amount

        save_balance(new_balance)
        save_entry('expenses', date, amount, category)

    elif user_input == 'д':
        new_balance = balance + amount

        save_balance(new_balance)
        save_entry('income', date, amount, category)

    else:
        print(f'{Fore.RED}Неверная команда!')

    print(f'{Fore.LIGHTGREEN_EX}Запись добавлена!')
    print()


def delete_entry():
    print('Запись удалена!')
    print()


def show_all_entries():
    account_data = get_data()

    user_input = input('Выберите: все записи (в), расходы (р) или доходы (д): ').strip().lower()

    if user_input == 'р':
        incomes = account_data[0]['expenses']
        print_entries(incomes, Fore.RED)

    elif user_input == 'д':
        expenses = account_data[0]['income']
        print_entries(expenses, Fore.GREEN)

    elif user_input == 'в':
        # TODO
        pass

    else:
        print(f'{Fore.RED}Неверная команда!')

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

        else:
            print(f'{Fore.RED}Неверная команда!')
            print()


def main():
    init(autoreset=True)
    interactions()


if __name__ == '__main__':
    main()
