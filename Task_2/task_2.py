#Найти максимальное из пяти чисел
list = [1, 3, 0, 5, 2]
max = 0
for i in list:
    if i > max:
        max = i
print (max)