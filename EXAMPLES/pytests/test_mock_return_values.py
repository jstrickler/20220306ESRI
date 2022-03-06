#!/usr/bin/env python
#
import pytest
from unittest.mock import Mock

RETURN_VALUE = 99

ham = Mock(return_value=RETURN_VALUE)  # <1>


class Spam():  # <2>
    def __init__(self):
        self._value = ham()  # <3>

    @property
    def value(self):  # <4>
        return self._value


# dependency to be mocked -- not used in test
# def ham():
#     return 42

def test_whatever():  # <5>
    spam = Spam()  # <6>
    assert RETURN_VALUE == spam.value  # <7>


if __name__ == '__main__':
    pytest.main([__file__])
