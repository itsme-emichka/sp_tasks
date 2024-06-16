from typing import Any


def max_odd(array: list[Any]) -> int | None:
    max_number = 0
    for element in array:
        if not (isinstance(element, int) or isinstance(element, float)):
            continue
        if isinstance(element, float) and element % 1:
            continue
        if not element % 2:
            continue
        if element > max_number:
            max_number = int(element)

    if max_number == 0:
        return None
    return max_number


if __name__ == '__main__':
    print(max_odd([1, 2, 3, 4, 4]))
    print(max_odd([21.0, 2, 3, 4, 4]))
    print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
    print(max_odd(['ololo', 'fufufu']))
    print(max_odd([2, 2, 3.0]))
