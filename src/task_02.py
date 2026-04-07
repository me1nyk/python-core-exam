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
    words = sentence.split()
    reversed_list = words[::-1]
    return " ".join(reversed_list)




def is_palindrome(s: str) -> bool:
    # TODO: реалізуйте функцію
    s = s.replace(" ", "")
    s = s.lower()
    return s == s[::-1]



