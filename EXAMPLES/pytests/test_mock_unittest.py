#!/usr/bin/env python
#
import pytest
from unittest.mock import Mock

ham = Mock()  # <1>


# system under test
class Spam():  # <2>
    def __init__(self, param):
        self._value = ham(param)  # <3>

    @property
    def value(self):  # <4>
        return self._value

# dependency to be mocked -- not used in test
# def ham(n):
#     pass

def test_spam_calls_ham():   # <5>
    _ = Spam(42)  # <6>
    ham.assert_called_once_with(42)  # <7>


if __name__ == '__main__':
    pytest.main([__file__])
