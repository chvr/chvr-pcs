__author__ = 'ChyrosNX'

PROBLEM_NO = 2
TITLE = 'Even Fibonacci Numbers'


def solve():
    term_limit = 4000000
    sequence = 0
    term = 0
    _sum = 0

    while term < term_limit:
        print('fibonacci({}) = {}'.format(str(sequence).rjust(2), str(term).rjust(len(str(term_limit)))))

        if term % 2 == 0:
            _sum += term

        sequence += 1
        term = fibonacci(sequence)

    print('\nANSWER: Sum of even-valued terms is {}.'.format(str(_sum)))


def fibonacci(n):
    """Compute fibonacci recursively where n is a sequence number."""
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def display_title():
    text_title = 'Problem #{} - {}'.format(str(PROBLEM_NO).zfill(2), TITLE)
    text_dashes = ''.rjust(len(text_title), '-')
    text_full_title = '{}\n{}\n{}\n'.format(text_dashes, text_title, text_dashes)

    print(text_full_title)


def main():
    display_title()
    solve()


main()
