import datetime
from functools import wraps


def logger(path_to_logfile):
    def _logger(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start_event = f'{datetime.datetime.now()} - Вызвана функция {fn.__name__} c аргументами: {str(args)}, {str(kwargs)}'
            write_to_file(start_event + '\n', 'decorators.log')

            result = fn(*args, **kwargs)

            end_event = f'{datetime.datetime.now()} - Функция {fn.__name__} вернула результат: {result}'
            write_to_file(end_event + '\n', path_to_logfile)

            return result

        return wrapper

    return _logger


def write_to_file(text, path_to_file):
    with open(path_to_file, 'a', encoding='utf-8') as f:
        f.write(text)
