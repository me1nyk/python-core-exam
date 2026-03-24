import pytest
from src.task_04 import Stack, Circle, Rectangle, Temperature


class TestStack:
    def test_push_and_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self):
        s = Stack()
        s.push(42)
        assert s.peek() == 42
        assert len(s) == 1

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False

    def test_pop_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().pop()

    def test_peek_empty_raises(self):
        with pytest.raises(IndexError):
            Stack().peek()

    def test_len(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert len(s) == 2


class TestShapes:
    def test_circle_area(self):
        c = Circle(5)
        assert abs(c.area() - 78.54) < 0.01

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        assert r.area() == 12

    def test_circle_str(self):
        assert "Circle" in str(Circle(5))
        assert "78.54" in str(Circle(5))

    def test_rectangle_str(self):
        assert "Rectangle" in str(Rectangle(3, 4))
        assert "12" in str(Rectangle(3, 4))


class TestTemperature:
    def test_fahrenheit(self):
        t = Temperature(0)
        assert t.fahrenheit == 32.0

    def test_fahrenheit_100(self):
        t = Temperature(100)
        assert t.fahrenheit == 212.0

    def test_celsius_setter(self):
        t = Temperature(20)
        t.celsius = 30
        assert t.celsius == 30

    def test_below_absolute_zero_raises(self):
        with pytest.raises(ValueError):
            Temperature(-300)

    def test_setter_below_absolute_zero_raises(self):
        t = Temperature(0)
        with pytest.raises(ValueError):
            t.celsius = -300
