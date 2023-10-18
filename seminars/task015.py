""" Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

N = int(input('Введите кол-во арбузов: '))
current_weight_watermellow = 0
max_weight_watermellow = 0
min_weight_watermellow = float('inf')

for i in range(N):
    weight_watermellow = float(input('Введите вес арбуза: '))
    
    if weight_watermellow > max_weight_watermellow:
        max_weight_watermellow = weight_watermellow
    if weight_watermellow < min_weight_watermellow:
        min_weight_watermellow = weight_watermellow
        
print(min_weight_watermellow, max_weight_watermellow)
        
