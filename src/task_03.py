"""
Task 03 — Структури даних, comprehension (20 балів)
=====================================================

Завдання 1 (5 балів):
    Напишіть функцію `unique_sorted(numbers)`, яка приймає список чисел і
    повертає відсортований список унікальних значень.
    Приклад: [3, 1, 2, 1, 3] → [1, 2, 3]

Завдання 2 (5 балів):
    Напишіть функцію `word_count(text)`, яка приймає рядок і повертає словник
    {слово: кількість_входжень}. Регістр ігнорується.
    Приклад: "hi hi Hello" → {"hi": 2, "hello": 1}

Завдання 3 (5 балів):
    Використовуючи list comprehension, напишіть функцію `squares_of_evens(numbers)`,
    яка повертає список квадратів лише парних чисел зі вхідного списку.
    Приклад: [1, 2, 3, 4, 5] → [4, 16]

Завдання 4 (5 балів):
    Напишіть функцію `group_by_length(words)`, яка приймає список слів і
    повертає словник {довжина: [слова_такої_довжини]}.
    Приклад: ["hi", "bye", "ok", "hey"] → {2: ["hi", "ok"], 3: ["bye", "hey"]}
"""
from operator import ifloordiv


def unique_sorted(numbers: list) -> list:
    set1 = set(numbers)
    list1 = list(set1)
    list1.sort()
    return list1


def word_count(text: str) -> dict:
    words = text.lower().split()
    dict = {}
    for word in words:
        count = 0
        for word1 in words:
            if word == word1:
                count += 1
        dict[word] = count
    return dict

def squares_of_evens(numbers: list[int]) -> list[int]:
    list = [x**2 for x in numbers if x % 2 == 0]
    return list
def group_by_length(words: list[str]) -> dict:
        dict  = {}
        for word in words:
            length = len(word)
            if length not in dict:
                dict[length] = []
            dict[length].append(word)
        return dict

