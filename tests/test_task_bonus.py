import pytest
from src.task_bonus import TextAnalyzer

TEXT = "the quick brown fox jumps over the lazy dog the"


@pytest.fixture
def analyzer():
    return TextAnalyzer(TEXT)


class TestTextAnalyzer:
    def test_word_count(self, analyzer):
        assert analyzer.word_count() == 10

    def test_unique_words(self, analyzer):
        assert analyzer.unique_words() == {
            "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"
        }

    def test_most_common(self, analyzer):
        top = analyzer.most_common(1)
        assert top[0] == ("the", 3)

    def test_longest_word(self, analyzer):
        assert analyzer.longest_word() == "brown"

    def test_average_word_length(self, analyzer):
        words = TEXT.split()
        expected = round(sum(len(w) for w in words) / len(words), 2)
        assert analyzer.average_word_length() == expected

    def test_empty_text(self):
        a = TextAnalyzer("")
        assert a.word_count() == 0
        assert a.unique_words() == set()
