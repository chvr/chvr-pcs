__version__ = '1.01 by ChyrosNX'


class MultiplesOfThreeAndFive(object):

    PROBLEM_NO = 1
    TITLE = 'Multiples of 3 and 5'

    def __init__(self):
        self.sum = 0

    def solve(self, num):
        self.sum = 0

        multiples_of_3_and_5 = []
        for i in range(1, num):
            if self.is_multiples_of_3_or_5(i):
                multiples_of_3_and_5.append(i)
                self.sum += i

        print('\nAll natural numbers below {} that are multiples of 3 and 5 are: {}.'.format(
            num
            , ', '.join(str(m) for m in multiples_of_3_and_5)
        ))
        print('\nANSWER: Sum of all multiples of 3 and 5 below {} is {}.'.format(str(num), str(self.sum)))

    def is_multiples_of_3_or_5(self, num):
        return num % 3 == 0 or num % 5 == 0

    def parse_num(self, num, default_num):
        """Validate as whole number. If the given value is invalid, a default value
        will be used instead"""

        try:
            num = int(num)
        except ValueError:
            print('NOTE: \'{}\' is not a whole number. Default value of {} will be used.'.format(str(num), str(default_num)))
            num = default_num

        return num

    def display_title(self):
        text_title = 'Problem #{} - {}'.format(str(self.PROBLEM_NO).zfill(2), self.TITLE)
        text_dashes = ''.rjust(len(text_title), '-')
        text_full_title = '{}\n{}\n{}\n'.format(text_dashes, text_title, text_dashes)

        print(text_full_title)


def main():
    default_num = 10

    mtf = MultiplesOfThreeAndFive()
    mtf.display_title()
    num = input('- Give a whole number(default: {}): '.format(default_num)) or default_num
    num = mtf.parse_num(num, default_num)
    mtf.solve(num)


if __name__ == '__main__':
    main()
