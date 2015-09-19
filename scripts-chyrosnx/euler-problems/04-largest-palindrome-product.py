import math

__author__ = 'ChyrosNX'

PROBLEM_NO = 4
TITLE = 'Largest Palindrome Product'


def solve(num):
    min_num = int(math.pow(10, num - 1))
    max_num = int(math.pow(10, num) - 1)
    largest_palindrome = 0

    for i in range(min_num, max_num + 1):
        for j in range(i, max_num + 1):
            product = i * j
            #if str(product) == reverse_text_manually(product):
            if str(product) == str(product)[::-1]:
                print('{} * {} = {}'.format(i, j, str(product).rjust(len(str(max_num * max_num)))))
                if product > largest_palindrome:
                    largest_palindrome = product

    print('\nANSWER: The largest palindrome made from the product of two {}-digit numbers is {}.'.format(str(num), str(largest_palindrome)))


def reverse_text_manually(text):
    """Basically the same as text[::-1], only slower."""
    text = str(text)
    reversed_text = str()

    for i in reversed(range(0, len(text))):
        reversed_text += text[i]

    return reversed_text


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
    default_num = 2

    display_title()
    num = ask_for_whole_number(default_num)
    print()
    solve(num)


main()
