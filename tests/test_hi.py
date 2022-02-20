import pytest

from dennisync import hi


class TestHi:
    def test_greet(self):
        assert hi.greet() == "Hello, world!"
