"""
Task 01 — Типи, цикли, умови (15 балів)
========================================

Завдання 1 (5 балів):
    Напишіть функцію `classify_number(n)`, яка приймає ціле число і повертає:
    - "negative" якщо n < 0
    - "zero"     якщо n == 0
    - "positive" якщо n > 0

Завдання 2 (5 балів):
    Напишіть функцію `fizzbuzz(n)`, яка повертає список рядків від 1 до n (включно):
    - "FizzBuzz" якщо число ділиться на 3 і на 5
    - "Fizz"     якщо ділиться тільки на 3
    - "Buzz"     якщо ділиться тільки на 5
    - інакше — рядкове представлення числа

Завдання 3 (5 балів):
    Напишіть функцію `count_evens(numbers)`, яка приймає список цілих чисел
    і повертає кількість парних чисел у ньому.
"""


def classify_number(n: int) -> str:
    # TODO: реалізуйте функцію
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def fizzbuzz(n: int) -> list[str]:
    # TODO: реалізуйте функцію
    new_LIST = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            new_LIST.append("FizzBuzz")
        elif i % 3 == 0:
            new_LIST.append("Fizz")
        elif i % 5 == 0:
            new_LIST.append("Buzz")
        else:
            new_LIST.append(i)
    return new_LIST


def count_evens(numbers: list[int]) -> int:
    # TODO: реалізуйте функцію
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum = sum + 1
    return sum

