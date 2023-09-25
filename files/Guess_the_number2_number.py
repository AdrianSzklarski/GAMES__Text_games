'''Downloading data'''


class Data:
    '''Return proper value provided by user
    :rtype: str
    :return: value provided bu user as
    ["s", "b", "w"] where:
    "s" is too samll
    "b" is too big
    "w" is you won'''

    def __init__(self):
        print(f'Provide a choice: ["s", "b", "w"] where: "s" is too small  "b" is too big  "w" is you won: ', end=' ')
        value = input().lower()
        self.answer_is = value

    def get_choose(self):
        '''Determination of selection'''
        choose = ["s", "b", "w"]
        while True:
            if self.answer_is in choose:
                return self.answer_is
            else:
                print("Input is not in your choose")
                exit(1)

    def get_start(self):
        return self.get_choose()

    def __str__(self):
        return f'{self.get_choose()}'

