from typing import Any
from math import prod


def multiply_numbers(inputs: Any = None) -> int:
    if not inputs:
        return
    sequence_of_digits = [int(i) for i in str(inputs) if i.isdigit()]
    if not sequence_of_digits:
        return
    return prod(sequence_of_digits)


if __name__ == '__main__':
    print(multiply_numbers())
    print(multiply_numbers('ss'))
    print(multiply_numbers('1234'))
    print(multiply_numbers('sssdd34'))
    print(multiply_numbers(2.3))
    print(multiply_numbers([5, 6, 4]))
