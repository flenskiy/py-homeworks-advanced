nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        self.row = 0
        self.items = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.items)
        except StopIteration:
            if self.row > (len(self.my_list) - 1):
                raise StopIteration
            self.items = iter(self.my_list[self.row])
            item = next(self.items)
            self.row += 1
        return item


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
