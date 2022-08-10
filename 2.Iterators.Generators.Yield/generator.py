nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_iterator(my_list):
    row = 0

    while True:
        for item in my_list[row]:
            yield item
        row += 1
        if row > (len(my_list) - 1):
            break


for item in flat_iterator(nested_list):
    print(item)
