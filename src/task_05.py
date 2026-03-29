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


def prime_generator():
    n = 2
    while True:
        prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            yield n
        n += 1


    # TODO: реалізуйте генератор
    pass


def retry(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e


            raise last_exception
        return wrapper
    return decorator
    # TODO: реалізуйте декоратор
    pass
