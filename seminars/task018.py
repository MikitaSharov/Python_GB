""" Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:
    
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
"""

list_1 = [1, 2, 3, 4, 5]
k = 6
base_diff = k - list_1[0]
nearest_k = []

for i in list_1:
    diff = abs(k - i)
    
    if diff < base_diff and i != k:
        base_diff = diff
        nearest_k = [i]
    elif diff == base_diff:
        nearest_k.append(i)
        
print(*nearest_k)