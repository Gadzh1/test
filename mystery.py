TRICK_ANSWER = 'троллейбус'


def mystery():
    answer = input('Что это такое: синий, большой, с усами и полностью набит зайцами?\n').lower()

    for i in range(2):
        if answer == 'cдаюсь':
            print('Правильный ответ: троллейбус.')
            return

        if answer == TRICK_ANSWER:
            print('Правильно!')
            return
        else:
            print('Подумай еще.')
            answer = input()

    print('Правильный ответ: троллейбус.')


mystery()
