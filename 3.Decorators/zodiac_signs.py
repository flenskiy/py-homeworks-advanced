from decorators import logger

zodiac_signs = {
    'овен': {'март': (21, 31), 'апрель': (1, 19)},
    'телец': {'апрель': (20, 30), 'май': (1, 20)},
    'близнецы': {'май': (20, 31), 'июнь': (1, 21)},
    'рак': {'июнь': (21, 30), 'июль': (1, 22)},
    'лев': {'июль': (23, 31), 'август': (1, 22)},
    'дева': {'август': (23, 31), 'сентябрь': (1, 22)},
    'весы': {'сентябрь': (23, 30), 'октябрь': (1, 23)},
    'скорпион': {'октябрь': (24, 31), 'ноябрь': (1, 21)},
    'стрелец': {'ноябрь': (22, 30), 'декабрь': (1, 21)},
    'козерог': {'декабрь': (22, 31), 'январь': (1, 19)},
    'водолей': {'январь': (20, 31), 'февраль': (1, 18)},
    'рыбы': {'февраль': (19, 28), 'март': (1, 20)},
}


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
