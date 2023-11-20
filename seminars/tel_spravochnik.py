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

def main():
    file_path = "phonebook.txt"
    contacts = load_data(file_path)

    while True:
        print("\n1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")

        choice = input("Выберите действие (1/2/3/4/5/6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(contacts, last_name, first_name, middle_name, phone_number)
            save_data(file_path, contacts)
        elif choice == '3':
            search_key = input("Выберите характеристику для поиска (last_name/first_name/middle_name/phone_number): ")
            search_value = input("Введите значение для поиска: ")
            results = search_contact(contacts, search_key, search_value)
            if results:
                print("\nРезультаты поиска:")
                display_contacts(results)
            else:
                print("\nНичего не найдено.")
        elif choice == '4':
            last_name = input("Введите фамилию для изменения: ")
            first_name = input("Введите имя для изменения: ")
            middle_name = input("Введите новое отчество: ")
            phone_number = input("Введите новый номер телефона: ")
            update_contact(contacts, last_name, first_name, middle_name, phone_number)
            save_data(file_path, contacts)
        elif choice == '5':
            last_name = input("Введите фамилию для удаления: ")
            first_name = input("Введите имя для удаления: ")
            delete_contact(contacts, last_name, first_name)
            save_data(file_path, contacts)
        elif choice == '6':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

main()