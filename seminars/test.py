""" 
Пит любит печь торты. У него есть несколько рецептов и ингредиентов. К сожалению, он не силен в математике. Можете ли вы помочь ему узнать, сколько тортов он сможет испечь по его рецептам?

Напишите функцию cakes(), которая принимает рецепт (объект) и доступные ингредиенты (тоже объект) и возвращает максимальное количество тортов, которые Пит может испечь (целое число). Для простоты нет единиц измерения количества (например, 1 фунт муки или 200 г сахара — это просто 1 или 200). Ингредиенты, отсутствующие в объектах, можно принять за 0.

Примеры:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

receipt = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
products = {'sugar': 500, 'flour': 2000, 'milk': 2000}

def cakes(user_receipt_list, user_product_list):
    for product_receipt_list, weight_receipt_list in user_receipt_list.items():
        for product_product_list, weight_product_list in user_product_list.items():
            if product_receipt_list == product_product_list and weight_product_list > weight_receipt_list:
                
    