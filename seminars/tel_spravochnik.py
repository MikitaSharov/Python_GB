import os

def load_data(file_path):
    contacts = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({'last_name': data[0], 'first_name': data[1], 'middle_name': data[2], 'phone_number': data[3]})
    return contacts

def save_data(file_path, contacts):
    with open(file_path, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n")

def display_contacts(contacts):
    for contact in contacts:
        print(f"{contact['last_name']}, {contact['first_name']}, {contact['middle_name']}, {contact['phone_number']}")

def add_contact(contacts, last_name, first_name, middle_name, phone_number):
    contacts.append({'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number})

def search_contact(contacts, key, value):
    results = [contact for contact in contacts if contact[key].lower() == value.lower()]
    return results

def update_contact(contacts, last_name, first_name, middle_name, phone_number):
    for contact in contacts:
        if contact['last_name'].lower() == last_name.lower() and contact['first_name'].lower() == first_name.lower():
            contact['middle_name'] = middle_name
            contact['phone_number'] = phone_number

def delete_contact(contacts, last_name, first_name):
    contacts[:] = [contact for contact in contacts if contact['last_name'].lower() != last_name.lower() or contact['first_name'].lower() != first_name.lower()]

def copy_contact(source_contacts, destination_contacts, line_number):
    if 0 < line_number <= len(source_contacts):
        contact_to_copy = source_contacts[line_number - 1]
        destination_contacts.append(contact_to_copy)
        print("Контакт успешно скопирован.")
    else:
        print("Некорректный номер строки для копирования.")

def main():
    source_file_path = "phonebook_source.txt"
    destination_file_path = "phonebook_destination.txt"

    source_contacts = load_data(source_file_path)
    destination_contacts = load_data(destination_file_path)

    while True:
        print("\n1. Вывести все контакты (Источник)")
        print("2. Вывести все контакты (Назначение)")
        print("3. Добавить контакт")
        print("4. Поиск контакта")
        print("5. Изменить контакт")
        print("6. Удалить контакт")
        print("7. Скопировать контакт из источника в назначение")
        print("8. Выйти")

        choice = input("Выберите действие (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            print("\nКонтакты (Источник):")
            display_contacts(source_contacts)
        elif choice == '2':
            print("\nКонтакты (Назначение):")
            display_contacts(destination_contacts)
        elif choice == '3':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(source_contacts, last_name, first_name, middle_name, phone_number)
            save_data(source_file_path, source_contacts)
        elif choice == '4':
            search_key = input("Выберите характеристику для поиска (last_name/first_name/middle_name/phone_number): ")
            search_value = input("Введите значение для поиска: ")
            results = search_contact(source_contacts, search_key, search_value)
            if results:
                print("\nРезультаты поиска (Источник):")
                display_contacts(results)
            else:
                print("\nНичего не найдено.")
        elif choice == '5':
            last_name = input("Введите фамилию для изменения: ")
            first_name = input("Введите имя для изменения: ")
            middle_name = input("Введите новое отчество: ")
            phone_number = input("Введите новый номер телефона: ")
            update_contact(source_contacts, last_name, first_name, middle_name, phone_number)
            save_data(source_file_path, source_contacts)
        elif choice == '6':
            last_name = input("Введите фамилию для удаления: ")
            first_name = input("Введите имя для удаления: ")
            delete_contact(source_contacts, last_name, first_name)
            save_data(source_file_path, source_contacts)
        elif choice == '7':
            line_number = int(input("Введите номер строки для копирования из источника в назначение: "))
            copy_contact(source_contacts, destination_contacts, line_number)
            save_data(destination_file_path, destination_contacts)
        elif choice == '8':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

main()
