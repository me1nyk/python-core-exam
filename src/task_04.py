"""
Task 04 — ООП: Stack, Shape, Temperature (20 балів)
=====================================================

Завдання 1 (7 балів) — Stack:
    Реалізуйте клас `Stack` зі методами:
    - push(item)   — додає елемент на вершину
    - pop()        — видаляє і повертає верхній елемент (raise IndexError якщо порожній)
    - peek()       — повертає верхній елемент без видалення (raise IndexError якщо порожній)
    - is_empty()   — повертає True якщо стек порожній
    - __len__()    — повертає кількість елементів

Завдання 2 (7 балів) — Shape:
    Реалізуйте абстрактний базовий клас `Shape` з абстрактним методом `area()`.
    Реалізуйте два підкласи:
    - `Circle(radius)`       — площа: π * r²
    - `Rectangle(width, height)` — площа: width * height
    Обидва класи повинні мати метод `__str__` що повертає назву фігури і площу,
    наприклад: "Circle: area=78.54" (округлення до 2 знаків)

Завдання 3 (6 балів) — Temperature:
    Реалізуйте клас `Temperature`:
    - Зберігає температуру в Цельсіях
    - Властивість (property) `fahrenheit` — повертає температуру у Фаренгейтах: (C * 9/5) + 32
    - Властивість (property) `celsius` з setter — при встановленні перев
    іряє що значення >= -273.15,
      інакше raise ValueError("Temperature below absolute zero")
"""

from abc import ABC, abstractmethod
import math


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        return self._data.append(item)

    def pop(self):
        if not self._data == []:
            return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self) -> bool:
        if self._data == []:
            raise IndexError() # не розумію як \yield True - не працює
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        if self.area is not None:
            return f"Circle: area={self.area:.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        if self.area is not None:
            return f"Rectangle: area={self.area:.2f}"


class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32
