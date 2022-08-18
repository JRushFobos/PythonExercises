from random import randint

def game ():
    print ('Welcome to my game "Guess the number"')
    print ('I guessed a number from 1 to 10')
    answer = randint(1,10)
    print('Guess the answer, please')
    guess = 0
    while guess != answer:
        guess = int(input('Try to guess, enter the number'))
        if answer  > guess:
            print ('more, try again')
        elif answer < guess:
            print ('less, try again')
        elif answer == guess:
            print ('Your guess, Great')
    
game()