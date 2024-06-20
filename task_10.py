def count_words(string: str) -> dict[str, int]:
    cleaned_string = ' '.join(
        [''.join(filter(str.isalpha, word.lower())) for word in string.split()]
    )
    final_dict: dict[str, int] = dict()
    for word in cleaned_string.split():
        word_amount = final_dict.get(word, None)
        if word_amount:
            final_dict[word] = word_amount + 1
            continue
        final_dict[word] = 1
    return final_dict


if __name__ == '__main__':
    print(count_words("A man, a plan, a canal -- Panama"))
    print(count_words("Doo bee doo bee doo"))
