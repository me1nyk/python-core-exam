"""
Task 03 — Структури даних, comprehension (20 балів)
=====================================================
"""



def unique_sorted(numbers: list) -> list:
    return sorted (set (numbers))



def word_count(text: str) -> dict:
    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def squares_of_evens(numbers: list[int]) -> list[int]:
    return [n ** 2 for n in numbers if n % 2 == 0]

def group_by_length(words: list[str]) -> dict:
    result = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []

        result[length].append(word)

    return result