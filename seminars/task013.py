""" Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в cоответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50
"""

N = int(input('Введите кол-во дней: '))
current_snowbreak_days = 0
max_snowbreak_days = 0

for i in range(N):
    temperatura = int(input(f'Введите температуру для {i + 1} дня: '))
    
    if temperatura > 0:
        current_snowbreak_days += 1
    else:
        current_snowbreak_days = 0
    
    if current_snowbreak_days > max_snowbreak_days:
        max_snowbreak_days = current_snowbreak_days
        
print(f'Максимальная оттепель длилась {max_snowbreak_days} дней')
    