""" Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
"""
           
string_input = 'a a a b c a a d c d d'.split()
print(string_input)
dict_result = {}
for i in string_input:
    if i not in dict_result:
        # dict_result[i]=0
        print(i, end=' ')
    else:
        # dict_result[i]+=1
        print(f'{i}_{dict_result[i]}', end=' ')
    dict_result[i]=dict_result.get(i, 0) + 1 # возвращает 0 (в этом случае) или то что напишешь
            