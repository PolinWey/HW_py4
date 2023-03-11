'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше 
заданного минимума и не больше заданного максимума)'''

import random
count=int(input("Введите количество элементов: "))
list_input=[random.randint(-5,20) for i in range(count)]
print(list_input)

def find_index(list_in):
    list_index=[]
    start_value=int(input("Ищем числа от: "))
    end_value=int(input("... до: "))
    for i in range(start_value,end_value):
        for j in range(len(list_in)):
            if list_in[j]==i:
                list_index.append(j)
    print(list_index)

find_index(list_input)