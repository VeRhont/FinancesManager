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


def save_entry(entry, date, amount, category):
    with open('account_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        if date not in data[0][entry]:
            data[0][entry][date] = {}

        if category not in data[0][entry][date]:
            data[0][entry][date][category] = amount
        else:
            data[0][entry][date][category] += amount

    with open('account_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))


def delete_entry(date, category):
    print(date, category)
