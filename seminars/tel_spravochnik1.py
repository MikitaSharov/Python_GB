def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить контакт',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Сохранить изменения в справочнике',
          '8. Закончить работу', sep = '\n')
    choice=int(input("Введите команду: "))
    return choice

def read_txt(txt_file_name):
    result_list=[] # будет формироваться список словарей: один контакт - один словарь с 4 ключами
    fields=['id','Фамилия', 'Имя', 'Телефон', 'Описание']
    data_txt=open(txt_file_name, 'r', encoding='utf-8')
    for line in data_txt:
        if line!='\n':
            # current_contact=line.split(',')
            # result_list.append({'Фамилия': current_contact[0],
            # 'Имя': current_contact[1], 
            # 'Телефон': current_contact[2],
            # 'Описание': current_contact[3]
            # })
            result_list.append(dict(zip(fields, map(lambda x: x.strip(), line.split(','))))) # заменим 18-23 строки на одну строкой
    data_txt.close()
    return result_list

def print_result(phnb_lst): # На вход идет список словарей: один контакт - один словарь с 4 ключами 
    for i in phnb_lst:
        for k,v in i.items():
            print (k,':',v)
        print()

def print_phonebook(phnb_lst):
    fields=['id:','Фамилия:', 'Имя:', 'Телефон:', 'Описание:']
    correct_size_for_print=lambda x,n:x+''.join([' ' for i in range(n-len(x))]) # функция добавляет недостающее количество пробелов до фиксированного размера n
    for k in fields:
        if k!='id:':
            print(correct_size_for_print(k,20),end='')
        else:
            print(correct_size_for_print(k,6),end='')
    print('\n')
    for i in phnb_lst:
        for k,v in i.items():
            if k!='id':
                print(correct_size_for_print(v,20),end='')
            else:
                print(correct_size_for_print(v,6),end='')
        print()
    print('\n')


def give_id_to_new_contact(phnb_lst):
    if len(phnb_lst)!=0:
        return str(max([int(i['id']) for i in phnb_lst])+1)
    else:
        return str(1)


def find_number_by_lastname(phnb_lst, last_name): # На вход идет список словарей: один контакт - один словарь с 4 ключами; второй параметр - фамилия
    find_lst=[] # людей с одной и той же фаимилией может быть несколько
    for i in phnb_lst:
        if i['Фамилия']==last_name:
            find_lst.append(i)
    if len(find_lst)!=0:
        if len(find_lst)>1:
            print("Найдено несколько контактов с такой фамилией\n")
            for c in find_lst:
                print(c['Фамилия'], c['Имя'], c['Телефон'])
        else:
            print(find_lst[0]['Телефон'])
    else:
        print('Контакта с такой фамилией нет')


def find_contact_index_for_changing(phnb_lst,last_name): # будет использована при поиске контакта для изменения или удаления записи
    find_lst=[] # людей с одной и той же фаимилией может быть несколько
    for i in range(len(phnb_lst)):
        if phnb_lst[i]['Фамилия']==last_name:
            find_lst.append(i) # будем заносить сюда индексы всех контактов с такой фамилией в списке телефонного справочника
    if len(find_lst)!=0:
        if len(find_lst)>1:
            print("Найдено несколько контактов с такой фамилией, необходимо уточнить id\n")
            print_result([phnb_lst[cont_ind] for cont_ind in find_lst])
            id=input("Введите id для уточнения: ")
            not_find_id=True
            for cont_ind in find_lst:
                if phnb_lst[cont_ind]['id']==id:
                        return cont_ind
            if not_find_id:
               return 'Контакта с таким id нет'
        else:
            return find_lst[0]
    else:
        return 'Контакта с такой фамилией в отобранном списке нет'

# def change_number_test(phnb_lst,last_name,new_num):  
#     cont_ind=find_contact_index_for_changing(phnb_lst,last_name)
#     if type(cont_ind)==str:
#         print(cont_ind) 
#     else:
#         phnb_lst[cont_ind]['Телефон']=new_num
#         print("Номер контакта успешно изменен\n")
#         print_result([phnb_lst[cont_ind]])

def show_edit_menu():
    print('1. Фамилия',
          '2. Имя',
          '3. Телефон',
          '4. Описание',
          '5. Подтвердить изменения',
          '6. Отменить изменения', sep = '\n')  # id менять нельзя, он будет у каждого уникальный и будет назначаться при создании автоматически
    choice=int(input("Введите команду: "))
    return choice

