"""
Task 02 — Функції + рядки (10 балів)
======================================

Завдання 1 (5 балів):
    Напишіть функцію `reverse_words(sentence)`, яка приймає рядок і повертає
    його зі словами у зворотному порядку.
    Приклад: "hello world" → "world hello"

Завдання 2 (5 балів):
    Напишіть функцію `is_palindrome(s)`, яка повертає True якщо рядок є
    паліндромом (ігноруйте регістр і пробіли), інакше False.
    Приклад: "A man a plan a canal Panama" → True
"""


def reverse_words(sentence: str) -> str:
    # TODO: реалізуйте функцію
    sentence = sentence.split()
    sentence.reverse()
    return " ".join(sentence)


def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]
