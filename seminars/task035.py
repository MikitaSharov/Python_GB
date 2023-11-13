""" Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
"""

def prime_number(number):
    if number > 1:    
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    return False
print(prime_number(0))

# рекурсия

# count = 0
# def prosto(n, i = 2):
#     if n == 2 or i * i > n:
#         return True
#     if n % i == 0:
#         return False
#     return prosto(n, i+1)

# print(prosto(10))
    