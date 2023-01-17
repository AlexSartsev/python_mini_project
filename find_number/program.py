# Числовая угадайка
import random
num_rand = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
    if 1 < num <= 100:
        return True
    else:
        return False

while True:
    number = int(input('Введите число от 1 до 100: '))
    if is_valid(number) == True:
        if number < num_rand:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif number > num_rand:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

is_valid(number)