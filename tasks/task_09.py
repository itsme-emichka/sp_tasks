def connect_dicts(
    dict1: dict[str, int],
    dict2: dict[str, int]
) -> dict[str, int]:
    if sum(dict1.values()) > sum(dict2.values()):
        primary_dict = dict1
        another_dict = dict2
    else:
        primary_dict = dict2
        another_dict = dict1
    final_dict = dict()
    for key, value in primary_dict.items():
        if value < 10:
            continue
        final_dict[key] = value
    for key, value in another_dict.items():
        if final_dict.get(key, None) or value < 10:
            continue
        final_dict[key] = value
    return dict(sorted(final_dict.items(), key=lambda item: item[1]))


if __name__ == '__main__':
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))
