'''Main fuction for our program
   @AdrianSzklarski, 09.2023'''

from files.Guess_the_number2_Gtn import Guess
import os, sys

if __name__ == '__main__':
    while True:
        print('What is your number? scope<0, 1000> > ', end=' ')
        no = input()
        if 0 <= int(no) <= 1000:
            print(f'Your number is {no} so:... ')
            guess = Guess()
            print(guess)
            print('\nIf you want to play again press "a", as you want to press any other button.')
            play = input()
            if play == 'a'.lower():
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                break
        else:
            print('Your value is out of range, try again: ')
