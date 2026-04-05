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
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"
def fizzbuzz(n: int) -> list[str]:
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            list.append("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            list.append("Buzz")
        else :
            list.append(str(i))
    return list
def count_evens(numbers: list[int]) -> int:
    count_p = 0
    for n in numbers:
        if n % 2 == 0:
            count_p += 1
    return count_p
