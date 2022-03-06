#!/usr/bin/env python
import pytest
import math

FILE_NAME = 'IDONOTEXIST.txt'

def test_missing_filename():
    with pytest.raises(FileNotFoundError):  # <1>
        open(FILE_NAME)  # <2>

def test_list():
    print()
    assert (.1 + .2) == pytest.approx(.3)  # <3>

def test_approximate_pi():
    assert 22 / 7 == pytest.approx(math.pi, .001)  # <4>

