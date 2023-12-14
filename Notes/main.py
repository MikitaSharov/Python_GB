""" Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом репозитории, использовать пул реквесты на изменения. Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.

Критерии оценки
Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.

Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.

Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента. """

from note_manager import NoteManager

def main_menu():
    print("\n1. Показать все заметки")
    print("2. Найти заметку по дате")
    print("3. Добавить заметку")
    print("0. Выход")

def note_menu():
    print("\n1. Просмотреть")
    print("2. Редактировать")
    print("3. Удалить")
    print("4. Назад в главное меню")
    print("0. Выход")

def main ():

    file_path = "Python_GB/Python_GB/Notes/notes.json"
    note_manager = NoteManager(file_path)

    while True:
        main_menu()
        choice_main_menu = input("Выберите действие 1/2/3/0: ")

        if choice_main_menu == "1":
            notes = note_manager.get_notes_list()
            for note in notes:
                print(note.as_dict())
            if not notes:
                print("Заметок нет")
        elif choice_main_menu == "2":
            search_data = input("Для поиска введите дату в фотмате (дд.мм.гг): ")
            matching_notes = note_manager.search_notes_by_data(search_data)
            for note in matching_notes:
                print(note.as_dict())
                if not matching_notes:
                    print("Ничего не найдено")
        elif choice_main_menu == "3":
            title = input("Введите заголовок: ")
            body = input("Введите тело заметки: ")
            note_manager.add_note(title, body)
            print("Заметка создана")
            continue
        elif choice_main_menu == "0":
            print("Пока-пока")
            break
        else:
            print("Что-то не то ввели! Надо циферку от 1 до 3 или 0. Попробуй ещё разок.")
            continue

        note_id = input("Введите ID заметки для работы с ней или ничего для возврата в предыдущее меню: ")

        if not note_id:
            continue
        if note_id.isdigit() :
            note_id = int(note_id)
        else:
            print("Вводить надо цифры. Попробуй еще разок")


        if choice_main_menu == "1" and note_id not in [note.note_id for note in notes]:
            print(f"Заметки с ID {note_id} не существует попробуй еще разок")
            continue
        elif choice_main_menu == "2" and note_id not in [note.note_id for note in matching_notes]:
            print(f"Заметки с ID {note_id} нет в списке поиска. Попробуй еще раз")
        
        selected_note = note_manager.get_note_by_id(note_id)

        while True:
            note_menu()
            choice_note_menu = input("Выберите действие (1/2/3/4/0): ")

            if choice_note_menu == "1":
                if selected_note:
                    print(selected_note.as_dict())
                else:
                    print("Что-то пошло не так =(")
            elif choice_note_menu == "2":
                new_title = input("Введите новый заголовок или оставьте поле пустым (жмите enter), если редактирование не требуется: ")
                new_body = input("Введите новое тело заметки или оставьте поле пустым (жмите enter), если редактирование не требуется: ")
                note_manager.edit_note(note_id, new_title if new_title else selected_note.title, new_body if new_body else selected_note.body)
                print(f"Редактирование заметки {note_id} выполнено")
            elif choice_note_menu == "3":
                note_manager.delete_note(note_id)
                print(f"Заметка {note_id} удалена")
                break
            elif choice_note_menu == "4":
                break
            elif choice_note_menu == "0":
                exit()
            else: 
                print("Что-то не то ввели! Надо циферку от 1 до 4 или 0. Попробуй ещё разок.")

main()