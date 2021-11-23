nested_lst = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.outer_cursor = 0
        self.inner_cursor = -1
        return self

    def __next__(self):
        self.inner_cursor += 1
        if self.inner_cursor < len(self.nested_list[self.outer_cursor]):
            return self.nested_list[self.outer_cursor][self.inner_cursor]
        else:
            if self.outer_cursor < len(self.nested_list) - 1:
                self.outer_cursor += 1
                self.inner_cursor = 0
                return self.nested_list[self.outer_cursor][self.inner_cursor]
            else:
                raise StopIteration


def flat_generator(nested_list):
    cursor = 0
    while cursor < len(nested_list):
        inner_cursor = 0
        while inner_cursor < len(nested_list[cursor]):
            yield nested_list[cursor][inner_cursor]
            inner_cursor += 1
        cursor += 1


def flat_generator2(my_list):
    for el in my_list:
        if isinstance(el, list):
            yield from flat_generator2(el)
        else:
            yield el


if __name__ == '__main__':
    for item in FlatIterator(nested_lst):
        print(item)

    for item in flat_generator(nested_lst):
        print(item)

    for item in flat_generator2(nested_lst):
        print(item)
