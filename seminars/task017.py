""" Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

list = [1, 1, 2, 0, -1, 3, 4, 4]
unic = set()

for i in range(len(list)):
    unic.add(list[i])

print(len(unic))