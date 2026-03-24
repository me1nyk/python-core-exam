import pytest
from src.task_01 import classify_number, fizzbuzz, count_evens


class TestClassifyNumber:
    def test_negative(self):
        assert classify_number(-5) == "negative"

    def test_zero(self):
        assert classify_number(0) == "zero"

    def test_positive(self):
        assert classify_number(10) == "positive"


class TestFizzBuzz:
    def test_basic(self):
        result = fizzbuzz(15)
        assert result[0] == "1"
        assert result[2] == "Fizz"
        assert result[4] == "Buzz"
        assert result[14] == "FizzBuzz"

    def test_length(self):
        assert len(fizzbuzz(10)) == 10

    def test_no_fizzbuzz_below_15(self):
        result = fizzbuzz(14)
        assert "FizzBuzz" not in result


class TestCountEvens:
    def test_mixed(self):
        assert count_evens([1, 2, 3, 4, 5, 6]) == 3

    def test_all_odd(self):
        assert count_evens([1, 3, 5]) == 0

    def test_empty(self):
        assert count_evens([]) == 0

    def test_negatives(self):
        assert count_evens([-2, -1, 0]) == 2
