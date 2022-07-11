#Показать первую цифру дробной части числа

n = float(input('Введите дробное число через точку: '))
res = round (n - int(n),1) * 10
if res >= 5:
    res -= 1
print (int (res))
