""" Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

def number_from_index_fib(index):
    if index <= 0:
        return 0
    elif index == 1:
        return 1
    else:
        return number_from_index_fib(index - 1) + number_from_index_fib(index - 2)
    
print(number_from_index_fib(7))