
a = int(input('Введите любое число: '))
if a % 5 == 0 and a % 10 == 0 or a % 15 == 0 and a % 30 != 0:
    print('Кратно')
else:
    print('Некратно')