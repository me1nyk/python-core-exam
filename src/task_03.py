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


def unique_sorted(numbers: list) -> list:
    return sorted(set(numbers))


def word_count(text: str) -> dict:
    result = {}
    for word in text.split():
        word = word.lower()
        if f"{word}" in result:
            result[word] += 1
        else:
            result[word] = 1
    return result



def squares_of_evens(numbers: list[int]) -> list[int]:
    return [num ** 2 for num in numbers if num % 2 == 0]


def group_by_length(words: list[str]) -> dict:
    result = {}
    for word in words:
        num = len(word)
        word = word.lower()
        if f"{num}" in result:
            result[num].append(f"{word}")
        else:
            result[num] = [f"{word}"]
    return result
