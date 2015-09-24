import time


INITIAL_DIVIDEND = 1
DIVISORS = list(range(1, 20 + 1))


def is_divisible_by_divisors(dividend, divisors):
    for d in divisors:
        if dividend % d != 0:
            return False

    return True


start_timestamp = int(round(time.time() * 1000))
while not is_divisible_by_divisors(INITIAL_DIVIDEND, DIVISORS):
    INITIAL_DIVIDEND += 1
elapsed_time = int(round(time.time() * 1000)) - start_timestamp

print(
    '{} is the smallest number that can be divided by each of the numbers from {} to {} without any remainder.'
    .format(INITIAL_DIVIDEND, DIVISORS[:1][0], DIVISORS[-1:][0])
      )

print('\nIt took {} millis to find the answer.'.format(elapsed_time))
