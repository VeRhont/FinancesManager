import json


def get_data():
    with open('account_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def save_balance(new_balance):
    with open('account_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data[0]['balance'] = new_balance

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))


def save_entry(entry, date, amount):
    with open('account_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data[0][entry][date] = amount

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))
