""" Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""

A = 5
first_fib = 1
prev_fib = first_fib
next_fib = 0
count_fib = 3

while next_fib < A:
    next_fib = prev_fib + first_fib
    first_fib = prev_fib
    prev_fib = next_fib
    count_fib += 1

if next_fib == A:
    print(count_fib)
else:
    print(-1)