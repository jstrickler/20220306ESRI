#!/usr/bin/env python
import pytest


def triple(x):  # <1>
    return x * 3

test_data = [(5, 15), ('a', 'aaa'), ([True], [True, True, True])]  # <2>

@pytest.mark.parametrize("input,result", test_data)  # <3>
def test_triple(input, result):  # <4>
    print("input {} result {}:".format(input, result))  # <4>
    assert triple(input) == result   # <5>


if __name__ == "__main__":
    pytest.main([__file__, '-s'])

