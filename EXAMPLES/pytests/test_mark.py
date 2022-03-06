#!/usr/bin/env python
import pytest

@pytest.mark.alpha  # <1>
def test_one():
    assert 1

@pytest.mark.alpha  # <1>
def test_two():
    assert 1

@pytest.mark.beta  # <2>
def test_three():
    assert 1

if __name__ == '__main__':
    pytest.main([__file__, '-m alpha'])  # <3>

