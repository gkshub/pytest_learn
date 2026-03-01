
import pytest
import sys

const = 9/5

def celsius_to_fahrenheit(celsius = 0):
    return celsius * const + 32

print(celsius_to_fahrenheit(100))

@pytest.mark.skip(reason="This test is not ready yet")
def test_case_01():
    assert type(const) == float

# @pytest.mark.skipif(sys.version_info < (3, 15), reason="Requires Python 3.15 or higher ")
# @pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
# @pytest.mark.skipif(celsius_to_fahrenheit() == 32, reason="default value hence skip")
@pytest.mark.skipif(
    sys.version_info < (3, 15) or sys.platform == "win32",
    reason="Incompatible environment"
)
# this is better than the above two separate skipif decorators 
# as it combines the conditions and provides a single reason
def test_case_02():    
    assert celsius_to_fahrenheit(0) == 32


def test_case_03():
    assert celsius_to_fahrenheit(38.4) == 101.12


