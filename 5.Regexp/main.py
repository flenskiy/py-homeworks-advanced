import re
import csv

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# раскладываем ФИО по нужным полям
for contact in contacts_list:
    full_name = []
    for item in range(3):
        full_name += contact[item].split(' ')
    contact[0] = full_name[0]
    contact[1] = full_name[1]
    contact[2] = full_name[2]

# объединяем одинаковые контакты
contacts_list_len = len(contacts_list)
indexes_to_remove = set()
for i in range(1, contacts_list_len):
    for j in range(i + 1, contacts_list_len):
        if contacts_list[i][0:1] == contacts_list[j][0:1]:
            fields_number = len(contacts_list[i])
            for n in range(2, fields_number):
                if contacts_list[i][n] == '':
                    contacts_list[i][n] = contacts_list[j][n]
                    indexes_to_remove.add(j)

# убираем дублирующиеся записи
for index in indexes_to_remove:
    contacts_list.pop(index)

# приводим телефоны в единый формат
for contact in contacts_list:
    phone_index = 5
    phone_pattern = r'(\+7|8)\s?[(]?(\d{3})[)]?[-|\s]?(\d{3})[-]?(\d{2})[-]?(\d{2})'
    phone_sub_pattern = r'+7(\2)\3-\4-\5'
    extension_phone_pattern = r'[(]?(доб.)\s(\d{4})[)]?'
    extension_phone_sub_pattern = r'\1\2'
    contact[phone_index] = re.sub(phone_pattern, phone_sub_pattern, contact[phone_index])
    contact[phone_index] = re.sub(extension_phone_pattern, extension_phone_sub_pattern, contact[phone_index])

# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
