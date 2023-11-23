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


# if __name__ == '__main__':
#     save_entry('income', '03.12.2023', 10000, 'стипендия')
#     save_entry('expenses', '03.12.2023', 200, 'обед')
#     save_entry('expenses', '03.12.2023', 500, 'продукты')
#     save_entry('expenses', '04.12.2023', 267, 'продукты')
#     save_entry('expenses', '07.12.2023', 2000, 'оплата жилья')
#     save_entry('expenses', '10.12.2023', 300, 'интернет')
#     save_entry('income', '10.12.2023', 1000, 'подарок')