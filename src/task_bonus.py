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


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def word_count(self, text) -> int:
        return len(self.text)

    def unique_words(self, text) -> set:
        self.text = self.text.lower()
        return sorted(set(self.text))

    def most_common(self, n: int) -> list[tuple]:


    def longest_word(self, text) -> str:




    def average_word_length(self) -> float:
        pass
