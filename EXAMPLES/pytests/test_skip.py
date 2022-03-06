#!/usr/bin/env python
import sys
import pytest

def test_one():  # <1>
    assert 1

@pytest.mark.skip(reason="can not currently test")  # <2>
def test_two():
    assert 1

@pytest.mark.skipif(sys.platform != 'win32', reason="only implemented on Windows")  # <3>
def test_three():
    assert 1

@pytest.mark.xfail  # <4>
def test_four():
    assert 1

@pytest.mark.xfail  # <4>
def test_five():
    assert 0

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
