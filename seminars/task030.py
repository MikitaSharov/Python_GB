""" Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15 """

def arifm_progres(first_el, diff, qty_elements):
    result = [first_el]
    for i in range(qty_elements - 1):
        result.append(result[i] + diff)
    print(result)

arifm_progres(7, 2, 5)