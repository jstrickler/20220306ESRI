#!/usr/bin/env python

def test_two_plus_two_equals_four():  # <1>
    assert 2 + 2 == 4, "two plus two does NOT equal four!"   #  <2>


def test_answer_is_42():
    assert answer() == 42

def answer():
    return 42
