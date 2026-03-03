import pytest
import math

@pytest.mark.parametrize('test_input', [82, 78, 45, 66])
def test_case_01(test_input):
    assert test_input > 50

@pytest.mark.parametrize("inp, out", [(2, 4), (3, 9), (4, 16)])
def test_case_02(inp, out):
    assert inp**2 == out

my_data = [([2,3,4], 'sum', 9), ([2,3,4], 'prod', 24)]
@pytest.mark.parametrize("a,b,c", my_data)
def test_case_03(a, b, c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c