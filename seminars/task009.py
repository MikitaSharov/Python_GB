""" По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input: 5
Output: 120
"""

n = 6
N = 1

while n > 0:
    N *= n
    n -= 1
print(N)