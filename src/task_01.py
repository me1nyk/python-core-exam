"""
Task 01 — Типи, цикли, умови (15 балів)
========================================
"""


def classify_number(n: int) -> str:
        if n == 0:
            return ("zero")
        if n > 0:
            return ("positive")
        elif n < 0:
            return ("negative")


def fizzbuzz(n: int) -> list[str]:
    result = []
    for n in range (1, n+1):
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))

    return result



def count_evens(numbers: list[int]) -> int:
    evens = 0
    for n in numbers:
        if n % 2 == 0:
            evens += 1

    return evens

