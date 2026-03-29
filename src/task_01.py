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
from unittest import result


def classify_number(n: int) -> str:
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"

    pass


def fizzbuzz(n: int) -> list[str]:

        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

    # TODO: реалізуйте функцію



def count_evens(numbers: list[int]) -> int:
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count



    # TODO: реалізуйте функцію
    pass
