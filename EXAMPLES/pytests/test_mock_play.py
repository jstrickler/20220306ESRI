#!/usr/bin/env python
import pytest
from unittest.mock import Mock


@pytest.fixture
def small_list():   # <1>
    return [1, 2, 3]


def test_m1_returns_correct_list(small_list):
    m1 = Mock(return_value=small_list)  # <2>
    mock_result = m1('a', 'b')  # <3>
    assert mock_result == small_list  # <4>


m2 = Mock()  # <5>

m2.spam('a', 'b')  # <6>
m2.ham('wombat')  # <6>
m2.eggs(1, 2, 3)  # <6>

print("mock calls:", m2.mock_calls)  # <7>

m2.spam.assert_called_with('a', 'b')  # <8>
