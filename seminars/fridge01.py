virus = 'anton'
n = int(input('Введите кол-во холодильников: '))
infected_fridges = []

for i in range(n):
    code_fridge = (input(f'Введите код {i + 1} холодильника: '))

    index = 0
    found = False
    for letter in code_fridge:
        if letter == virus[index]:
            index += 1
        if index == len(virus):
            found = True
            break
    if found:
        infected_fridges.append(i + 1)
print(infected_fridges)