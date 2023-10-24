""" Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. """

A = 2
B = 5

def exp(number, exponenta):
    if exponenta == 1:
        return number
    else:
        return number * exp(number, exponenta - 1)

print(exp(A, B))