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
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)





    # TODO: реалізуйте функцію
    pass


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()

    # перевіряємо, чи рядок однаковий з перевернутим
    return cleaned == cleaned[::-1]
    # TODO: реалізуйте функцію
    pass



