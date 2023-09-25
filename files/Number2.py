'''Downloading data'''


class Data:
    '''Return proper value provided by user
    :rtype: str
    :return: value provided bu user as
    ["s", "b", "w"] where:
    "s" is too samll
    "b" is too big
    "w" is you won'''

    def __init__(self, value):
        self.answer_is = value

    def get_choose(self):
        choose = ["s", "b", "w"]
        while True:
            if self.answer_is in choose:
                break
            else:
                print("Input is not in your choose")
                exit(1)
        return choose

    def __str__(self):
        return f'{self.get_choose()}'


if __name__ == '__main__':
    print(f'Provide a choice: ["s", "b", "w"] where: "s" is too samll  "b" is too big  "w" is you won: ', end=' ')
    value = input().lower()
    data = Data(value)
    print(data)
