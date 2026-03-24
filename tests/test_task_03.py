import pytest
from src.task_03 import unique_sorted, word_count, squares_of_evens, group_by_length


class TestUniqueSorted:
    def test_duplicates(self):
        assert unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]

    def test_already_unique(self):
        assert unique_sorted([5, 3, 1]) == [1, 3, 5]

    def test_empty(self):
        assert unique_sorted([]) == []


class TestWordCount:
    def test_basic(self):
        assert word_count("hi hi hello") == {"hi": 2, "hello": 1}

    def test_case_insensitive(self):
        assert word_count("Hi HI hi") == {"hi": 3}

    def test_empty(self):
        assert word_count("") == {}


class TestSquaresOfEvens:
    def test_mixed(self):
        assert squares_of_evens([1, 2, 3, 4, 5]) == [4, 16]

    def test_all_odd(self):
        assert squares_of_evens([1, 3, 5]) == []

    def test_empty(self):
        assert squares_of_evens([]) == []


class TestGroupByLength:
    def test_basic(self):
        result = group_by_length(["hi", "bye", "ok", "hey"])
        assert sorted(result[2]) == ["hi", "ok"]
        assert sorted(result[3]) == ["bye", "hey"]

    def test_empty(self):
        assert group_by_length([]) == {}

    def test_single(self):
        assert group_by_length(["cat"]) == {3: ["cat"]}
