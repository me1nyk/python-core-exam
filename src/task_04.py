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
    - Властивість (property) `celsius` з setter — при встановленні перевіряє що значення >= -273.15,
      інакше raise ValueError("Temperature below absolute zero")
"""

from abc import ABC, abstractmethod
import math


class Stack:
    def __init__(self):
        # TODO: реалізуйте клас
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data


    def __len__(self) -> int:
        return len(self.data)


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        # TODO: реалізуйте клас
        self.radius = radius


    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def __str__(self) -> str:
        return f"Circle: area={self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        # TODO: реалізуйте клас
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle: area={self.area():.2f}"


class Temperature:
    def __init__(self, celsius: float):
        # TODO: реалізуйте клас
        self.celsius = celsius


    @property
    def celsius(self) -> float:
        self.celsius = self._celsius
        return self._celsius


    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32
