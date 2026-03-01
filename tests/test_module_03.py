import pytest

def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (10 / 0) 

def func1():
    raise ValueError("This is a ValueError")

def test_case02():
    with pytest.raises(ValueError) as excinfo:
        # assert(1,2,3) == (1,2,3)
        func1()
        print(str(excinfo))