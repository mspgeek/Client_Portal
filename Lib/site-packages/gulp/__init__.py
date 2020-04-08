# -*- coding: utf-8 -*-

from functools import wraps
import logging
import time as t

__author__ = 'Cahyo Primawidodo'
__email__ = 'cahyo.p@gmail.com'
__version__ = '0.1.0'


def debug_log(lvl=logging.DEBUG, logger_name=None):

    def enable(f):
        logger = logging.getLogger(logger_name)

        @wraps(f)
        def wrapper(*args, **kwargs):
            init = logger.getEffectiveLevel()
            logger.setLevel(lvl)
            print('\n# function: {}'.format(f.__name__))
            y = f(*args, **kwargs)
            logger.setLevel(init)
            return y
        return wrapper
    return enable


def time_this(fmt, multiplier=1, **print_kwargs):
    def enable(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_t = t.time()
            y = f(*args, **kwargs)
            end_t = t.time()
            print('\n# function: {}'.format(f.__name__))
            print(fmt.format(multiplier * (end_t-start_t)), **print_kwargs)
            return y
        return wrapper
    return enable


def peek_vars():
    def enable(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            y = f(*args, **kwargs)
            print('\n# function: {}'.format(f.__name__))
            print('args: {}'.format(str(args)))
            print('kwargs: {}'.format(str(kwargs)))
            print('return: {}'.format(str(y)))
            return y
        return wrapper
    return enable
