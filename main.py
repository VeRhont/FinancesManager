from prettytable import PrettyTable
from colorama import Fore, init
from data_manager import get_data, save_entry, delete_entry, save_balance


def print_entries(entries):
    if not entries:
        print(f'{Fore.RED}Записей нет!\n')
        return False

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
    balance = account_data['balance']

    print(f'Текущий баланс: {Fore.LIGHTBLUE_EX}{balance:.2f} р.')
    print()


def get_all_entries():
    account_data = get_data()
    all_entries = account_data['expenses']

    for date, entry in account_data['income'].items():
        if date in all_entries.keys():
            all_entries[date] |= entry
        else:
            all_entries[date] = entry

    return all_entries


def add_entry():
    balance = get_data()['balance']

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
    if not (amount.isdigit() and float(amount) >= 0):
        print(f'{Fore.RED}Сумма должна быть неотрицательной!')
        print()
        return

    category = input('Введите категорию: ').strip().lower()

    if user_input == 'р':
        new_balance = balance - float(amount)
        amount = '\033[91m' + amount

        save_balance(new_balance)
        save_entry('expenses', date, amount, category)

    elif user_input == 'д':
        new_balance = balance + float(amount)
        amount = '\033[92m' + amount

        save_balance(new_balance)
        save_entry('income', date, amount, category)

    else:
        print(f'{Fore.RED}Неверная команда!')

    print(f'{Fore.LIGHTGREEN_EX}Запись добавлена!')
    print()


def delete():
    table = show_all_entries('в')

    if not table:
        print(f'{Fore.RED}Записей нет!')
        return

    id = input('Введите номер записи, которую хотите удалить (о - отмена): ')
    if id == 'о':
        print(f'{Fore.RED}Отмена удаления')
        print()
        return

    id = int(id) - 1
    if id >= len(table.rows) or id < 0:
        print(f'{Fore.RED}Неверный номер строки')
        print()
        return

    row_to_delete = table.rows[id]

    new_balance = get_data()['balance']
    amount = float(str(row_to_delete[3])[5:-4])

    if row_to_delete[3].startswith('\033[92m'):
        new_balance -= amount
        entry = 'income'
    else:
        new_balance += amount
        entry = 'expenses'

    save_balance(new_balance)
    delete_entry(entry, row_to_delete[1], row_to_delete[2])

    print(f'{Fore.LIGHTGREEN_EX}Запись удалена!')
    print()


def show_all_entries(user_input='-'):
    account_data = get_data()

    if user_input == '-':
        user_input = input('Выберите: все записи (в), расходы (р) или доходы (д): ').strip().lower()

    if user_input == 'р':
        expenses = account_data['expenses']
        print_entries(expenses)

    elif user_input == 'д':
        incomes = account_data['income']
        print_entries(incomes)

    elif user_input == 'в':

        all_entries = get_all_entries()

        entries = print_entries(all_entries)
        return entries

    else:
        print(f'{Fore.RED}Неверная команда!')

    print()


def show_entries_by_date():
    start_date = input('Введите начальную дату: ')
    end_date = input('Введите конечную дату: ')

    all_entries = get_all_entries()

    necessary_entries = {}
    for date in all_entries:
        if start_date <= date <= end_date:
            necessary_entries[date] = all_entries[date]

    print_entries(necessary_entries)


def show_entries_by_category():
    category = input('Введите категорию для сортировки: ')

    all_entries = get_all_entries()

    necessary_entries = {}
    for date in all_entries:
        for c in all_entries[date]:
            if c == category:
                necessary_entries[date] = {c: all_entries[date][c]}

    if necessary_entries:
        print_entries(necessary_entries)
    else:
        print(f'{Fore.RED}Нет записей с этой категорией')
        print()


def interactions():
    print(f'{Fore.LIGHTBLUE_EX}Your Finances')
    print()

    while True:
        user_input = input('Выберите действие:'
                           '\n1 - Просмотр баланса'
                           '\n2 - Добавить запись'
                           '\n3 - Удалить запись'
                           '\n4 - Просмотр всех записей'
                           '\n5 - Просмотр всех записей по дате'
                           '\n6 - Просмотр всех записей по категории'
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

        elif user_input == '5':
            show_entries_by_date()

        elif user_input == '6':
            show_entries_by_category()

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
