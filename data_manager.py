import json


def get_data():
    with open('account_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data[0]


def save_balance(new_balance):
    data = get_data()
    data['balance'] = new_balance

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps([data], indent=2, ensure_ascii=False))


def save_entry(entry, date, amount, category):
    data = get_data()

    if date not in data[entry]:
        data[entry][date] = {}

    if category not in data[entry][date]:
        data[entry][date][category] = amount
    else:
        data[entry][date][category] += amount

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps([data], indent=2, ensure_ascii=False))


def delete_entry(entry, date, category):
    data = get_data()
    data[entry][date].pop(category)

    if data[entry][date] == {}:
        data[entry].pop(date)

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps([data], indent=2, ensure_ascii=False))
