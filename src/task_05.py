from functools import wraps
"""
Task 05 — Генератор простих + декоратор retry (10 балів)
=========================================================

Завдання 1 (5 балів) — Генератор простих чисел:
    Напишіть генератор `prime_generator()`, який нескінченно генерує
    прості числа починаючи з 2: 2, 3, 5, 7, 11, ...

Завдання 2 (5 балів) — Декоратор retry:
    Напишіть декоратор `retry(times)`, який повторює виклик функції
    до `times` разів якщо вона кидає виняток.
    Якщо всі спроби невдалі — пробрасує останній виняток.

    Приклад використання:
        @retry(times=3)
        def unstable():
            ...
"""


def prime_generator(numbers: int):
   for i in range(2, numbers):
       yield i
       pass







def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return (func(*args, **kwargs))
                except Exception as e:
                    print(e)
                    if attempt == times:
                        raise e
            raise Exception("")
        return wrapper
    return decorator


