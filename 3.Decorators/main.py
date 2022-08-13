import datetime
from functools import wraps
from zodiac_signs import zodiac_signs


# код текущего дз
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


# код из дз 2.conditions
@logger(path_to_logfile='decorators.log')
def check_date(day, month):
    months = {
        'январь': 31,
        'февраль': 28,
        'март': 31,
        'апрель': 30,
        'май': 31,
        'июнь': 30,
        'июль': 31,
        'август': 30,
        'сентябрь': 31,
        'октябрь': 30,
        'ноябрь': 31,
        'декабрь': 30
    }

    if month in months:
        if (day > 0) and (day <= months[month]):
            return True

    return False

@logger(path_to_logfile='decorators.log')
def main():
    try:
        month = input('Введите месяц: ').lower()
        day = int(input('Введите день: '))

        if check_date(day, month):
            for sign in zodiac_signs.items():
                if month in sign[1].keys():
                    if (day >= sign[1][month][0]) and (day <= sign[1][month][1]):
                        print(f'Знак зодиака: {sign[0]}')

        else:
            raise Exception('invalid date')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
