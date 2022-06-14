# input = [1..25]

while(True):
    x = input()
    try:
        x = int(x)
    except:
        print('Введите число от 1 до 25')
        continue
    if x < 1 or x > 25:
        print('Введите число от 1 до 25')
        continue

    break

abilityList = ['spel1', 'spel2', 'spel3']

while(True):
    x = input()
    if x not in abilityList:
        print('Введите строку из списка: ', abilityList)
        continue
    break

print(x)
