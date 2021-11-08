import random

from os import system


class Jokenpo:
    def __init__(self):
        list = ['1', '2', '3']

        choice = random.choice(list)

        print('''
        ===============================================
                            Jokenpô                    
        ===============================================
            Chose your weapon:
            [1] Rock
            [2] Paper
            [3] Scissor
        ''')

        i = 0
        while i == 0:
            entry = input('Your choice: ')

            if entry in list:
                if entry == choice:
                    return 'Draw'
                    
                elif entry == '1':
                    if choice == '2':
                        return 'You lose.'
                        
                    elif choice == '3':
                        return 'You win!'

                elif entry == '2':
                    if choice == '3':
                        return 'You lose.'

                    elif choice == '1':
                        return 'You win!'

                elif entry == '3':
                    if choice == '1':
                        return 'You lose.'

                    elif choice == '2':
                        return 'You win!'


def main():
    n = 0
    while n == 0:
        system('cls')

        response = Jokenpo()

        print(response)

        again = input('Play again?(y/n): ')

        if again != 'y':
            n += 1


if __name__ == '__main__':
    main()

