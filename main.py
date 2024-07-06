"""Бейглз (Быки и коровы)
    Дедуктивная логическая игра на угадывание числа по подсказкам.
    Нужно угадать число, Бык - одно число корректно и на правильном месте
    Корова - одно число корректно, но место неверно"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Быки и коровы, дедуктивно - логическая игра.

    Я загадал число из {} не повторяющихся цифр.
    Попробуй его угадать. Вот тебе подсказки:
    Когда я говорю : Это означает:
    Бык - правильное число на правильном месте
    Корова - правильное число на неправильном месте
   
    Например, если мое число 248, а ты предполагаешь 843, то
    моим ответом будет 1 бык, 1 корова.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()
        print('Я загадал число.')
        print('У тебя есть {} попыток, чтобы его отгадать.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка № {}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('Попытки закончились.')
                print('Правильный ответ был {}.'.format(secretNum))
        print('Хотите сыграть еще? (да или нет)')
        if not input('> ').lower().startswith('д'):
            break
    print('Спасибо за игру!')


def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""
    if guess == secretNum:
        return 'Правильно!'

    clues = []
    bull_word = ""
    cow_word = ""
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Бык')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Корова')
    if len(clues) == 0:
        return 'Ни быков, ни коров'
    else:
        bulls = clues.count("Бык")
        cows = clues.count("Корова")
        if bulls == 2 or bulls == 3 or bulls == 4:
            bull_word = "быка"
        elif bulls == 1:
            bull_word = "бык"
        else:
            bull_word = "быков"
        if cows == 2 or cows == 3 or cows == 4:
            cow_word = "коровы"
        elif cows == 1:
            cow_word = "корова"
        else:
            cow_word = "коров"
        return f"{bulls} {bull_word}, {cows} {cow_word}."



if __name__ == '__main__':
    main()


