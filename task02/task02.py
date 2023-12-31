# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число
# ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена 
# система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним. Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9

def max_berry_three_bush(num:int):
    """
    Функция, возвращающая максимальное количество ягод,
    которые можно собрать за один раз с трех кустов.
    На вход функции подается количество кустов.
    """
    berry = []
    for i in range(num):
        berry.append(int(input("Введите количество ягод на кусте: ")))
        
    three_bush = []
    for i in range(num):
        if i != num - 1 and i != 0:
            three_bush.append(berry[i - 1] + berry[i] + berry[i + 1])
        elif i == num - 1:
            three_bush.append(berry[i - 1] + berry[i] + berry[0])
        elif i == 0:
            three_bush.append(berry[i] + berry[i + 1] + berry[num - 1])
    max_berry = three_bush[0] # можно воспользовать методом max(three_bush)
    for i in three_bush:
        if max_berry < i:
            max_berry = i
    return max_berry

print(max_berry_three_bush(int(input("Введите колиство кустов: "))))