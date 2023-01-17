# Шифр Цезаря

language = input('Выберите язык, а - английский, р - русский: ')
left_or_right = input('Выберите сдвиг, л - влево, в - вправо: ')
num = int(input("Введите N: "))
string = input('Введите текст: ')

# Английский текст со сдвигом в лево
def english_left(text, num):
    chifr = ''
    for i in range(len(text)):
        if 64 < ord(text[i]) < 91:
            code = ord(text[i]) - num
            if code < 65:
                code = 90 - (64 - code)
            chifr += chr(code)
        elif 96 < ord(text[i]) < 123:
            code = ord(text[i]) - num
            if code < 97:
                code = 122 - (96 - code)
            chifr += chr(code)
        else:
            chifr += text[i]
    return chifr

# Английский текст со сдвигом в право
def english_right(text, num):
    chifr = ''
    for i in range(len(text)):
        if 64 < ord(text[i]) < 91:
            code = ord(text[i]) + num
            if code > 90:
                code = (code - 90) + 64
            chifr += chr(code)
        elif 96 < ord(text[i]) < 123:
            code = ord(text[i]) + num
            if code > 122:
                code = (code - 122) + 96
            chifr += chr(code)
        else:
            chifr += text[i]
    return chifr

# Русский текст со сдвигом в лево
def russian_left(text, num):
    chifr = ''
    for i in range(len(text)):
        if 1039 < ord(text[i]) < 1072:
            code = ord(text[i]) - num
            if code < 1040:
                code = 1071 - (1039 - code)
            chifr += chr(code)
        elif 1071 < ord(text[i]) < 1104:
            code = ord(text[i]) - num
            if code < 1072:
                code = 1103 - (1071 - code)
            chifr += chr(code)
        else:
            chifr += text[i]
    return chifr

# Русский текст со сдвигом в право
def russian_right(text, num):
    chifr = ''
    for i in range(len(text)):
        if 1039 < ord(text[i]) < 1072:
            code = ord(text[i]) + num
            if code > 1072:
                code = (code - 1071) + 1039
            chifr += chr(code)
        elif 1071 < ord(text[i]) < 1104:
            code = ord(text[i]) + num
            if code > 1103:
                code = (code - 1103) + 1071
            chifr += chr(code)
        else:
            chifr += text[i]
    return chifr

if language == 'а':
    if left_or_right == 'п':
        print(english_right(string, num))
    else:
        print(english_left(string, num))
else:
    if left_or_right == 'л':
        print(russian_left(string, num))
    else:
        print(russian_right(string, num))