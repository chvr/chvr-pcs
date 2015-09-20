import logging
import os
from queue import Queue
from threading import Thread
import time
#from Scripts.chyros.template.chyros import loggingutil
from chyros import loggingutil

__author__ = 'ChyrosNX'

PROBLEM_NO = 3
TITLE = 'Largest Prime Factor (Threaded)'


_debug_mode = True
threads = {}
thread_name = 0
result_queue = Queue()
start = int(time.time() * 1000)
max_prime_factor = 0
task_completed = False


def get_divisibles(name, num, from_divisible_by, to_divisible_by):
    lifetime_start = int(time.time() * 1000)

    for i in range(from_divisible_by, to_divisible_by):
        if (num / i).is_integer():
            result_queue.put(i)

    if _debug_mode:
        elapsed_time = int(time.time() * 1000) - lifetime_start
        logging.debug('Threads: {} | {} -> {} completed (Elapsed time: {} ms)'.format(len(threads), from_divisible_by, to_divisible_by, elapsed_time))

    threads.pop(name)


def check_for_prime_number(num):
    global max_prime_factor

    while not task_completed or not result_queue.empty():
        while not result_queue.empty():
            divisible = result_queue.get()

            if divisible >= 10086647:
                elapsed_time = int(time.time() * 1000) - start
                logging.info('  - checking if {} is a prime number... (Elapsed Time: {} millis)'.format(divisible, elapsed_time))

            if is_prime_number(divisible):
                if divisible > max_prime_factor:
                    max_prime_factor = divisible

                logging.info('{} is a prime factor of {}.'.format(divisible, str(num)))

        time.sleep(0.02)

    logging.info('ANSWER: The largest prime factor of the number {} is {}.'.format(str(num), str(max_prime_factor)))


def solve(num):
    global task_completed, thread_name

    Thread(target=check_for_prime_number, args={num}).start()

    batch_per_thread = 5000000
    thread_limit = 999999999

    from_range = 2
    to_range = num + 1
    max_range = int(num / 2)

    idx = 0
    while idx < to_range:
        arg_from_divisible_by = idx + from_range
        arg_to_divisible_by = arg_from_divisible_by + batch_per_thread
        if arg_to_divisible_by > max_range:
            arg_to_divisible_by = max_range

        idx += batch_per_thread

        while len(threads) >= thread_limit:
            time.sleep(0.02)

        t = Thread(target=get_divisibles, args=(thread_name, num, arg_from_divisible_by, arg_to_divisible_by))
        threads[thread_name] = t
        t.start()

        if _debug_mode:
            logging.debug('Threads: {} | New thread created.'.format(len(threads)))

        thread_name += 1

    for t in threads:
        t.join()

    task_completed = True


def is_prime_number(n):
    if n <= 1:
        return False

    for divisor in range(2, int(n / 2) + 1):
        if (n / divisor).is_integer():
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
        logging.warning('NOTE: \'{}\' is not a whole number. Default value of {} will be used.'.format(str(num), str(default_num)))
        num = default_num

    return num


def main():
    log_file = '{}.log'.format(os.path.splitext(os.path.basename(__file__))[0])
    loggingutil.create(log_file, log_level=logging.DEBUG)

    default_num = 13195

    display_title()
    #num = ask_for_whole_number(default_num)
    num = 600851475143
    solve(num)


main()
