import pytest

# Fixtures are kept in conftest.py file and can be used across multiple test files 
# without importing them explicitly. 
# They are automatically discovered by pytest when running tests.

def test_case_01(setup_01):
    del setup_01[-1]
    print("\n in test_case_01")
    print(setup_01)
    assert setup_01 == pytest.weekdays1

def test_case_02(setup_01, setup_02):
    print("\n in test_case_02")
    setup_02.remove("Thursday")
    assert setup_02 == pytest.weekdays2