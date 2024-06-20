def combine_anagrams(array: list[str]) -> list[list[str]]:
    characters_words: dict[str, list[str]] = dict()
    for word in array:
        anagram_chars = ''.join(sorted(word)), None
        anagram_words: list[str] = characters_words.get(anagram_chars, None)
        if not anagram_words:
            characters_words[anagram_chars] = [word]
            continue
        anagram_words.append(word)
    return [words for words in characters_words.values()]


if __name__ == '__main__':
    print(combine_anagrams(
        [
            'cars',
            'for',
            'potatoes',
            'racs',
            'four',
            'scar',
            'creams',
            'scream'
        ]
        )
    )
