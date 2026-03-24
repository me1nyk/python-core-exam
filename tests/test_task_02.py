import pytest
from src.task_02 import reverse_words, is_palindrome


class TestReverseWords:
    def test_two_words(self):
        assert reverse_words("hello world") == "world hello"

    def test_single_word(self):
        assert reverse_words("hello") == "hello"

    def test_multiple_words(self):
        assert reverse_words("one two three") == "three two one"


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_with_spaces_and_case(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_single_char(self):
        assert is_palindrome("a") is True


