import locale


__author__ = 'ChyrosNX'


MULTIPLY_BY_X_DIGITS = 8
A_1000_DIGIT_TEXT = \
    '73167176531330624919225119674426574742355349194934' \
    + '96983520312774506326239578318016984801869478851843' \
    + '85861560789112949495459501737958331952853208805511' \
    + '12540698747158523863050715693290963295227443043557' \
    + '66896648950445244523161731856403098711121722383113' \
    + '62229893423380308135336276614282806444486645238749' \
    + '30358907296290491560440772390713810515859307960866' \
    + '70172427121883998797908792274921901699720888093776' \
    + '65727333001053367881220235421809751254540594752243' \
    + '52584907711670556013604839586446706324415722155397' \
    + '53697817977846174064955149290862569321978468622482' \
    + '83972241375657056057490261407972968652414535100474' \
    + '82166370484403199890008895243450658541227588666881' \
    + '16427171479924442928230863465674813919123162824586' \
    + '17866458359124566529476545682848912883142607690042' \
    + '24219022671055626321111109370544217506941658960408' \
    + '07198403850962455444362981230987879927244284909188' \
    + '84580156166097919133875499200524063689912560717606' \
    + '05886116467109405077541002256983155200055935729725' \
    + '71636269561882670428252483600823257530420752963450'


def main():
    locale.setlocale(locale.LC_ALL, 'US')
    solve()


def solve():
    highest_product = 0
    max_product_length = len(num_fmt(9 ** MULTIPLY_BY_X_DIGITS))

    for idx in range(0, len(A_1000_DIGIT_TEXT) - MULTIPLY_BY_X_DIGITS):
        numbers = list(int(t) for t in A_1000_DIGIT_TEXT[idx:idx + MULTIPLY_BY_X_DIGITS])
        product = multiply_recursively(*numbers)
        highest_product = max(highest_product, product)

        print('  {} = {}'.format('*'.join(str(n) for n in numbers), num_fmt(product).rjust(max_product_length)))

    print('\nHighest product is {}'.format(num_fmt(highest_product)))


def multiply_recursively(*numbers):
    """
    Multiply any number of given numbers using recursive technique
    :param numbers: Numbers that will be multiplied
    :return: Product of all given numbers
    """
    if len(numbers) > 1:
        return multiply_recursively(*tuple([numbers[0] * numbers[1]]) + numbers[2:])
    else:
        return numbers[0]


def num_fmt(num):
    return locale.format('%d', num, grouping=True)


main()
