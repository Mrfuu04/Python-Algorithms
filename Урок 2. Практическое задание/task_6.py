"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""

from random import randint

rand_num = randint(0, 100)


def func(cnt=10):
    player_num = int(input('Число '))
    if cnt == 0:
        print(f'Вы проиграли\nЧисло {rand_num}')
        return
    if player_num == rand_num:
        print(f'Вы победили!\nЧисло {rand_num}')
    else:
        print(f'Попыток: {cnt}')
        if player_num < rand_num:
            print('Загаданное число больше')
        else:
            print('Загаданное число меньше')
        func(cnt - 1)


func()
