import pytest
from src.task_05 import prime_generator, retry


class TestPrimeGenerator:
    def test_first_five(self):
        gen = prime_generator()
        primes = [next(gen) for _ in range(5)]
        assert primes == [2, 3, 5, 7, 11]

    def test_first_ten(self):
        gen = prime_generator()
        primes = [next(gen) for _ in range(10)]
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


class TestRetry:
    def test_succeeds_on_first_try(self):
        calls = []

        @retry(times=3)
        def ok():
            calls.append(1)
            return "ok"

        assert ok() == "ok"
        assert len(calls) == 1

    def test_retries_on_failure(self):
        calls = []

        @retry(times=3)
        def flaky():
            calls.append(1)
            if len(calls) < 3:
                raise ValueError("fail")
            return "done"

        assert flaky() == "done"
        assert len(calls) == 3

    def test_raises_after_all_attempts(self):
        @retry(times=3)
        def always_fails():
            raise RuntimeError("boom")

        with pytest.raises(RuntimeError, match="boom"):
            always_fails()
