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

from pygments.lexer import words
import re
from collections import Counter


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    # Приватний метод для отримання списку слів
    def _get_words(self) -> list[str]:
        # Розбиваємо на слова, видаляємо пунктуацію
        words = re.findall(r'\b\w+\b', self.text.lower())
        return words

    def word_count(self) -> int:
        return len(self._get_words())

    def unique_words(self) -> set[str]:
        return set(self._get_words())

    def most_common(self, n: int) -> list[tuple[str, int]]:
        words = self._get_words()
        counter = Counter(words)
        return counter.most_common(n)

    def longest_word(self) -> str:
        words = self._get_words()
        if not words:
            return ''
        # Сортуємо спочатку за довжиною спадання, потім за алфавітом
        return sorted(words, key=lambda w: (-len(w), w))[0]

    def average_word_length(self) -> float:
        words = self._get_words()
        if not words:
            return 0.0
        avg = sum(len(w) for w in words) / len(words)
        return round(avg, 2)