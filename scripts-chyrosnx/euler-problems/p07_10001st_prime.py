__author__ = 'ChyrosNX'


def is_prime_number(n):
    if n < 2:
        return False

    for divisor in range(2, int(n / 2) + 1):
            if (n / divisor).is_integer():
                return False

    return True


num = 2
count = 0

while count < 10001:
    if is_prime_number(num):
        print('{} is a prime number.'.format(num))
        count += 1

    num += 1

print('\n{} is the 10001st prime number.'.format(num))
