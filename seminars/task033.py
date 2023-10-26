""" Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

ball_list = [1, 3, 3, 3, 2]
          
def replace_max_ball(list1, min_ball, max_ball):
    for ball in range(len(list1)):
        if list1[ball] == max_ball:
            list1[ball] = min_ball
    
    print(list1)

replace_max_ball(ball_list, min(ball_list), max(ball_list))