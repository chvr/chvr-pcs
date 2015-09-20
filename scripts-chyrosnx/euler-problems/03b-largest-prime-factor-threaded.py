import logging
import os
from queue import Queue, Full
from threading import Thread
import time
#from Scripts.chyros.template.chyros import loggingutil
from chyros import loggingutil


__author__ = 'ChyrosNX'

PROBLEM_NO = 3
TITLE = 'Largest Prime Factor (Threaded)'

DEBUG_MODE = True
LOGGING_MODE = logging.DEBUG

DEFAULT_USER_INPUT = 600851475143  # 13195, 600851475143
ASK_FOR_USER_INPUT = True
RESULT_QUEUE_SIZE = 100
DIVISORS_PER_TASK = 5000000    # Divide operations per thread
CONCURRENT_THREADS_LIMIT = -1  # Use 0 or -1 for no limit

tasks = {}
prime_factors_queue = Queue(RESULT_QUEUE_SIZE)
start_timestamp = int(time.time() * 1000)


def solve(num):
    logging.info('Getting prime factors for number {}...'.format(num))

    create_divisor_tasks(num)

    while len(tasks) > 0:
        time.sleep(0.01)

    show_highest_prime_factor(num)


def create_divisor_tasks(num):
    """
    Create and distribute divisors per task.
    :param num: The given number for this problem.
    """

    task_id = 0
    min_divisor_range = 2
    max_divisor_range = int(num / 2)
    current_range_from = 0

    while current_range_from <= max_divisor_range:
        arg_divisor_range_from = current_range_from + min_divisor_range
        arg_divisor_range_to = arg_divisor_range_from + DIVISORS_PER_TASK
        if arg_divisor_range_to > max_divisor_range:
            arg_divisor_range_to = max_divisor_range

        while 1 < CONCURRENT_THREADS_LIMIT <= len(tasks):
            time.sleep(0.01)

        new_task = Thread(
            target=task_find_possible_prime_factors
            , args=(task_id, num, arg_divisor_range_from, arg_divisor_range_to)
        )

        tasks[task_id] = new_task
        new_task.start()

        if LOGGING_MODE == logging.DEBUG:
            logging.debug(
                'Active tasks: {} | Task {} ({}-{}) started.'
                .format(len(tasks), task_id, arg_divisor_range_from, arg_divisor_range_to)
            )

        current_range_from += DIVISORS_PER_TASK
        task_id += 1


def task_find_possible_prime_factors(task_id, dividend, divisor_range_from, divisor_range_to):
    """
    Divide a given dividend number with a specified range of divisors. If a dividend is divisible by a divisor,
    the divisor will then be processed to check if its a prime factor. Prime factor results will be saved to a
    queue.
    :param task_id: Task ID. Required for removing task from the list upon completion.
    :param dividend: Number the will be checked for divisibility.
    :param divisor_range_from: Starting range of divisors
    :param divisor_range_to: Ending range for divisors
    """

    start_timestamp_task = int(time.time() * 1000)

    for divisor in range(divisor_range_from, divisor_range_to):
        # Division operation with Float.is_integer() is used over modulus operation for performance reasons.
        # Modulus operation is significantly slower specially when used repeatedly.
        if (dividend / divisor).is_integer():
            if divisor >= 10086647:
                elapsed_time = int(time.time() * 1000) - start_timestamp
                logging.info('  - checking if {} is a prime number... (Total Elapsed Time: {} ms)'.format(divisor, elapsed_time))

            start_timestamp_ipn_task = int(time.time() * 1000)
            is_divisor_a_prime_number = is_prime_number(divisor)

            if LOGGING_MODE == logging.DEBUG:
                elapsed_time = int(time.time() * 1000) - start_timestamp_ipn_task
                logging.debug('is_prime_number({}) task completed. (Elapsed time: {} ms)'.format(divisor, elapsed_time))

            if is_divisor_a_prime_number:
                logging.info('{} is a prime factor of {}.'.format(divisor, dividend))
                try:
                    prime_factors_queue.put_nowait(divisor)
                except Full:
                    logging.warning('prime_factors_queue is full! Unable to add Prime Factor {}.'.format(divisor))

    if LOGGING_MODE == logging.DEBUG:
        elapsed_time = int(time.time() * 1000) - start_timestamp_task
        logging.debug(
            'Active tasks: {} | Task {} ({}-{}) completed. (Elapsed time: {} ms)'
            .format(len(tasks), task_id, divisor_range_from, divisor_range_to, elapsed_time)
        )

    # Remove task from the list
    try:
        tasks.pop(task_id)
    except KeyError:
        logging.warning('Task ID {} not found! Task won\'t be removed from the list.')


def is_prime_number(num):
    """
    A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and
    itself.
    :param num: A number that will be check as a prime number.
    :return: True if a given number is a prime number. Otherwise, False.
    """

    if num <= 1:
        return False

    for divisor in range(2, int(num / 2) + 1):
        # Division operation with Float.is_integer() is used over modulus operation for performance reasons.
        # Modulus operation is significantly slower specially when used repeatedly.
        if (num / divisor).is_integer():
            return False

    return True


def show_highest_prime_factor(num):
    """
    Shows the highest prime factor from the queue.
    :param num: The given number for this problem.
    """

    max_prime_factor = 0
    prime_factors = []

    while not prime_factors_queue.empty():
        prime_factors.append(prime_factors_queue.get())

    for prime_factor in prime_factors:
        if prime_factor > max_prime_factor:
            max_prime_factor = prime_factor

    logging.info('ANSWER: The largest prime factor of the number {} is {}.'.format(num, max_prime_factor))


def setup_logging():
    log_file = '{}.log'.format(os.path.splitext(os.path.basename(__file__))[0])
    loggingutil.create(log_file, log_level=LOGGING_MODE)


def display_title():
    """
    Displays this problem's title information. Nothing special, really.
    """
    text_title = 'Problem #{} - {}'.format(str(PROBLEM_NO).zfill(2), TITLE)
    text_dashes = ''.rjust(len(text_title), '-')
    text_full_title = '{}\n{}\n{}\n'.format(text_dashes, text_title, text_dashes)

    print(text_full_title)
    logging.info(text_dashes)
    logging.info(text_title)
    logging.info(text_dashes)


def ask_for_whole_number(default_num=DEFAULT_USER_INPUT):
    """
    Ask for user input and validate if it is a whole number. If the given value is invalid, a default value will be
    used instead.
    :param default_num: Default number that will be used if user input has been invalidated.
    :return: Whole number.
    """

    if not ASK_FOR_USER_INPUT:
        return DEFAULT_USER_INPUT

    num = None
    try:
        num = input('- Give a whole number(default: {}): '.format(default_num)) or default_num
        num = int(num)
    except ValueError:
        logging.warning(
            'NOTE: \'{}\' is not a whole number. Default value of {} will be used.'
            .format(num, default_num)
        )
        num = default_num

    return num


def main():
    setup_logging()
    display_title()
    num = ask_for_whole_number()
    solve(num)


main()
