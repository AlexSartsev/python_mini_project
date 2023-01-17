# Генератор безопасных паролей
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

length_password = int(input('Длина пароля: '))
ques_digits = input('Включать цифры? д - да, н - нет: ')
ques_upper = input('Включать ли прописные буквы? д - да, н - нет: ')
ques_lower = input('Влючать строчные буквы? д - да, н - нет: ')
ques_sybmols = input('Включать символы? д - да, н - нет: ')
ques = input('Исключать ли неодназначные символы? д - да, н - нет: ')

if ques_digits == 'д':
    chars += digits
if ques_upper == 'д':
    chars += uppercase_letters
if ques_lower == 'д':
    chars += lowercase_letters
if ques_sybmols == 'д':
    chars += punctuation

def generate_password(chars, length_password):
    password = ''
    for i in range(length_password):
        password += chars[random.randint(0, len(chars))]
    return password

print(generate_password(chars, length_password))