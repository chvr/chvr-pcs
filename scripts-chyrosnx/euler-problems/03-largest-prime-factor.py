import time


__author__ = 'ChyrosNX'

PROBLEM_NO = 3
TITLE = 'Largest Prime Factor'


start = int(time.time() * 1000)


def solve(num):
    _max = 0

    for i in range(2, int(num / 2) + 1):
        if num % i != 0:
            continue

        if i >= 10086647:
            elapsed_time = int(time.time() * 1000) - start
            print('  - checking if {} is a prime number... (Elapsed Time: {} millis)'.format(i, elapsed_time))

        if is_prime_number(i):
            _max = i
            print('{} is a prime factor of {}.'.format(i, num))

    print('\nANSWER: The largest prime factor of the number {} is {}.'.format(str(num), str(_max)))


def is_prime_number(n):
    if n <= 1:
        return False

    for divisor in range(2, int(n / 2) + 1):
        if n % divisor == 0:
            return False

    return True


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
    default_num = 13195

    display_title()
    num = ask_for_whole_number(default_num)
    print()
    solve(num)


main()
