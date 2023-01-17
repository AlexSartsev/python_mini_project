# Угадайка слов

import random
word_lst = ['лето', 'чай', 'кофе', 'стена', 'ковер', 'стол', 'мышь', 'кот', 'ложь', 'лампа', 'дробь', 'пуля', 'нож', 'слово', 'аист', 'плед', 'тюль', 'цвет', 'окно', 'гора', 'холм', 'куль', 'снег']

def get_word(words):
    return word_lst[random.randint(0, len(word_lst))].upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print('Давай играть в угадайку слов!')
    word_completion = '_' * len(word)
    guessed_letters = []  # список угаданных букв
    guessed_words = []  # список угаданных слов
    tries = 6  # количество попыток
    while True:
      print(display_hangman(tries))
      print(word_completion)
      letter = input('Введите букву или слово целиком: ').upper()
      
      if letter.isalpha() == True:
         if letter in guessed_letters:
            print('Эта буква уже была, попробуй другую')

         elif letter in word:
            for i in range(len(word)):
               if word[i] == letter:
                  word_completion = word_completion[:i] + letter + word_completion[i + 1:]
            guessed_letters.append(letter)

         elif tries == 0:
            print(f'Мне жаль вы проиграли, слово: {word.capitalize()}')
            break            

         else:
            tries -= 1
            print('К сожалению нет такой буквы, попробуй другую')
            guessed_letters.append(letter)
            continue
            return tries

      else:
         print('Слово содержит только русские буквы верхнего и нижнего регистра')

      if word_completion == word or letter == word:
         print(f'Поздравляем вы угадали слово: {word.capitalize()}')
         break

random_word = get_word(word_lst)
play(random_word)