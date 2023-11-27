from prettytable import PrettyTable
from colorama import Fore, init
from data_manager import get_data, save_entry, delete_entry, save_balance


def print_entries(entries):
    END = '\033[0m'

    table = PrettyTable()
    table.field_names = ['ID', 'Дата', 'Категория', 'Сумма']

    id = 1
    for date in entries.keys():
        for category, amount in entries[date].items():
            colored_amount = str(amount) + END
            table.add_row([id, date, category, colored_amount])
            id += 1

    print(table)
    return table


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

    category = input('Введите категорию: ').strip().lower()

    if user_input == 'р':
        new_balance = balance - int(amount)
        amount = '\033[91m' + amount


        save_balance(new_balance)
        save_entry('expenses', date, amount, category)

    elif user_input == 'д':
        new_balance = balance + int(amount)
        amount = '\033[92m' + amount

        save_balance(new_balance)
        save_entry('income', date, amount, category)

    else:
        print(f'{Fore.RED}Неверная команда!')

    print(f'{Fore.LIGHTGREEN_EX}Запись добавлена!')
    print()


def delete():

    table = show_all_entries('в')
    id = int(input('Введите номер записи, которую хотите удалить: ')) - 1

    row_to_delete = table.rows[id]

    delete_entry(row_to_delete[1], row_to_delete[2])

    print('Запись удалена!')
    print()


def show_all_entries(user_input='-'):
    account_data = get_data()

    if user_input == '-':
        user_input = input('Выберите: все записи (в), расходы (р) или доходы (д): ').strip().lower()

    if user_input == 'р':
        expenses = account_data[0]['expenses']
        print_entries(expenses)

    elif user_input == 'д':
        incomes = account_data[0]['income']
        print_entries(incomes)

    elif user_input == 'в':

        all_entries = account_data[0]['expenses']

        for date, entry in account_data[0]['income'].items():
            if date in all_entries.keys():
                all_entries[date] |= entry
            else:
                all_entries[date] = entry

        entries = print_entries(all_entries)
        return entries

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
            delete()

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
