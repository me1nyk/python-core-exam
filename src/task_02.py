"""
Task 02 — Функції + рядки (10 балів)
======================================
"""


def reverse_words(sentence: str) -> str:
    sentence = sentence.split ()
    reversed_sentence = sentence[::-1]
    return " ".join(reversed_sentence)



def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]
