__author__ = 'ChyrosNX'

PROBLEM_NO = 1
TITLE = 'Multiples of 3 and 5'


def solve(num):
    _sum = 0
    multiples_of_3_and_5 = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            multiples_of_3_and_5.append(i)
            _sum += i

    print('\nAll natural numbers below {} that are multiples of 3 and 5 are: {}.'.format(
        num
        , ', '.join(str(m) for m in multiples_of_3_and_5)
    ))
    print('\nANSWER: Sum of all multiples of 3 and 5 below {} is {}.'.format(str(num), str(_sum)))


def display_title():
    text_title = 'Problem #{} - {}'.format(str(PROBLEM_NO).zfill(2), TITLE)
    text_dashes = ''.rjust(len(text_title), '-')
    text_full_title = '{}\n{}\n{}\n'.format(text_dashes, text_title, text_dashes)

    print(text_full_title)


def ask_for_whole_number(default_num):
    """Ask for a whole number from user and validate as whole number. If the given value is invalid, a default value
    will be used instead"""

    num = None
    try:
        num = input('- Give a whole number(default: {}): '.format(default_num)) or default_num
        num = int(num)
    except ValueError:
        print('NOTE: \'{}\' is not a whole number. Default value of {} will be used.'.format(str(num), str(default_num)))
        num = default_num

    return num


def main():
    default_num = 10

    display_title()
    num = ask_for_whole_number(default_num)
    solve(num)


main()
