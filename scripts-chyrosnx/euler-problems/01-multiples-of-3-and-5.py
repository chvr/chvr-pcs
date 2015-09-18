__author__ = 'ChyrosNX'

PROBLEM_NO = 1
TITLE = 'Multiples of 3 and 5'


def solve(num):
    _sum = 0

    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            _sum += i

    print('\nANSWER: Sum of all multiples of 3 and 5 below {} is {}.'.format(str(num), str(_sum)))


def display_title():
    text_title = 'Problem #{} - {}'.format(str(PROBLEM_NO).zfill(2), TITLE)
    text_dashes = ''.rjust(len(text_title), '-')
    text_full_title = '{}\n{}\n{}\n'.format(text_dashes, text_title, text_dashes)

    print(text_full_title)


def ask_for_whole_number(default_num=10):
    """Ask for a whole number from user and validate as whole number. If the given value is invalid, a default value
    will be used instead"""

    num = None
    try:
        num = input('- Give a whole number: ')
        num = int(num)
    except ValueError:
        print('\'{}\' is not a whole number. Default value of {} will be used.'.format(str(num), str(default_num)))
        num = default_num

    return num


def main():
    display_title()
    num = ask_for_whole_number()
    solve(num)


main()