def edit_contact(phnb_lst,last_name):
    cont_ind=find_contact_index_for_changing(phnb_lst,last_name)
    if type(cont_ind)==str:
        print(cont_ind) 
    else:
        print_result([phnb_lst[cont_ind]])
        choice=show_edit_menu()
        fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
        edit=False
        edited_contact=phnb_lst[cont_ind].copy()
        while choice not in [5,6]:
            k=fields[choice-1]
            new_data=input(f'{k}: ')
            edited_contact[k]=new_data
            edit=True
            choice=show_edit_menu()
        if choice==5 and edit==True:
            print("Контакт изменен")
            phnb_lst[cont_ind]=edited_contact
            print_result([phnb_lst[cont_ind]])
            

def delete_by_lastname(phnb_lst,last_name):
    cont_ind=find_contact_index_for_changing(phnb_lst,last_name)
    if type(cont_ind)==str:
        print(cont_ind) 
    else:
        print_result([phnb_lst[cont_ind]])
        delete=''
        while delete not in ['yes','no']:
            delete=input("Подтвердите удаление данного контакта - напечатайте yes или no: ")
        if delete=='yes':
            phnb_lst.pop(cont_ind)
            print("Данный контакт удален\n")

def find_by_number(phnb_lst, tel_number):
    not_find_contact=True
    for i in phnb_lst:
        if i['Телефон']==tel_number:
            print_result([i]) # return i
            not_find_contact=False
    if not_find_contact:
        print("Контакта с таким номером телефона нет в справочнике")

def add_new_contact(phnb_lst):
    new_contact_data={}
    fields=['id','Фамилия', 'Имя', 'Телефон', 'Описание']
    letter_symbols=[chr(i) for i in range(1040,1104)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)] # все буквенные символы кириллицы и латиницы
    # number_symbols=[chr(i) for i in range(48,58)] # все цифровые символы  # .isdigit(), .isnumber() 
    new_contact_data['id']=give_id_to_new_contact(phnb_lst)
    for i in fields[1:]:
        new_contact_data[i]=input(f'Введите данные для поля "{i}": ').strip().replace(',','') # если вдруг попала запятая в поле, то ее нужно убрать, иначе будет проблема при распаковке справочника программой
    while set(new_contact_data['Фамилия'])&set(letter_symbols)==set():
        print("Поле 'Фамилия' обязательно для заполнения и должно содержать буквенные символы")
        new_contact_data['Фамилия']=input(f"Введите данные для поля 'Фамилия': ").strip().replace(',','')
    if new_contact_data['Телефон'] in [i['Телефон'] for i in phnb_lst]:
        exist_number_ind=[i['Телефон'] for i in phnb_lst].index(new_contact_data['Телефон']) # находим индекс контакта, у которого оказался такой же номер телефона
        print("Контакт с таким номером уже существует!")
        print_result([phnb_lst[exist_number_ind]])
    else:
        phnb_lst.append(new_contact_data)
        print('Контакт добавлен в справочник')
        print_result([new_contact_data])
    

def write_txt(filename , phnb_lst):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phnb_lst)):
            s='' 
            for v in phnb_lst[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def work_with_phonebook(filename):
	

    choice=show_menu()

    phone_book=read_txt(filename)  # будет формироваться список словарей: один контакт-один словарь с 4 полями 

    while (choice!=8):

        if choice==1: # '1. Распечатать справочник'
            print_phonebook(phone_book)
        elif choice==2: # '2. Найти телефон по фамилии'
            last_name=input('lastname ')
            find_number_by_lastname(phone_book,last_name)
        elif choice==3: # '3. Изменить контакт'
            last_name=input('lastname ')
            edit_contact(phone_book,last_name)
        elif choice==4: # '4. Удалить запись'
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
        elif choice==5: # '5. Найти абонента по номеру телефона'
            number=input('number ') 
            find_by_number(phone_book,number)
        elif choice==6: # '6. Добавить абонента в справочник'
            add_new_contact(phone_book)
        elif choice==7: # '7. Сохранить изменения в справочнике'
            write_txt(filename,phone_book)
        choice=show_menu()



work_with_phonebook('phonebook.txt')