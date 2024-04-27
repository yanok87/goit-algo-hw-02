"""This module checks if the words are palindrome"""

from collections import deque


def is_palindrome(word):
    """This function checks if the word it palindrome"""

    characters = word.strip().lower()
    character_deque = deque(characters)

    while len(character_deque) > 1:
        first = character_deque.popleft()
        last = character_deque.pop()
        if first != last:
            return False

    return True


print(is_palindrome("lsdKjfskf   "))
print(is_palindrome("radaR "))
print(is_palindrome(" aNna"))
