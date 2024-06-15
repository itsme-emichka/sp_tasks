from typing import Any


def coincidence(array: list[Any] = [], num_range: range | None = None) -> bool:
    final_array = []
    for element in array:
        if (
            (
                element in num_range
            ) or (
                (
                    isinstance(element, float)
                ) and (
                    num_range.start < element < num_range.stop
                )
            )
        ):
            final_array.append(element)
    return final_array


if __name__ == '__main__':
    print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # [3, 4, 5]
    print(coincidence())  # []
    print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # [1, 2, 2.5]
