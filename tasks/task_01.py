from typing import Any


def is_palindrome(string: Any) -> bool:
    if string is None:  # Можно обойтись и без этого условия
        return False
    if not isinstance(string, str):
        string = str(string)
    cleared_string = ''.join(filter(str.isalpha, string)).lower()
    left_cur = 0
    right_cur = len(cleared_string) - 1
    while left_cur < len(cleared_string):
        if not cleared_string[left_cur] == cleared_string[right_cur]:
            return False
        left_cur += 1
        right_cur -= 1
    return True


if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal -- Panama"))  # => True
    print(is_palindrome("Madam, I'm Adam!"))  # => True
    print(is_palindrome(333))  # => True
    print(is_palindrome(None))  # => False
    print(is_palindrome("Abracadabra"))  # => False
