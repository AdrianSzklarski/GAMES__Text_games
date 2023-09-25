'''Main finction of Guess the number 2
   @AdrianSzklarski, 09.2023'''

from files.Guess_the_number2_number import Data


class Guess:
    def __init__(self):
        self.minNo = 0
        self.maxNo = 2000
        self.initial_value = (self.maxNo - self.minNo) // 2 + self.minNo
        print(f'My number is? {self.initial_value}')
        self.max = self.initial_value
        self.choose = Data().get_start()

    def get_loop(self):
        '''Guessing values'''
        while self.choose != 'w':
            initial_value = (self.max - self.minNo) // 2 + self.minNo
            print(f'My number is? {initial_value}')
            self.choose = Data().get_choose()
            if self.choose == 'b':
                self.max = initial_value
            elif self.choose == 's':
                self.minNo = initial_value
        self.choose = ''
        print('You Win! :)')
        return self.choose

    def __str__(self):
        return f'{self.get_loop()}'
