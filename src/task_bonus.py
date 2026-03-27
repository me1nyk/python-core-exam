"""
Task Bonus — TextAnalyzer (+10 балів)
======================================

Реалізуйте клас `TextAnalyzer`, який аналізує текст.

Конструктор: `TextAnalyzer(text: str)`

Методи:
    word_count() -> int
        Повертає загальну кількість слів у тексті.

    unique_words() -> set[str]
        Повертає множину унікальних слів (в нижньому регістрі).

    most_common(n: int) -> list[tuple[str, int]]
        Повертає список з n найчастіших слів у форматі [(слово, кількість), ...],
        відсортований за спаданням частоти.

    longest_word() -> str
        Повертає найдовше слово в тексті (при рівності — перше за алфавітом).

    average_word_length() -> float
        Повертає середню довжину слова, округлену до 2 знаків.

Примітка: словом вважається послідовність літер (без пунктуації).
Використайте re.findall(r"[a-zA-Z]+", text) для отримання слів.
"""
import re
from collections import Counter
from itertools import count
from unittest import removeResult


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words = re.findall(r"[a-zA-Z]+", text.lower())

    def word_count(self) -> int:
        return len(self.words)
    def unique_words(self) -> set:
        return set(self.words)

    def most_common(self):
        result = []
        for word in self.words:
            count = 0
            for word1 in self.words:
                if word1 == word:
                    count += 1
            result.append((word, count))
        return set(result) #функція працює якщо вивести окремо її в іншу файл просто повертає слова і їх кількість в різній послідовності
    def longest_word(self) -> str:
        longest = 0
        s = ''
        self.words.sort()
        print(self.words)
        for word in self.words:
            if len(word) > longest:
                longest = len(word)
                s = word
        return s
    def average_word_length(self) -> float:
        suma_target = 0
        for word in self.words:
            for target in word:
                suma_target += 1
        return suma_target / len(self.words)



