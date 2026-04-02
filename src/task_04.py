"""
Task 04 — ООП: Stack, Shape, Temperature (20 балів)
=====================================================
"""

from abc import ABC, abstractmethod
import math


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        if len (self.data) == 0:
            raise IndexError
        else:
            return self.data.pop()

    def peek(self):
        if len (self.data) == 0:
            raise IndexError
        else:
            return self.data[-1]

    def is_empty(self) -> bool:
        if len (self.data) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        return len(self.data)


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return (self.radius ** 2) * math.pi

    def __str__(self) -> str:
        return f"Circle: area={self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


    def area(self) -> float:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Rectangle: area={self.area():.2f}"





class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("температура нижча абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32

