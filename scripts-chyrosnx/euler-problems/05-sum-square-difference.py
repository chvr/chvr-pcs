# https://repl.it/BKWZ
# Problem #6: Sum square difference by ChyrosNX (https://projecteuler.net/problem=6)

from functools import reduce

__author__ = 'ChyrosNX'


def solve_normally():
    _sum = 0
    sum_of_squares = 0

    for n in range(1, 10 + 1):
        _sum += n
        sum_of_squares += n ** 2

    square_of_sum = _sum ** 2

    return sum_of_squares, square_of_sum


def solve_using_lambda():
    sum_of_squares = reduce(lambda n1, n2: n1 + n2, map(lambda n: n * n, list(range(1, 10 + 1))))
    square_of_sum = reduce(lambda n1, n2: n1 + n2, list(range(1, 10 + 1))) ** 2

    return sum_of_squares, square_of_sum


def solve_using_list_comprehension():
    sum_of_squares = sum([n * n for n in list(range(1, 10 + 1))])
    square_of_sum = sum(list(range(1, 10 + 1))) ** 2

    return sum_of_squares, square_of_sum


def show_output(caption, sum_of_squares, square_of_sum):
    difference = square_of_sum - sum_of_squares
    output = '\n({}) The difference between the sum of the squares of the'.format(caption) \
        + 'first ten natural numbers and the square of the sum is:' \
        + '\n\t{} - {} = {}'.format(sum_of_squares, square_of_sum, difference)

    print(output)


# Solve Normally
show_output('NORMAL', *solve_normally())

# Solve Using Lambda (http://www.secnetix.de/olli/Python/lambda_functions.hawk)
show_output('LAMBDA', *solve_using_lambda())

# Solve Using List Comprehension (http://www.python-course.eu/list_comprehension.php)
show_output('LIST_COMPREHENSION', *solve_using_list_comprehension())
