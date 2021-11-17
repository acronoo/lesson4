"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
"""

from sys import argv
from itertools import cycle
from itertools import count
""" 
Задание А. Для выполнения скрипта необходимо перед запуском указать в стартовых параметрах 2 значения. 
Первое - стартовое число с которого будет генерироваться числа
Второе - число до которого будет генерироваться числа
"""
script_name, start_numb, end_numb = argv
numb_list = []
for element in count(int(start_numb)):
    if int(element) > int(end_numb):
        break
    numb_list.append(element * 7)
print(numb_list)

"""
Задание Б.
"""
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = 0  # Номер итерации
for num in cycle(some_list):
    if i > 13:  # Цикл завершится после 14 итераций
        break
    print(num)
    i += 1
