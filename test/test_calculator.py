from build import calculator as c

import pytest


def test_add():
    assert c.add(30,40,20) == 90
    assert c.add(10,4) == 14
    assert c.add() == 0

def test_subtract():
    assert c.subtract(1,-1,3) == -1
    assert c.subtract(1) == 1
    assert c.subtract(-20,0,1) == -21
    assert c.subtract(0,-21,21) ==0

def test_multiplication():
    assert c.multiplication(3,4,0) ==0
    assert c.multiplication(-3,-4) ==12
    assert c.multiplication() == 0
    assert c.multiplication(-2,4) == -8

