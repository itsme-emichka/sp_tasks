def sort_list(array: list[int]) -> list[int]:
    if not array:
        return array
    for index, num in enumerate(array):
        if index == 0:
            min_num = num
            max_num = num
            min_num_indexes = [index]
            max_num_indexes = [index]
            continue

        if num < min_num:
            min_num_indexes = [index]
            min_num = num
            continue
        if num > max_num:
            max_num_indexes = [index]
            max_num = num
            continue
        if num == min_num:
            min_num_indexes.append(index)
            continue
        if num == max_num:
            max_num_indexes.append(index)
            continue

    if min_num == max_num:
        array.append(min_num)
        return array

    for index in min_num_indexes:
        array[index] = max_num

    for index in max_num_indexes:
        array[index] = min_num

    array.append(min_num)
    return array


if __name__ == '__main__':
    print(sort_list([]))  # => []
    print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
    print(sort_list([1]))  # => [1, 1]
    print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
    print(sort_list([1, 2, 3, 18, 3, 1, 1, 18, 7, 6, 5, 2, 18, 1]))
