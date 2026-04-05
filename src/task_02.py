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
import shlex
from pickletools import string1


def reverse_words(sentence: str) -> str:
    list = sentence.split(' ')
    return " ".join(list[::-1])
def is_palindrome(s: str) -> bool:
    s = s.replace(' ', '').lower()
    s1 = s[::-1]
    return s == s1





