# с помощью лямбда функций опрдеделить является ли число 2-х значным

number = '23'

is_two_digit = lambda x: len(number) == 2
result = is_two_digit(number)

print(f"Число {number} является двузначным: {result}")
    